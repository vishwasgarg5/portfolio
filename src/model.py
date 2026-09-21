from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor, HistGradientBoostingRegressor
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
    model_name: str
    candidate_mae: dict[str, float]

def _model(name: str = "hist"):
    if name == "extra_trees":
        return ExtraTreesRegressor(
            n_estimators=300, min_samples_leaf=5, max_features=0.8,
            random_state=42, n_jobs=-1
        )
    if name == "hist":
        return HistGradientBoostingRegressor(
            learning_rate=0.05, max_iter=350, max_leaf_nodes=15,
            l2_regularization=1.0, random_state=42
        )
    raise ValueError(f"Unknown model: {name}")

MODEL_NAMES = ("hist", "extra_trees")

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

    candidate_mae={}
    candidate_predictions={}
    for name in MODEL_NAMES:
        model=_model(name)
        model.fit(train[feature_columns],train[target_column])
        pred=model.predict(test[feature_columns])
        candidate_predictions[name]=pred
        candidate_mae[name]=float(mean_absolute_error(test[target_column],pred))

    # Use a horizon-specific historical median-return baseline.
    # Unlike a zero-return baseline, this preserves differences between horizons.
    median_return=float(train[target_column].median())
    median_pred=np.full(len(test), median_return, dtype=float)
    candidate_predictions["historical_median"]=median_pred
    candidate_mae["historical_median"]=float(mean_absolute_error(test[target_column],median_pred))
    best_name=min(candidate_mae,key=candidate_mae.get)
    best_pred=candidate_predictions[best_name]
    mae=candidate_mae[best_name]

    latest=features.dropna(subset=feature_columns).iloc[-1]
    if best_name=="historical_median":
        pred=median_return
    else:
        final_model=_model(best_name)
        final_model.fit(clean[feature_columns],clean[target_column])
        pred=float(final_model.predict(latest[feature_columns].to_frame().T)[0])

    # Robust horizon-specific sanity guard.
    # Long horizons have wider return distributions, so use the distribution
    # of this horizon rather than one global cap. This preserves 3M/6M/.../36M
    # differences while preventing a few extreme historical observations from
    # producing implausible current forecasts.
    target_series=pd.to_numeric(train[target_column],errors="coerce").dropna()
    q01=float(target_series.quantile(0.01))
    q99=float(target_series.quantile(0.99))
    q25=float(target_series.quantile(0.25))
    q75=float(target_series.quantile(0.75))
    iqr=max(q75-q25,0.01)
    robust_low=float(target_series.median()-3.0*iqr)
    robust_high=float(target_series.median()+3.0*iqr)
    guard_low=max(q01,robust_low)
    guard_high=min(q99,robust_high)
    if guard_low<guard_high:
        pred=float(np.clip(pred,guard_low,guard_high))

    residuals=test[target_column].to_numpy()-best_pred
    sigma=float(np.std(residuals,ddof=1)) if len(residuals)>1 else mae
    sigma=max(sigma,mae*0.5,0.01)
    lower=pred-1.28*sigma
    upper=pred+1.28*sigma
    price=float(latest["Close"])
    confidence="high" if len(clean)>=500 else "medium" if len(clean)>=200 else "low"
    return ForecastResult(
        predicted_return=pred,predicted_price=price*(1+pred),
        lower_return=lower,upper_return=upper,validation_mae=mae,
        validation_samples=len(test),training_samples=len(clean),
        confidence=confidence,model_name=best_name,candidate_mae=candidate_mae
    )
