from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

from .model import _model


def walk_forward_backtest(
    features: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
    min_train_rows: int = 80,
    max_folds: int = 20,
    step: int = 21,
) -> pd.DataFrame:
    """Evaluate historical one-step-origin forecasts without random shuffling.

    Each fold trains only on observations available before the forecast origin,
    then predicts that origin's already-known forward return target.
    """
    clean = features.dropna(subset=feature_columns + [target_column]).copy()
    if len(clean) <= min_train_rows:
        return pd.DataFrame(
            columns=["forecast_date", "target_return", "predicted_return", "error", "abs_error"]
        )

    origins = list(range(min_train_rows, len(clean), max(1, step)))
    origins = origins[-max_folds:]
    rows: list[dict] = []

    for origin in origins:
        train = clean.iloc[:origin]
        test = clean.iloc[[origin]]
        model = _model()
        model.fit(train[feature_columns], train[target_column])
        predicted = float(model.predict(test[feature_columns])[0])
        actual = float(test[target_column].iloc[0])
        error = actual - predicted
        rows.append(
            {
                "forecast_date": clean.index[origin].date().isoformat(),
                "target_return": actual,
                "predicted_return": predicted,
                "error": error,
                "abs_error": abs(error),
            }
        )

    return pd.DataFrame(rows)


def summarize_backtest(results: pd.DataFrame) -> dict[str, float | int]:
    if results.empty:
        return {
            "folds": 0,
            "mean_abs_error": np.nan,
            "mean_error": np.nan,
            "direction_accuracy": np.nan,
        }

    actual = results["target_return"]
    predicted = results["predicted_return"]
    return {
        "folds": int(len(results)),
        "mean_abs_error": float(results["abs_error"].mean()),
        "mean_error": float(results["error"].mean()),
        "direction_accuracy": float((np.sign(actual) == np.sign(predicted)).mean()),
        "price_return_mae": float(mean_absolute_error(actual, predicted)),
    }
