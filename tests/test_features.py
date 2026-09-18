import pandas as pd
import numpy as np

from src.features import FEATURE_COLUMNS, HORIZONS, make_features


def test_features_are_created_without_future_feature_columns():
    idx = pd.date_range("2020-01-01", periods=600, freq="B")
    close = pd.Series(np.linspace(100, 180, len(idx)), index=idx)
    df = pd.DataFrame({
        "Open": close * 0.99,
        "High": close * 1.01,
        "Low": close * 0.98,
        "Close": close,
        "Volume": 100000,
    }, index=idx)

    out = make_features(df)

    assert set(FEATURE_COLUMNS).issubset(out.columns)
    assert all(f"target_{h}" in out.columns for h in HORIZONS)
