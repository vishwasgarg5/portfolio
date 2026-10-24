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

def test_rsi_handles_zero_loss_and_flat_windows():
    from src.features import _rsi
    idx=pd.date_range("2024-01-01",periods=40,freq="B")
    rising=pd.Series(np.arange(100.0,140.0),index=idx)
    flat=pd.Series(100.0,index=idx)
    assert _rsi(rising).dropna().eq(100.0).all()
    assert _rsi(flat).dropna().eq(50.0).all()
