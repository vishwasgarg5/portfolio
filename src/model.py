from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error


@dataclass
class ForecastResult:
    predicted_return: float
    predicted_price: float
    lower_return: float
    upper_return: float
    validation_mae: float
    validation_samples: int


def _model() -> HistGradientBoostingRegressor:
    return HistGradientBoostingRegressor(
        learning_rate=0.05,
        max_iter=350,
        max_leaf_nodes=15,
        l2_regularization=1.0,
        random_state=42,
    )


def fit_forecast(
    features: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
    min_rows: int = 500,
) -> ForecastResult:
    clean = features.dropna(subset=feature_columns + [target_column]).copy()
    if len(clean) < min_rows:
        raise ValueError(f"Not enough observations: {len(clean)} < {min_rows}")

    split = max(int(len(clean) * 0.80), min_rows - 1)
    split = min(split, len(clean) - 1)

    train = clean.iloc[:split]
    test = clean.iloc[split:]

    model = _model()
    model.fit(train[feature_columns], train[target_column])
    test_pred = model.predict(test[feature_columns])
    mae = float(mean_absolute_error(test[target_column], test_pred))

    final_model = _model()
    final_model.fit(clean[feature_columns], clean[target_column])

    latest = features.dropna(subset=feature_columns).iloc[-1]
    pred = float(final_model.predict(latest[feature_columns].to_frame().T)[0])

    residuals = test[target_column].to_numpy() - test_pred
    sigma = float(np.std(residuals, ddof=1)) if len(residuals) > 1 else mae
    sigma = max(sigma, mae * 0.5, 0.01)

    lower = pred - 1.28 * sigma
    upper = pred + 1.28 * sigma

    price = float(latest["Close"])
    return ForecastResult(
        predicted_return=pred,
        predicted_price=price * (1 + pred),
        lower_return=lower,
        upper_return=upper,
        validation_mae=mae,
        validation_samples=len(test),
    )
