from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from .features import HORIZONS
from .data import load_history

ROOT=Path(__file__).resolve().parents[1]
HISTORY=ROOT/"predictions/history.csv"
LEARNING=ROOT/"predictions/model_learning.csv"
SCORECARD=ROOT/"predictions/model_scorecard.csv"
AVG_LEARNING=ROOT/"predictions/averaging_learning.csv"
AVG_PLAN=ROOT/"predictions/averaging_plan.csv"
CONFIG=ROOT/"config/stocks.csv"
COLUMNS=["forecast_date","target_date","symbol","name","horizon","purchase_price","current_price","predicted_price","predicted_return","lower_price","upper_price","actual_price","actual_return","actual_profit_loss_per_share","break_even_reached","error","abs_error","status"]

def _target_date(forecast_date,symbol,horizon):
    prices=load_history(symbol)
    if prices.empty: raise ValueError(f"No history available for {symbol}")
    last_date=pd.Timestamp(prices.index[-1])
    target=last_date+pd.tseries.offsets.BDay(HORIZONS[horizon])
    return target.date().isoformat()

def load_history_table():
    if not HISTORY.exists(): return pd.DataFrame(columns=COLUMNS)
    df=pd.read_csv(HISTORY)
    for c in COLUMNS:
        if c not in df.columns: df[c]=pd.NA
    return df[COLUMNS]

def _purchase_prices():
    if not CONFIG.exists(): return {}
    c=pd.read_csv(CONFIG)
    return {str(r.symbol):float(r.purchase_price) for r in c.itertuples() if pd.notna(r.purchase_price)}

def evaluate_pending(df):
    if df.empty:return df
    out=df.copy()
    for i,row in out.iterrows():
        if row["status"]=="evaluated":continue
        try:
            prices=load_history(row["symbol"])
            target=pd.Timestamp(row["target_date"])
            candidates=prices.loc[prices.index>=target,"Close"]
            if candidates.empty:continue
            actual=float(candidates.iloc[0])
            actual_return=actual/float(row["current_price"])-1
            error=actual_return-float(row["predicted_return"])
            purchase=row.get("purchase_price")
            purchase=float(purchase) if pd.notna(purchase) else None
            out.at[i,"actual_price"]=actual
            out.at[i,"actual_return"]=actual_return
            out.at[i,"actual_profit_loss_per_share"]=pd.NA if purchase is None else actual-purchase
            out.at[i,"break_even_reached"]=pd.NA if purchase is None else bool(actual>=purchase)
            out.at[i,"error"]=error
            out.at[i,"abs_error"]=abs(error)
            out.at[i,"status"]="evaluated"
        except Exception:
            continue
    return out

def _write_learning_metrics(history):
    evaluated=history[history["status"].eq("evaluated")].copy()
    columns=["symbol","name","horizon","completed","mae","rmse","mape","direction_accuracy","bias","last_evaluated_date"]
    rows=[]
    if not evaluated.empty:
        for (symbol,horizon),g in evaluated.groupby(["symbol","horizon"]):
            err=pd.to_numeric(g["error"],errors="coerce").dropna()
            pred=pd.to_numeric(g["predicted_return"],errors="coerce")
            actual=pd.to_numeric(g["actual_return"],errors="coerce")
            valid=pd.concat([pred,actual],axis=1).dropna()
            if err.empty: continue
            direction=float((np.sign(valid.iloc[:,0])==np.sign(valid.iloc[:,1])).mean()) if not valid.empty else np.nan
            rows.append({
                "symbol":symbol,
                "name":str(g["name"].iloc[-1]),
                "horizon":horizon,
                "completed":len(err),
                "mae":float(err.abs().mean()),
                "rmse":float(np.sqrt((err**2).mean())),
                "mape":float((err.abs()/actual.abs().replace(0,np.nan)).dropna().mean()) if not actual.empty else np.nan,
                "direction_accuracy":direction,
                "bias":float(err.mean()),
                "last_evaluated_date":str(pd.to_datetime(g["target_date"],errors="coerce").max().date()) if pd.notna(pd.to_datetime(g["target_date"],errors="coerce").max()) else "",
            })
    pd.DataFrame(rows,columns=columns).to_csv(LEARNING,index=False)


