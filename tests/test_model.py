import numpy as np
import pandas as pd

from src.features import FEATURE_COLUMNS, make_features
from src.model import fit_forecast


def _prices(n: int) -> pd.DataFrame:
    idx = pd.date_range("2020-01-01", periods=n, freq="B")
    close = pd.Series(100 + np.cumsum(np.sin(np.arange(n) / 8) + 0.2), index=idx)
    return pd.DataFrame(
        {
            "Open": close * 0.99,
            "High": close * 1.01,
            "Low": close * 0.98,
            "Close": close,
            "Volume": 100000,
        },
        index=idx,
    )


def test_shorter_history_can_train_when_enough_labelled_rows_exist():
    features = make_features(_prices(260))
    result = fit_forecast(features, FEATURE_COLUMNS, "target_3M")
    assert result.training_samples >= 100
    assert result.validation_samples >= 10
    assert result.confidence == "low"


def test_long_horizon_rejects_history_without_enough_labels():
    features = make_features(_prices(220))
    try:
        fit_forecast(features, FEATURE_COLUMNS, "target_12M")
    except ValueError as exc:
        assert "Insufficient history" in str(exc)
    else:
        raise AssertionError("Expected insufficient-history error")
