from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

from .data import load_history, update_history
from .backtest import summarize_backtest, walk_forward_backtest
from .calibration import calibrate_return
from .features import FEATURE_COLUMNS, HORIZONS, make_features
from .model import fit_forecast
from .tracking import append_forecasts

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/"config/stocks.csv"
PREDICTIONS=ROOT/"predictions/latest.csv"
BACKTEST=ROOT/"predictions/backtest.csv"

def load_stocks():
    return pd.read_csv(CONFIG)

def run(update_data=True):
    stocks=load_stocks()
    rows=[]; backtest_rows=[]
    run_time=datetime.now(timezone.utc).isoformat()
    for stock in stocks.to_dict("records"):
        symbol=stock["symbol"]
        try:
            prices=update_history(symbol) if update_data else load_history(symbol)
            features=make_features(prices)
            latest_price=float(prices["Close"].iloc[-1])
            row={"run_at_utc":run_time,"symbol":symbol,"name":stock["name"],
                 "shares":stock["shares"],"current_price":latest_price,
                 "data_date":prices.index[-1].date().isoformat(),"status":"ok"}
            successful=0
            for horizon in HORIZONS:
                try:
                    result=fit_forecast(features,FEATURE_COLUMNS,f"target_{horizon}")
                    bt=walk_forward_backtest(features,FEATURE_COLUMNS,f"target_{horizon}",
                                             min_train_rows=80,max_folds=12,step=42)
                    summary=summarize_backtest(bt)
                    calibrated_return, adjustment, calibration_samples=calibrate_return(
                        result.predicted_return,bt)
                    predicted_price=latest_price*(1+calibrated_return)
                    lower_return=max(-0.99,result.lower_return+adjustment)
                    upper_return=max(lower_return,result.upper_return+adjustment)
                    successful+=1
                    row[f"{horizon}_status"]="ok"
                    row[f"{horizon}_raw_predicted_price"]=result.predicted_price
                    row[f"{horizon}_predicted_price"]=predicted_price
                    row[f"{horizon}_expected_return"]=calibrated_return
                    row[f"{horizon}_calibration_adjustment"]=adjustment
                    row[f"{horizon}_calibration_samples"]=calibration_samples
                    row[f"{horizon}_lower_price"]=max(0.0,latest_price*(1+lower_return))
                    row[f"{horizon}_upper_price"]=max(0.0,latest_price*(1+upper_return))
                    row[f"{horizon}_validation_mae"]=result.validation_mae
                    row[f"{horizon}_validation_samples"]=result.validation_samples
                    row[f"{horizon}_training_samples"]=result.training_samples
                    row[f"{horizon}_confidence"]=result.confidence
                    backtest_rows.append({"run_at_utc":run_time,"symbol":symbol,
                        "name":stock["name"],"horizon":horizon,**summary,
                        "calibration_adjustment":adjustment,
                        "calibration_samples":calibration_samples})
                except Exception as exc:
                    row[f"{horizon}_status"]=f"unavailable: {exc}"
                    for suffix in ("raw_predicted_price","predicted_price","expected_return",
                                    "calibration_adjustment","calibration_samples","lower_price",
                                    "upper_price","validation_mae","validation_samples",
                                    "training_samples","confidence"):
                        row[f"{horizon}_{suffix}"]=pd.NA
            if successful==0:
                row["status"]="error: no horizon has enough labelled history"
            rows.append(row)
        except Exception as exc:
            rows.append({"run_at_utc":run_time,"symbol":symbol,"name":stock["name"],
                         "shares":stock["shares"],"current_price":None,"data_date":None,
                         "status":f"error: {exc}"})
    result_df=pd.DataFrame(rows)
    PREDICTIONS.parent.mkdir(parents=True,exist_ok=True)
    result_df.to_csv(PREDICTIONS,index=False)
    pd.DataFrame(backtest_rows).to_csv(BACKTEST,index=False)
    good=result_df[result_df["status"].eq("ok")]
    if not good.empty:
        append_forecasts(good.to_dict("records"),pd.Timestamp(datetime.now(timezone.utc).date()))
    return result_df
