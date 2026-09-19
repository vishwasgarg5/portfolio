from __future__ import annotations
from pathlib import Path
import pandas as pd
from .features import HORIZONS
from .data import load_history
ROOT=Path(__file__).resolve().parents[1];HISTORY=ROOT/"predictions/history.csv";CONFIG=ROOT/"config/stocks.csv"
COLUMNS=["forecast_date","target_date","symbol","name","horizon","purchase_price","current_price","predicted_price","predicted_return","lower_price","upper_price","actual_price","actual_return","actual_profit_loss_per_share","break_even_reached","error","abs_error","status"]

def _target_date(forecast_date,symbol,horizon):
    prices=load_history(symbol)
    if prices.empty: raise ValueError(f"No history available for {symbol}")
    dates=pd.DatetimeIndex(prices.index);eligible=dates[dates>=forecast_date];start_pos=int(dates.get_loc(eligible[0])) if len(eligible) else len(dates)-1
    target_pos=start_pos+HORIZONS[horizon]
    if target_pos>=len(dates): return (dates[-1]+pd.tseries.offsets.BDay(target_pos-(len(dates)-1))).date().isoformat()
    return dates[target_pos].date().isoformat()

def load_history_table():
    if not HISTORY.exists(): return pd.DataFrame(columns=COLUMNS)
    df=pd.read_csv(HISTORY)
    for c in COLUMNS:
        if c not in df.columns: df[c]=pd.NA
    return df[COLUMNS]

def _purchase_prices():
    if not CONFIG.exists(): return {}
    c=pd.read_csv(CONFIG);return {str(r.symbol):float(r.purchase_price) for r in c.itertuples() if pd.notna(r.purchase_price)}

def evaluate_pending(df):
    if df.empty:return df
    out=df.copy()
    for i,row in out.iterrows():
        if row["status"]=="evaluated":continue
        try:
            prices=load_history(row["symbol"]);target=pd.Timestamp(row["target_date"]);candidates=prices.loc[prices.index>=target,"Close"]
            if candidates.empty:continue
            actual=float(candidates.iloc[0]);actual_return=actual/float(row["current_price"])-1;error=actual_return-float(row["predicted_return"])
            purchase=row.get("purchase_price");purchase=float(purchase) if pd.notna(purchase) else None
            out.at[i,"actual_price"]=actual;out.at[i,"actual_return"]=actual_return;out.at[i,"actual_profit_loss_per_share"]=pd.NA if purchase is None else actual-purchase
            out.at[i,"break_even_reached"]=pd.NA if purchase is None else bool(actual>=purchase)
            out.at[i,"error"]=error;out.at[i,"abs_error"]=abs(error);out.at[i,"status"]="evaluated"
        except Exception: continue
    return out

def append_forecasts(forecast_rows,forecast_date):
    history=evaluate_pending(load_history_table());purchase_prices=_purchase_prices()
    existing_keys=set(zip(history["forecast_date"].astype(str),history["symbol"].astype(str),history["horizon"].astype(str)))
    new=[];date_str=forecast_date.date().isoformat()
    for row in forecast_rows:
        for horizon in HORIZONS:
            if row.get(f"{horizon}_status")!="ok":continue
            key=(date_str,str(row["symbol"]),horizon)
            if key in existing_keys:continue
            new.append({"forecast_date":date_str,"target_date":_target_date(forecast_date,str(row["symbol"]),horizon),
                        "symbol":row["symbol"],"name":row["name"],"horizon":horizon,
                        "purchase_price":purchase_prices.get(str(row["symbol"])),"current_price":row["current_price"],
                        "predicted_price":row[f"{horizon}_predicted_price"],"predicted_return":row[f"{horizon}_expected_return"],
                        "lower_price":row[f"{horizon}_lower_price"],"upper_price":row[f"{horizon}_upper_price"],
                        "actual_price":pd.NA,"actual_return":pd.NA,"actual_profit_loss_per_share":pd.NA,
                        "break_even_reached":pd.NA,"error":pd.NA,"abs_error":pd.NA,"status":"pending"})
    if new:history=pd.concat([history,pd.DataFrame(new)],ignore_index=True)
    history=history[COLUMNS];HISTORY.parent.mkdir(parents=True,exist_ok=True);history.to_csv(HISTORY,index=False);return history
