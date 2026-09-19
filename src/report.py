from __future__ import annotations
from pathlib import Path
import pandas as pd
from .averaging import averaging_scenarios
from .features import HORIZONS

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/"config/stocks.csv"
PREDICTIONS=ROOT/"predictions/latest.csv"
REPORT=ROOT/"predictions/portfolio_report.csv"
REPORT_MD=ROOT/"predictions/portfolio_report.md"

def build_report():
    stocks=pd.read_csv(CONFIG)
    forecasts=pd.read_csv(PREDICTIONS) if PREDICTIONS.exists() else pd.DataFrame()
    rows=[]
    for stock in stocks.to_dict("records"):
        f=forecasts[forecasts["symbol"].eq(stock["symbol"])]
        if f.empty: continue
        r=f.iloc[0]
        qty=float(stock["shares"])
        raw=stock.get("purchase_price")
        avg=float(raw) if pd.notna(raw) and str(raw).strip() else None
        current=float(r["current_price"]) if pd.notna(r.get("current_price")) else None
        o={"symbol":stock["symbol"],"name":stock["name"],"quantity":qty,
           "purchase_price":avg,"current_price":current}
        if avg is not None and current is not None:
            o.update(invested_value=qty*avg,current_value=qty*current,
                     current_profit_loss=qty*(current-avg),current_return=current/avg-1)
            crossing=next((h for h in HORIZONS if pd.notna(r.get(f"{h}_predicted_price")) and float(r[f"{h}_predicted_price"])>=avg),None)
            o["first_forecast_horizon_at_or_above_purchase_price"]=crossing or "Not reached in 12M forecast"
            for i,s in enumerate(averaging_scenarios(qty,avg,current),1):
                o[f"avg_target_{i}"]=s["target_average"]
                o[f"avg_qty_at_current_{i}"]=s["additional_quantity"]
                o[f"avg_capital_at_current_{i}"]=s["additional_capital"]
        else:
            o.update(invested_value=pd.NA,current_value=pd.NA,current_profit_loss=pd.NA,current_return=pd.NA)
            o["first_forecast_horizon_at_or_above_purchase_price"]="Purchase price required"
            for i in range(1,4):
                o[f"avg_target_{i}"]=pd.NA;o[f"avg_qty_at_current_{i}"]=pd.NA;o[f"avg_capital_at_current_{i}"]=pd.NA
        for h in HORIZONS:
            p=r.get(f"{h}_predicted_price")
            o[f"{h}_predicted_price"]=p
            o[f"{h}_profit_loss_at_forecast"]=pd.NA if avg is None or pd.isna(p) else qty*(float(p)-avg)
            o[f"{h}_return_vs_purchase"]=pd.NA if avg is None or pd.isna(p) else float(p)/avg-1
        rows.append(o)
    df=pd.DataFrame(rows)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(REPORT,index=False)
    lines=["# Portfolio forecast report","","Forecasts are model estimates, not guarantees.",""]
    for _,r in df.iterrows():
        lines += [f"## {r['name']} ({r['symbol']})",
                  f"- Quantity: {r['quantity']}",
                  f"- Purchase price: {r['purchase_price'] if pd.notna(r['purchase_price']) else 'MISSING'}",
                  f"- Current price: {r['current_price']}",
                  f"- First forecast horizon at/above purchase price: {r['first_forecast_horizon_at_or_above_purchase_price']}",""]
        for h in HORIZONS: lines.append(f"- {h} forecast: {r[f'{h}_predicted_price']}")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines),encoding="utf-8")
    return df
