from __future__ import annotations
from pathlib import Path
import pandas as pd
from .averaging import quantity_for_target_average
from .features import HORIZONS
from .tracking import load_history_table

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/"config/stocks.csv"
PREDICTIONS=ROOT/"predictions/latest.csv"
REPORT=ROOT/"predictions/portfolio_report.csv"
REPORT_MD=ROOT/"predictions/portfolio_report.md"
AVG_REPORT=ROOT/"predictions/averaging_scenarios.csv"
DIVIDENDS=ROOT/"data/dividends.csv"
DIV_HISTORY=ROOT/"predictions/dividend_history.csv"

def _num(v):
    return float(v) if pd.notna(v) else None

def _horizon_label(row, h):
    status=str(row.get(f"{h}_status",""))
    price=_num(row.get(f"{h}_predicted_price"))
    if price is None or status.startswith("unavailable"):
        return None
    return price

def build_report():
    stocks=pd.read_csv(CONFIG)
    forecasts=pd.read_csv(PREDICTIONS) if PREDICTIONS.exists() else pd.DataFrame()
    history=load_history_table()
    divs=pd.read_csv(DIVIDENDS) if DIVIDENDS.exists() else pd.DataFrame()
    divhist=pd.read_csv(DIV_HISTORY) if DIV_HISTORY.exists() else pd.DataFrame()
    rows=[]
    avg_rows=[]
    signal_rows=[]

    for stock in stocks.to_dict("records"):
        f=forecasts[forecasts["symbol"].eq(stock["symbol"])] if not forecasts.empty and "symbol" in forecasts else pd.DataFrame()
        if f.empty:
            continue
        r=f.iloc[0]
        qty=float(stock["shares"])
        avg=float(stock["purchase_price"]) if pd.notna(stock.get("purchase_price")) else None
        current=_num(r.get("current_price"))
        o={
            "symbol":stock["symbol"],"name":stock["name"],"quantity":qty,
            "purchase_price":avg,"current_price":current,
            "price_source":"latest available market close",
            "market_data_date":r.get("data_date")
        }

        d=divs[divs["symbol"].eq(stock["symbol"])] if not divs.empty else pd.DataFrame()
        if not d.empty:
            d=d.sort_values("ex_date").iloc[0]
            o.update(next_dividend_per_share=d.get("dividend_per_share"),
                     next_dividend_yield=d.get("dividend_yield"),
                     next_dividend_ex_date=d.get("ex_date"),
                     next_dividend_record_date=d.get("record_date"),
                     next_dividend_cum_date=d.get("cum_date"),
                     next_dividend_status=d.get("status"))
        else:
            o.update(next_dividend_per_share=pd.NA,next_dividend_yield=pd.NA,
                     next_dividend_ex_date=pd.NA,next_dividend_record_date=pd.NA,
                     next_dividend_cum_date=pd.NA,next_dividend_status="NONE")

        dh=divhist[divhist["symbol"].eq(stock["symbol"])] if not divhist.empty else pd.DataFrame()
        if not dh.empty:
            o.update(
                avg_ex_day_return=pd.to_numeric(dh["ex_day_return"],errors="coerce").mean(),
                avg_recovery_days=pd.to_numeric(dh["recovery_days"],errors="coerce").mean(),
                avg_5d_total_return=pd.to_numeric(dh["total_return_5d_including_dividend"],errors="coerce").mean(),
                historical_dividend_events=len(dh))
        else:
            o.update(avg_ex_day_return=pd.NA,avg_recovery_days=pd.NA,
                     avg_5d_total_return=pd.NA,historical_dividend_events=0)

        fp={h:_horizon_label(r,h) for h in HORIZONS}

        if avg is not None and current is not None:
            o.update(
                invested_value=qty*avg,
                current_value=qty*current,
                current_profit_loss=qty*(current-avg),
                current_return=current/avg-1)

            future=[h for h,p in fp.items() if p is not None and p>=avg]
            available=[h for h,p in fp.items() if p is not None]
            o["first_forecast_horizon_at_or_above_purchase_price"] = (
                future[0] if future else ("Not reached in available forecast" if available else "Unavailable: insufficient history")
            )

            for pct in (0,-0.05,-0.10,-0.15,-0.20):
                buy=max(0,current*(1+pct))
                for target_pct in (0.95,0.90,0.85):
                    target=avg*target_pct
                    q=quantity_for_target_average(qty,avg,buy,target)
                    avg_rows.append({
                        "symbol":stock["symbol"],"name":stock["name"],
                        "buy_price":buy,
                        "price_scenario":f"{int(abs(pct)*100)}% below current" if pct else "current",
                        "target_average":target,
                        "additional_quantity":q,
                        "additional_capital":None if q is None else q*buy
                    })

            # Profit-oriented averaging signal: find the smallest mathematical
            # averaging capital among price scenarios that can put the new average
            # below a forecast exit price by the configured profit target.
            profit_target=0.05
            scenarios=(("current",current),("5% below",current*0.95),("10% below",current*0.90),("15% below",current*0.85),("20% below",current*0.80))
            best_signal=None
            for scenario,buy_price in scenarios:
                for h in HORIZONS:
                    forecast=fp[h]
                    if forecast is None or buy_price<=0 or forecast <= buy_price:
                        continue
                    target_avg=forecast/(1+profit_target)
                    q=quantity_for_target_average(qty,avg,buy_price,target_avg)
                    if q is None or q <= 0:
                        continue
                    capital=q*buy_price
                    new_avg=new_average= (qty*avg + q*buy_price)/(qty+q)
                    expected_profit=(forecast/new_avg)-1
                    candidate={"symbol":stock["symbol"],"name":stock["name"],"signal":"AVERAGING CANDIDATE",
                               "buy_price":buy_price,"price_scenario":scenario,"horizon":h,"forecast_exit_price":forecast,
                               "additional_quantity":math.ceil(q),"capital_required":math.ceil(capital),
                               "new_average":new_avg,"forecast_profit_percent":expected_profit,
                               "profit_target_percent":profit_target}
                    if best_signal is None or candidate["capital_required"] < best_signal["capital_required"]:
                        best_signal=candidate
            if best_signal is None:
                best_signal={"symbol":stock["symbol"],"name":stock["name"],"signal":"NO QUALIFYING AVERAGING SIGNAL",
                             "buy_price":pd.NA,"price_scenario":pd.NA,"horizon":pd.NA,"forecast_exit_price":pd.NA,
                             "additional_quantity":pd.NA,"capital_required":pd.NA,"new_average":pd.NA,
                             "forecast_profit_percent":pd.NA,"profit_target_percent":profit_target}
            signal_rows.append(best_signal)

            for h,p in fp.items():
                o[f"{h}_profit_loss_at_forecast"]=pd.NA if p is None else qty*(p-avg)
                o[f"{h}_return_vs_purchase"]=pd.NA if p is None else p/avg-1
                qreq=quantity_for_target_average(qty,avg,current,p) if p is not None and p>current else None
                o[f"{h}_break_even_additional_qty_at_current"]=qreq
                o[f"{h}_break_even_additional_capital_at_current"]=None if qreq is None else qreq*current
        else:
            o.update(invested_value=pd.NA,current_value=pd.NA,current_profit_loss=pd.NA,current_return=pd.NA)
            o["first_forecast_horizon_at_or_above_purchase_price"]="Purchase price required"
            for h in HORIZONS:
                o[f"{h}_profit_loss_at_forecast"]=pd.NA
                o[f"{h}_return_vs_purchase"]=pd.NA

        for h in HORIZONS:
            o[f"{h}_raw_predicted_price"]=_num(r.get(f"{h}_raw_predicted_price"))
            o[f"{h}_predicted_price"]=fp[h]
            o[f"{h}_model"]=r.get(f"{h}_model")
            o[f"{h}_status"]=r.get(f"{h}_status")
            o[f"{h}_calibration_adjustment"]=_num(r.get(f"{h}_calibration_adjustment"))
            o[f"{h}_error_band"]=_num(r.get(f"{h}_error_band"))
        rows.append(o)

    df=pd.DataFrame(rows)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(REPORT,index=False)
    pd.DataFrame(avg_rows).to_csv(AVG_REPORT,index=False)
    pd.DataFrame(signal_rows).to_csv(ROOT/"predictions/averaging_profit_signals.csv",index=False)

    evaluated=history[history["status"].eq("evaluated")]
    lines=[
        "# Portfolio forecast report","",
        "Models retrain from the latest market history on every scheduled run.",
        "The selected model is chosen using chronological holdout error, with a zero-return baseline included.",
        "Forecast calibration uses completed real forecast errors for the same stock/horizon when available, then walk-forward errors.",
        "Error bands are empirical historical-error bands, not guarantees.",
        "Forecast horizons marked unavailable have insufficient labelled historical data and are not treated as failed forecasts.",
        "The first forecast horizon is a model checkpoint, not a guaranteed date.",
        "Averaging scenarios are mathematical cost-basis calculations. The profit-signal table is a model-generated scenario, not a guarantee or personalized financial advice.",""
    ]
    if not evaluated.empty:
        mae=pd.to_numeric(evaluated["abs_error"],errors="coerce").mean()
        lines += [f"Completed forecast evaluations: {len(evaluated)}",f"Mean absolute forecast error: {mae:.2%}",""]

    for _,r in df.iterrows():
        current_pl = f"₹{r['current_profit_loss']:.2f}" if pd.notna(r["current_profit_loss"]) else "purchase price missing"
        lines += [
            f"## {r['name']} ({r['symbol']})",
            f"- Quantity: {r['quantity']}",
            f"- Purchase price: {r['purchase_price'] if pd.notna(r['purchase_price']) else 'MISSING'}",
            f"- Current price: {r['current_price']}",
            f"- Current P/L: {current_pl}",
            f"- First forecast horizon at/above purchase price: {r['first_forecast_horizon_at_or_above_purchase_price']}",
            ""
        ]
        for h in HORIZONS:
            status=str(r[f"{h}_status"])
            p=r[f"{h}_predicted_price"]
            if pd.isna(p) or status.startswith("unavailable"):
                lines.append(f"- {h}: N/A — {status.replace('unavailable: ','')}")
            else:
                lines.append(f"- {h}: ₹{p:.2f} | model={r[f'{h}_model']} | error band=±{r[f'{h}_error_band']:.2%}")
        lines += ["","Dividend data: upcoming and historical analysis are in the report CSV.",
                  "Averaging scenarios: see predictions/averaging_scenarios.csv",""]

    REPORT_MD.write_text("\n".join(lines),encoding="utf-8")
    return df
