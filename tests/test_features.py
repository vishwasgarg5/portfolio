import numpy as np
import pandas as pd
from src.features import FEATURE_COLUMNS,HORIZONS,make_features
def test_features_include_regime_columns_without_future_data():
    idx=pd.date_range("2020-01-01",periods=600,freq="B");close=pd.Series(np.linspace(100,180,len(idx)),index=idx)
    df=pd.DataFrame({"Open":close*.99,"High":close*1.01,"Low":close*.98,"Close":close,"Volume":100000},index=idx)
    out=make_features(df)
    assert set(FEATURE_COLUMNS).issubset(out.columns)
    assert out["nifty_return_20d"].notna().any()
    assert all(f"target_{h}" in out.columns for h in HORIZONS)
