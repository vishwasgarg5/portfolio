from __future__ import annotations
import numpy as np
import pandas as pd

def calibrate_return(raw_return: float, backtest_results: pd.DataFrame,
                     historical_errors=None, shrinkage: float=0.5,
                     max_adjustment: float=0.15) -> tuple[float,float,int]:
    """Conservative bias correction.

    Completed real forecast errors for the same stock/horizon are preferred.
    Walk-forward errors are the fallback when too few completed forecasts exist.
    """
    source=historical_errors if historical_errors is not None else []
    errors=pd.to_numeric(pd.Series(source),errors="coerce").dropna()
    if len(errors)<3:
        errors=pd.to_numeric(backtest_results.get("error",pd.Series(dtype=float)),errors="coerce").dropna()
    if len(errors)<3:
        return float(raw_return),0.0,int(len(errors))
    bias=float(errors.median())
    adjustment=float(np.clip(shrinkage*bias,-max_adjustment,max_adjustment))
    return float(raw_return+adjustment),adjustment,int(len(errors))

def empirical_error_band(backtest_results: pd.DataFrame, fallback_sigma: float,
                         quantile: float=0.80) -> float:
    if not backtest_results.empty and "abs_error" in backtest_results:
        errors=pd.to_numeric(backtest_results["abs_error"],errors="coerce").dropna()
        if len(errors)>=5:
            return max(float(errors.quantile(quantile)),0.01)
    return max(float(fallback_sigma),0.01)
