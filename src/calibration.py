from __future__ import annotations
import numpy as np
import pandas as pd

def calibrate_return(raw_return: float, backtest_results: pd.DataFrame, shrinkage: float = 0.5,
                     max_adjustment: float = 0.15) -> tuple[float, float, int]:
    """Apply a conservative bias correction learned only from historical walk-forward errors."""
    if backtest_results.empty or "error" not in backtest_results:
        return float(raw_return), 0.0, 0
    errors=pd.to_numeric(backtest_results["error"],errors="coerce").dropna()
    if len(errors)<3:
        return float(raw_return), 0.0, int(len(errors))
    bias=float(errors.median())
    adjustment=float(np.clip(shrinkage*bias,-max_adjustment,max_adjustment))
    return float(raw_return+adjustment), adjustment, int(len(errors))
