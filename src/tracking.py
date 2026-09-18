from __future__ import annotations

from pathlib import Path
import pandas as pd

from .features import HORIZONS
from .data import load_history

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "predictions" / "history.csv"
MONTHS = {"3M": 3, "6M": 6, "9M": 9, "12M": 12}

COLUMNS = [
    "forecast_date", "target_date", "symbol", "name", "horizon",
    "current_price", "predicted_price", "predicted_return",
    "lower_price", "upper_price", "actual_price", "actual_return",
    "error", "abs_error", "status",
]


def _target_date(forecast_date: pd.Timestamp, horizon: str) -> str:
    return (forecast_date + pd.DateOffset(months=MONTHS[horizon])).date().isoformat()


def load_history_table() -> pd.DataFrame:
    if not HISTORY.exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(HISTORY)
    for c in COLUMNS:
        if c not in df.columns:
            df[c] = pd.NA
    return df[COLUMNS]


def evaluate_pending(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()
    for i, row in out.iterrows():
        if row["status"] == "evaluated":
            continue
        try:
            prices = load_history(row["symbol"])
            target = pd.Timestamp(row["target_date"])
            candidates = prices.loc[prices.index >= target, "Close"]
            if candidates.empty:
                continue
            actual_price = float(candidates.iloc[0])
            actual_return = actual_price / float(row["current_price"]) - 1
            error = actual_return - float(row["predicted_return"])
            out.at[i, "actual_price"] = actual_price
            out.at[i, "actual_return"] = actual_return
            out.at[i, "error"] = error
            out.at[i, "abs_error"] = abs(error)
            out.at[i, "status"] = "evaluated"
        except Exception:
            continue
    return out


def append_forecasts(forecast_rows: list[dict], forecast_date: pd.Timestamp) -> pd.DataFrame:
    history = evaluate_pending(load_history_table())
    existing_keys = set(
        zip(
            history.get("forecast_date", pd.Series(dtype=str)).astype(str),
            history.get("symbol", pd.Series(dtype=str)).astype(str),
            history.get("horizon", pd.Series(dtype=str)).astype(str),
        )
    )

    new_rows = []
    date_str = forecast_date.date().isoformat()
    for row in forecast_rows:
        for horizon in HORIZONS:
            key = (date_str, str(row["symbol"]), horizon)
            if key in existing_keys:
                continue
            new_rows.append({
                "forecast_date": date_str,
                "target_date": _target_date(forecast_date, horizon),
                "symbol": row["symbol"],
                "name": row["name"],
                "horizon": horizon,
                "current_price": row["current_price"],
                "predicted_price": row[f"{horizon}_predicted_price"],
                "predicted_return": row[f"{horizon}_expected_return"],
                "lower_price": row[f"{horizon}_lower_price"],
                "upper_price": row[f"{horizon}_upper_price"],
                "actual_price": pd.NA,
                "actual_return": pd.NA,
                "error": pd.NA,
                "abs_error": pd.NA,
                "status": "pending",
            })

    if new_rows:
        history = pd.concat([history, pd.DataFrame(new_rows)], ignore_index=True)

    history = history[COLUMNS]
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    history.to_csv(HISTORY, index=False)
    return history
