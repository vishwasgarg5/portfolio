import pandas as pd
from src.strategy_backtest import _simulate_plan

def test_strategy_simulation_requires_all_entries_before_exit():
    idx = pd.date_range("2024-01-01", periods=5, freq="B")
    prices = pd.DataFrame({
        "Low": [100, 95, 90, 85, 80],
        "High": [101, 96, 91, 86, 120],
    }, index=idx)
    plan = {
        "rows": [
            {"buy_price": 95, "capital": 95, "cumulative_average": 95},
            {"buy_price": 85, "capital": 85, "cumulative_average": 90},
        ],
        "forecast_exit_price": 120,
        "final_average": 90,
    }
    result = _simulate_plan(prices, idx[0], plan)
    assert result["all_entries_reached"] is True
    assert result["exit_reached"] is True
    assert result["profit_percent"] == 120/90-1
