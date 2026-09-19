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
    training_samples: int
    confidence: str

def _model():
    return HistGradientBoostingRegressor(
        learning_rate=0.05,max_iter=350,max_leaf_nodes=15,
        l2_regularization=1.0,random_state=42,
    )

def _minimum_rows(target_column: str) -> int:
    return 80

def fit_forecast(features, feature_columns, target_column, min_rows=None):
    required=min_rows if min_rows is not None else _minimum_rows(target_column)
    clean=features.dropna(subset=feature_columns+[target_column]).copy()
    if len(clean)<required:
        raise ValueError(f"Insufficient history for {target_column}: {len(clean)} labelled rows < {required}")
    test_size=max(20,int(len(clean)*0.20))
    if len(clean)-test_size<60:
        test_size=max(10,len(clean)-60)
    split=len(clean)-test_size
    train,test=clean.iloc[:split],clean.iloc[split:]
    model=_model()
    model.fit(train[feature_columns],train[target_column])
    test_pred=model.predict(test[feature_columns])
    mae=float(mean_absolute_error(test[target_column],test_pred))
    final_model=_model()
    final_model.fit(clean[feature_columns],clean[target_column])
    latest=features.dropna(subset=feature_columns).iloc[-1]
    pred=float(final_model.predict(latest[feature_columns].to_frame().T)[0])
    residuals=test[target_column].to_numpy()-test_pred
    sigma=float(np.std(residuals,ddof=1)) if len(residuals)>1 else mae
    sigma=max(sigma,mae*0.5,0.01)
    lower=pred-1.28*sigma
    upper=pred+1.28*sigma
    price=float(latest["Close"])
    confidence="high" if len(clean)>=500 else "medium" if len(clean)>=200 else "low"
    return ForecastResult(
        predicted_return=pred,
        predicted_price=price*(1+pred),
        lower_return=lower,
        upper_return=upper,
        validation_mae=mae,
        validation_samples=len(test),
        training_samples=len(clean),
        confidence=confidence,
    )
