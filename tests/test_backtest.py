import numpy as np
import pandas as pd

from src.backtest import summarize_backtest, walk_forward_backtest


def _features(n: int = 260) -> pd.DataFrame:
    idx = pd.date_range("2020-01-01", periods=n, freq="B")
    x = np.arange(n)
    feature = np.sin(x / 10)
    target = 0.05 * feature + 0.01 * np.cos(x / 7)
    return pd.DataFrame({"feature": feature, "target": target}, index=idx)


def test_walk_forward_uses_chronological_training():
    df = _features()
    result = walk_forward_backtest(df, ["feature"], "target", min_train_rows=80, max_folds=5, step=20)
    assert len(result) == 5
    assert result["forecast_date"].is_monotonic_increasing
    assert result["abs_error"].ge(0).all()


def test_backtest_summary_reports_direction_accuracy():
    result = pd.DataFrame(
        {
            "target_return": [0.1, -0.1, 0.2],
            "predicted_return": [0.05, -0.03, -0.02],
            "error": [0.05, 0.07, -0.22],
            "abs_error": [0.05, 0.07, 0.22],
        }
    )
    summary = summarize_backtest(result)
    assert summary["folds"] == 3
    assert summary["direction_accuracy"] == 2 / 3
