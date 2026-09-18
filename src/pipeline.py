from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

from .data import load_history, update_history
from .features import FEATURE_COLUMNS, HORIZONS, make_features
from .model import fit_forecast


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "stocks.csv"
PREDICTIONS = ROOT / "predictions" / "latest.csv"


def load_stocks() -> pd.DataFrame:
    return pd.read_csv(CONFIG)


def run(update_data: bool = True) -> pd.DataFrame:
    stocks = load_stocks()
    rows: list[dict] = []
    run_time = datetime.now(timezone.utc).isoformat()

    for stock in stocks.to_dict("records"):
        symbol = stock["symbol"]
        try:
            prices = update_history(symbol) if update_data else load_history(symbol)
            features = make_features(prices)
            latest_price = float(prices["Close"].iloc[-1])
            row = {
                "run_at_utc": run_time,
                "symbol": symbol,
                "name": stock["name"],
                "shares": stock["shares"],
                "current_price": latest_price,
                "data_date": prices.index[-1].date().isoformat(),
                "status": "ok",
            }

            for horizon in HORIZONS:
                result = fit_forecast(
                    features,
                    FEATURE_COLUMNS,
                    f"target_{horizon}",
                )
                row[f"{horizon}_predicted_price"] = result.predicted_price
                row[f"{horizon}_expected_return"] = result.predicted_return
                row[f"{horizon}_lower_price"] = latest_price * (1 + result.lower_return)
                row[f"{horizon}_upper_price"] = latest_price * (1 + result.upper_return)
                row[f"{horizon}_validation_mae"] = result.validation_mae
                row[f"{horizon}_validation_samples"] = result.validation_samples

            rows.append(row)
        except Exception as exc:
            rows.append({
                "run_at_utc": run_time,
                "symbol": symbol,
                "name": stock["name"],
                "shares": stock["shares"],
                "current_price": None,
                "data_date": None,
                "status": f"error: {exc}",
            })

    result_df = pd.DataFrame(rows)
    PREDICTIONS.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(PREDICTIONS, index=False)
    return result_df