def _write_scorecard(history):
    evaluated=history[history["status"].eq("evaluated")].copy()
    rows=[]
    if not evaluated.empty:
        for (symbol,horizon),g in evaluated.groupby(["symbol","horizon"]):
            err=pd.to_numeric(g["error"],errors="coerce").dropna()
            if err.empty: continue
            pred=pd.to_numeric(g["predicted_return"],errors="coerce")
            actual=pd.to_numeric(g["actual_return"],errors="coerce")
            valid=pd.concat([pred,actual],axis=1).dropna()
            be=pd.to_numeric(g["break_even_reached"],errors="coerce").dropna()
            rows.append({"symbol":symbol,"name":str(g["name"].iloc[-1]),"horizon":horizon,"completed":len(err),"mae":float(err.abs().mean()),"rmse":float(np.sqrt((err**2).mean())),"direction_accuracy":float((np.sign(valid.iloc[:,0])==np.sign(valid.iloc[:,1])).mean()) if not valid.empty else np.nan,"bias":float(err.mean()),"break_even_rate":float(be.mean()) if not be.empty else np.nan,"last_evaluated_date":str(pd.to_datetime(g["target_date"],errors="coerce").max().date()) if pd.notna(pd.to_datetime(g["target_date"],errors="coerce").max()) else ""})
    pd.DataFrame(rows,columns=["symbol","name","horizon","completed","mae","rmse","direction_accuracy","bias","break_even_rate","last_evaluated_date"]).to_csv(SCORECARD,index=False)

def _evaluate_averaging_plans():
    cols=["symbol","name","entry","buy_price","additional_quantity","capital","cumulative_average","horizon","forecast_exit_price","reached","reached_date","exit_reached","actual_exit_price","profit_vs_cumulative_average"]
    if not AVG_PLAN.exists():
        pd.DataFrame(columns=cols).to_csv(AVG_LEARNING,index=False); return
    plan=pd.read_csv(AVG_PLAN)
    if plan.empty:
        pd.DataFrame(columns=cols).to_csv(AVG_LEARNING,index=False); return
    rows=[]
    for _,r in plan.iterrows():
        try:
            prices=load_history(str(r["symbol"]))
            buy=float(r["buy_price"]); exit_target=float(r["forecast_exit_price"])
            reached_idx=prices.index[prices["Low"]<=buy]
            exit_idx=prices.index[prices["High"]>=exit_target]
            reached=bool(len(reached_idx)); exit_reached=bool(len(exit_idx))
            rows.append({**r.to_dict(),"reached":reached,"reached_date":str(reached_idx[0].date()) if reached else "","exit_reached":exit_reached,"actual_exit_price":exit_target if exit_reached else np.nan,"profit_vs_cumulative_average":exit_target/float(r["cumulative_average"])-1 if exit_reached else np.nan})
        except Exception:
            rows.append({**r.to_dict(),"reached":False,"reached_date":"","exit_reached":False,"actual_exit_price":np.nan,"profit_vs_cumulative_average":np.nan})
    pd.DataFrame(rows).to_csv(AVG_LEARNING,index=False)

def append_forecasts(forecast_rows,forecast_date):
    history=evaluate_pending(load_history_table())
    _write_learning_metrics(history)
    _write_scorecard(history)
    _evaluate_averaging_plans()
    purchase_prices=_purchase_prices()
    existing_keys=set(zip(history["forecast_date"].astype(str),history["symbol"].astype(str),history["horizon"].astype(str)))
    new=[]
    date_str=forecast_date.date().isoformat()
    for row in forecast_rows:
        for horizon in HORIZONS:
            if row.get(f"{horizon}_status")!="ok":continue
            key=(date_str,str(row["symbol"]),horizon)
            if key in existing_keys:continue
            new.append({
                "forecast_date":date_str,
                "target_date":_target_date(forecast_date,str(row["symbol"]),horizon),
                "symbol":row["symbol"],"name":row["name"],"horizon":horizon,
                "purchase_price":purchase_prices.get(str(row["symbol"])),
                "current_price":row["current_price"],
                "predicted_price":row[f"{horizon}_predicted_price"],
                "predicted_return":row[f"{horizon}_expected_return"],
                "lower_price":row[f"{horizon}_lower_price"],
                "upper_price":row[f"{horizon}_upper_price"],
                "actual_price":pd.NA,"actual_return":pd.NA,
                "actual_profit_loss_per_share":pd.NA,"break_even_reached":pd.NA,
                "error":pd.NA,"abs_error":pd.NA,"status":"pending"
            })
    if new:history=pd.concat([history,pd.DataFrame(new)],ignore_index=True)
    history=history[COLUMNS]
    HISTORY.parent.mkdir(parents=True,exist_ok=True)
    history.to_csv(HISTORY,index=False)
    _write_learning_metrics(history)
    _write_scorecard(history)
    _evaluate_averaging_plans()
    return history
