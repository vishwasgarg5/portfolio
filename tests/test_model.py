import numpy as np
import pandas as pd
from src.features import FEATURE_COLUMNS,make_features
from src.model import fit_forecast
def _prices(n=260):
    idx=pd.date_range("2020-01-01",periods=n,freq="B");close=pd.Series(100+np.cumsum(np.sin(np.arange(n)/8)+0.2),index=idx)
    return pd.DataFrame({"Open":close*.99,"High":close*1.01,"Low":close*.98,"Close":close,"Volume":100000},index=idx)
def test_model_selects_from_candidates():
    result=fit_forecast(make_features(_prices()),FEATURE_COLUMNS,"target_3M")
    assert result.model_name in {"hist","extra_trees","zero_baseline"}
    assert set(result.candidate_mae)=={"hist","extra_trees","zero_baseline"}
def test_long_horizon_rejects_insufficient_history():
    try: fit_forecast(make_features(_prices(220)),FEATURE_COLUMNS,"target_12M")
    except ValueError as exc: assert "Insufficient history" in str(exc)
    else: raise AssertionError("Expected insufficient history")
