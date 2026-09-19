from __future__ import annotations
from pathlib import Path
import pandas as pd
from .averaging import quantity_for_target_average
from .features import HORIZONS
from .tracking import load_history_table
ROOT=Path(__file__).resolve().parents[1];CONFIG=ROOT/"config/stocks.csv";PREDICTIONS=ROOT/"predictions/latest.csv";REPORT=ROOT/"predictions/portfolio_report.csv";REPORT_MD=ROOT/"predictions/portfolio_report.md";AVG_REPORT=ROOT/"predictions/averaging_scenarios.csv"
def _num(v): return float(v) if pd.notna(v) else None
def build_report():
    stocks=pd.read_csv(CONFIG);forecasts=pd.read_csv(PREDICTIONS) if PREDICTIONS.exists() else pd.DataFrame();history=load_history_table();rows=[];avg_rows=[]
    for stock in stocks.to_dict("records"):
        f=forecasts[forecasts["symbol"].eq(stock["symbol"])]
        if f.empty:continue
        r=f.iloc[0];qty=float(stock["shares"]);avg=float(stock["purchase_price"]) if pd.notna(stock.get("purchase_price")) else None;current=_num(r.get("current_price"))
        o={"symbol":stock["symbol"],"name":stock["name"],"quantity":qty,"purchase_price":avg,"current_price":current}
        fp={h:_num(r.get(f"{h}_predicted_price")) for h in HORIZONS}
        if avg is not None and current is not None:
            o.update(invested_value=qty*avg,current_value=qty*current,current_profit_loss=qty*(current-avg),current_return=current/avg-1)
            o["first_forecast_horizon_at_or_above_purchase_price"]=next((h for h in HORIZONS if fp[h] is not None and fp[h]>=avg),None) or "Not reached in 12M forecast"
            for i,pct in enumerate((0,-0.05,-0.10,-0.15,-0.20),1):
                buy=max(0,current*(1+pct))
                for target_pct in (0.95,0.90,0.85):
                    target=avg*target_pct;q=quantity_for_target_average(qty,avg,buy,target)
                    avg_rows.append({"symbol":stock["symbol"],"name":stock["name"],"buy_price":buy,"price_scenario":f"{int(abs(pct)*100)}% below current" if pct else "current","target_average":target,"additional_quantity":q,"additional_capital":None if q is None else q*buy})
            for h,p in fp.items(): o[f"{h}_profit_loss_at_forecast"]=pd.NA if p is None else qty*(p-avg);o[f"{h}_return_vs_purchase"]=pd.NA if p is None else p/avg-1
        else:
            o.update(invested_value=pd.NA,current_value=pd.NA,current_profit_loss=pd.NA,current_return=pd.NA);o["first_forecast_horizon_at_or_above_purchase_price"]="Purchase price required"
            for h in HORIZONS:o[f"{h}_profit_loss_at_forecast"]=pd.NA;o[f"{h}_return_vs_purchase"]=pd.NA
        for h in HORIZONS:
            o[f"{h}_raw_predicted_price"]=_num(r.get(f"{h}_raw_predicted_price"));o[f"{h}_predicted_price"]=fp[h];o[f"{h}_model"]=r.get(f"{h}_model");o[f"{h}_calibration_adjustment"]=_num(r.get(f"{h}_calibration_adjustment"));o[f"{h}_error_band"]=_num(r.get(f"{h}_error_band"))
        rows.append(o)
    df=pd.DataFrame(rows);REPORT.parent.mkdir(parents=True,exist_ok=True);df.to_csv(REPORT,index=False);pd.DataFrame(avg_rows).to_csv(AVG_REPORT,index=False)
    evaluated=history[history["status"].eq("evaluated")]
    lines=["# Portfolio forecast report","","Models retrain from the latest market history on every scheduled run.","The selected model is chosen using chronological holdout error, with a zero-return baseline included.","Forecast calibration prefers completed real forecast errors for the same stock/horizon, then falls back to walk-forward errors.","Error bands are empirical historical-error bands, not guarantees.","The first forecast horizon is a model checkpoint, not a guaranteed date.","Averaging scenarios are mathematical cost-basis calculations, not buy recommendations.",""]
    if not evaluated.empty:
        lines += [f"Completed forecast evaluations: {len(evaluated)}",f"Mean absolute forecast error: {pd.to_numeric(evaluated['abs_error'],errors='coerce').mean():.2%}",""]
    for _,r in df.iterrows():
        lines += [f"## {r['name']} ({r['symbol']})",f"- Quantity: {r['quantity']}",f"- Purchase price: {r['purchase_price'] if pd.notna(r['purchase_price']) else 'MISSING'}",f"- Current price: {r['current_price']}",f"- Current P/L: ₹{r['current_profit_loss']:.2f}" if pd.notna(r["current_profit_loss"]) else "- Current P/L: purchase price missing",f"- First forecast horizon at/above purchase price: {r['first_forecast_horizon_at_or_above_purchase_price']}",""]
        for h in HORIZONS: lines.append(f"- {h}: ₹{r[f'{h}_predicted_price']} | model={r[f'{h}_model']} | error band=±{r[f'{h}_error_band']}")
        lines += ["","Averaging scenarios: see predictions/averaging_scenarios.csv",""]
    REPORT_MD.write_text("\n".join(lines),encoding="utf-8");return df
