from __future__ import annotations
from pathlib import Path
import math
import pandas as pd
from .averaging import quantity_for_target_average, build_staged_averaging_plan
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
    staged_rows=[]
    candidate_plans=[]
    MAX_STOCK_ADD_CAPITAL_RATIO=0.50
    MAX_PORTFOLIO_ADD_CAPITAL_RATIO=0.20
    MAX_VALIDATION_MAE=0.20
    MAX_ERROR_BAND=0.30

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
            trend20=_num(r.get("return_20d")); ma20=_num(r.get("ma_ratio_20"))
            o["trend_20d_return"]=trend20
            o["trend_20d_health"]="stop_averaging" if trend20 is not None and trend20 <= -0.20 else "ok"
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

            # Build a candidate; final acceptance is subject to model-quality and portfolio-wide capital gates.
            profit_target=0.05
            lower_fp={h:_num(r.get(f"{h}_lower_price")) for h in HORIZONS}
            quality=[]
            for h in HORIZONS:
                if fp[h] is None: continue
                conf=str(r.get(f"{h}_confidence","")).lower()
                mae=_num(r.get(f"{h}_validation_mae"))
                band=_num(r.get(f"{h}_error_band"))
                quality.append(conf in {"medium","high"} and mae is not None and band is not None and mae <= MAX_VALIDATION_MAE and band <= MAX_ERROR_BAND)
            model_quality_ok=any(quality)
            trend_ok=(trend20 is None or trend20 > -0.20) and (ma20 is None or ma20 > -0.15)
            plan=build_staged_averaging_plan(qty,avg,current,fp,profit_target=profit_target,max_add_capital_ratio=MAX_STOCK_ADD_CAPITAL_RATIO,volatility=_num(r.get("atr_pct")),lower_forecasts=lower_fp) if model_quality_ok and trend_ok else None
            candidate_plans.append((stock["symbol"],stock["name"],plan,model_quality_ok and trend_ok))

            for h,p in fp.items():
                o[f"{h}_profit_loss_at_forecast"]=pd.NA if p is None else qty*(p-avg)
                o[f"{h}_return_vs_purchase"]=pd.NA if p is None else p/avg-1
                qreq=quantity_for_target_average(qty,avg,current,p) if p is not None and p>current else None
                o[f"{h}_break_even_additional_qty_at_current"]=None if qreq is None else math.ceil(qreq)
                o[f"{h}_break_even_additional_capital_at_current"]=None if qreq is None else math.ceil(qreq)*current
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
            o[f"{h}_confidence"]=r.get(f"{h}_confidence")
            o[f"{h}_validation_mae"]=_num(r.get(f"{h}_validation_mae"))
        rows.append(o)

    df=pd.DataFrame(rows)
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(REPORT,index=False)
    pd.DataFrame(avg_rows).to_csv(AVG_REPORT,index=False)
    total_invested=float(pd.to_numeric(df["invested_value"],errors="coerce").sum()) if not df.empty else 0.0
    portfolio_budget=total_invested*MAX_PORTFOLIO_ADD_CAPITAL_RATIO
    accepted_capital=0.0
    for symbol,name,plan,model_quality_ok in sorted(candidate_plans,key=lambda x:((list(HORIZONS.keys()).index(x[2]["horizon"]) if x[2] else 999),(x[2]["total_capital"] if x[2] else float("inf")))):
        if plan is None or not model_quality_ok or accepted_capital+plan["total_capital"]>portfolio_budget+1e-9:
            reason="NO QUALIFYING AVERAGING PLAN" if plan is None or not model_quality_ok else "PORTFOLIO BUDGET FULL"
            signal_rows.append({"symbol":symbol,"name":name,"signal":reason,"horizon":pd.NA,"forecast_exit_price":pd.NA,"total_additional_quantity":pd.NA,"total_capital":pd.NA,"final_average":pd.NA,"forecast_profit_percent":pd.NA})
            continue
        accepted_capital+=plan["total_capital"]
        signal_rows.append({"symbol":symbol,"name":name,"signal":"AVERAGING PLAN","horizon":plan["horizon"],"forecast_exit_price":plan["forecast_exit_price"],"conservative_exit_price":plan["conservative_exit_price"],"total_additional_quantity":plan["total_additional_quantity"],"total_capital":plan["total_capital"],"final_average":plan["final_average"],"forecast_profit_percent":plan["forecast_profit_percent"],"conservative_profit_percent":plan["conservative_profit_percent"]})
        for step in plan["rows"]:
            staged_rows.append({"symbol":symbol,"name":name,"plan_date":r.get("market_data_date"),"signal":"AVERAGING PLAN","entry":step["entry"],"buy_price":step["buy_price"],"additional_quantity":step["additional_quantity"],"capital":step["capital"],"cumulative_quantity":step["cumulative_quantity"],"cumulative_average":step["cumulative_average"],"horizon":plan["horizon"],"forecast_exit_price":plan["forecast_exit_price"],"conservative_exit_price":plan["conservative_exit_price"],"forecast_profit_percent":plan["forecast_profit_percent"],"conservative_profit_percent":plan["conservative_profit_percent"]})
    pd.DataFrame(signal_rows).to_csv(ROOT/"predictions/averaging_profit_signals.csv",index=False)
    pd.DataFrame(staged_rows).to_csv(ROOT/"predictions/averaging_plan.csv",index=False)

    evaluated=history[history["status"].eq("evaluated")]
    lines=[
        "# Portfolio forecast report","",
        "Models retrain from the latest market history on every scheduled run.",
        "The selected model is chosen using chronological holdout error, with a zero-return baseline included.",
        "Forecast calibration uses completed real forecast errors for the same stock/horizon when available, then walk-forward errors.",
        "Error bands are empirical historical-error bands, not guarantees.",
        "Averaging plans require medium/high model confidence, validation MAE <= 20%, error band <= 30%, a conservative lower-forecast profit check, and no severe 20-day deterioration.",
        "Portfolio-wide additional averaging capital is capped at 20% of configured invested cost; each stock is capped at 50%.",
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
