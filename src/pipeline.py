from __future__ import annotations
from datetime import datetime, timezone
import numpy as np
from pathlib import Path
import pandas as pd
from .data import load_history, update_history, load_benchmark, update_benchmark
from .backtest import summarize_backtest, walk_forward_backtest
from .calibration import calibrate_return, empirical_error_band
from .features import FEATURE_COLUMNS, HORIZONS, make_features
from .model import fit_forecast
from .tracking import append_forecasts, evaluate_pending, load_history_table
from .dividends import update_dividends
ROOT=Path(__file__).resolve().parents[1];CONFIG=ROOT/"config/stocks.csv";PREDICTIONS=ROOT/"predictions/latest.csv";BACKTEST=ROOT/"predictions/backtest.csv"
def load_stocks(): return pd.read_csv(CONFIG)
def run(update_data=True):
    stocks=load_stocks();rows=[];backtest_rows=[];run_time=datetime.now(timezone.utc).isoformat();tracked=evaluate_pending(load_history_table())
    prior=pd.read_csv(PREDICTIONS) if PREDICTIONS.exists() else pd.DataFrame()
    try: benchmark=update_benchmark() if update_data else load_benchmark()
    except Exception: benchmark=None
    for stock in stocks.to_dict("records"):
        symbol=stock["symbol"]
        try:
            prices=update_history(symbol) if update_data else load_history(symbol)
            if prices.empty or len(prices)<60: raise ValueError("insufficient history for data-quality gate")
            if not prices.index.is_monotonic_increasing: raise ValueError("history dates are not ordered")
            last_date=pd.Timestamp(prices.index[-1]).normalize(); today=pd.Timestamp.now(tz="UTC").tz_convert("Asia/Kolkata").tz_localize(None).normalize()
            if (today-last_date).days>7: raise ValueError(f"stale market data: {last_date.date()}")
            ohlc=prices[["Open","High","Low","Close"]].apply(pd.to_numeric,errors="coerce")
            if ohlc.isna().all(axis=1).tail(20).any() or (ohlc<=0).any().any(): raise ValueError("invalid OHLC data")
            features=make_features(prices,benchmark);latest_price=float(prices["Close"].iloc[-1])
            row={"run_at_utc":run_time,"symbol":symbol,"name":stock["name"],"shares":stock["shares"],"current_price":latest_price,"data_date":prices.index[-1].date().isoformat(),"status":"ok","benchmark_data":"available" if benchmark is not None else "unavailable","volatility_20":float(features["volatility_20"].iloc[-1]) if pd.notna(features["volatility_20"].iloc[-1]) else pd.NA,"atr_pct":float(features["atr_pct"].iloc[-1]) if pd.notna(features["atr_pct"].iloc[-1]) else pd.NA,"return_20d":float(features["return_20d"].iloc[-1]) if pd.notna(features["return_20d"].iloc[-1]) else pd.NA,"ma_ratio_20":float(features["ma_ratio_20"].iloc[-1]) if pd.notna(features["ma_ratio_20"].iloc[-1]) else pd.NA}
            successful=0
            for horizon in HORIZONS:
                try:
                    result=fit_forecast(features,FEATURE_COLUMNS,f"target_{horizon}")
                    bt=walk_forward_backtest(features,FEATURE_COLUMNS,f"target_{horizon}",80,12,42,"auto");summary=summarize_backtest(bt)
                    completed=tracked[(tracked["symbol"].eq(symbol))&(tracked["horizon"].eq(horizon))&(tracked["status"].eq("evaluated"))]
                    calibrated_return,adjustment,calibration_samples=calibrate_return(result.predicted_return,bt,completed["error"].tolist() if not completed.empty else None)
                    band=empirical_error_band(bt,abs(result.upper_return-result.predicted_return)/1.28);predicted_price=latest_price*(1+calibrated_return)
                    lower_return=max(-0.99,calibrated_return-band);upper_return=calibrated_return+band;successful+=1
                    row[f"{horizon}_status"]="ok";row[f"{horizon}_raw_predicted_price"]=result.predicted_price;row[f"{horizon}_predicted_price"]=predicted_price;row[f"{horizon}_expected_return"]=calibrated_return;row[f"{horizon}_calibration_adjustment"]=adjustment;row[f"{horizon}_calibration_samples"]=calibration_samples;row[f"{horizon}_error_band"]=band;row[f"{horizon}_lower_price"]=max(0.0,latest_price*(1+lower_return));row[f"{horizon}_upper_price"]=max(0.0,latest_price*(1+upper_return));row[f"{horizon}_validation_mae"]=result.validation_mae;row[f"{horizon}_validation_samples"]=result.validation_samples;row[f"{horizon}_training_samples"]=result.training_samples;row[f"{horizon}_confidence"]=result.confidence;row[f"{horizon}_model"]=result.model_name
                    row[f"{horizon}_candidate_mae_hist"]=result.candidate_mae.get("hist");row[f"{horizon}_candidate_mae_extra_trees"]=result.candidate_mae.get("extra_trees");row[f"{horizon}_candidate_mae_historical_median"]=result.candidate_mae.get("historical_median")
                    old=prior[prior["symbol"].eq(symbol)].iloc[0] if not prior.empty and "symbol" in prior and not prior[prior["symbol"].eq(symbol)].empty else None
                    oldp=float(old.get(f"{horizon}_predicted_price")) if old is not None and pd.notna(old.get(f"{horizon}_predicted_price")) else np.nan
                    change=(predicted_price/oldp-1.0) if np.isfinite(oldp) and oldp>0 else np.nan
                    row[f"{horizon}_prediction_change_vs_previous"]=change
                    row[f"{horizon}_prediction_stability"]="stable" if not np.isfinite(change) or abs(change)<=0.10 else ("watch" if abs(change)<=0.20 else "large_change")
                    model_counts=bt["model_name"].value_counts().to_dict() if not bt.empty else {}
                    row[f"{horizon}_backtest_model_mix"]=";".join(f"{k}:{v}" for k,v in model_counts.items())
                    backtest_rows.append({"run_at_utc":run_time,"symbol":symbol,"name":stock["name"],"horizon":horizon,**summary,"selected_model_for_current_forecast":result.model_name,"backtest_model_mix":row[f"{horizon}_backtest_model_mix"],"calibration_adjustment":adjustment,"calibration_samples":calibration_samples,"error_band":band})
                except Exception as exc:
                    row[f"{horizon}_status"]=f"unavailable: {exc}"
                    for suffix in ("raw_predicted_price","predicted_price","expected_return","prediction_change_vs_previous","prediction_stability","calibration_adjustment","calibration_samples","error_band","lower_price","upper_price","validation_mae","validation_samples","training_samples","confidence","model","candidate_mae_hist","candidate_mae_extra_trees","candidate_mae_historical_median","backtest_model_mix"): row[f"{horizon}_{suffix}"]=pd.NA
            if successful==0:row["status"]="error: no horizon has enough labelled history"
            rows.append(row)
        except Exception as exc:rows.append({"run_at_utc":run_time,"symbol":symbol,"name":stock["name"],"shares":stock["shares"],"current_price":None,"data_date":None,"status":f"error: {exc}"})
    result_df=pd.DataFrame(rows);PREDICTIONS.parent.mkdir(parents=True,exist_ok=True);result_df.to_csv(PREDICTIONS,index=False);pd.DataFrame(backtest_rows).to_csv(BACKTEST,index=False)
    try:
        stocks = load_stocks()
        prices = {str(r['symbol']): float(r['current_price']) for r in rows if r.get('current_price') is not None}
        upcoming, historical, capture_summary = update_dividends(stocks, prices)
        print(f'Dividend events: {len(upcoming)} upcoming, {len(historical)} historical, {len(capture_summary)} capture horizons')
    except Exception as exc:
        print(f'Dividend update unavailable: {exc}')
    good=result_df[result_df["status"].eq("ok")]
    if not good.empty:
        # Use the latest market-data date, not the calendar date of the workflow run.
        # A weekend/holiday run therefore keeps the forecast anchored to the last trading session.
        forecast_date=pd.Timestamp(max(r["data_date"] for r in good.to_dict("records")))
        append_forecasts(good.to_dict("records"),forecast_date)
    return result_df
