import pandas as pd
from src.strategy_backtest import _adaptive_target, _simulate_plan

def test_adaptive_target():
    assert _adaptive_target(100, 140) == 120
    assert _adaptive_target(100, 103) == 105

def test_v6_requires_all_entries_before_full_profit():
    idx=pd.date_range("2024-01-01",periods=6,freq="B")
    prices=pd.DataFrame({
        "Close":[100,94,90,86,100,120],
        "Low":[99,93,89,85,99,119],
        "High":[101,95,91,87,101,121],
    },index=idx)
    plan={"rows":[
        {"buy_price":95,"capital":95,"additional_quantity":1},
        {"buy_price":85,"capital":85,"additional_quantity":1}],
        "forecast_exit_price":120,"final_average":90,"horizon":"3M",
        "existing_qty":2,"existing_avg":100}
    result=_simulate_plan(prices,idx[0],plan)
    assert result["all_entries_reached"] is True
    assert result["exit_reached"] is True
    assert result["actual_exit_price"] == 105

def test_partial_entry_does_not_count_as_full_entry():
    idx=pd.date_range("2024-01-01",periods=5,freq="B")
    prices=pd.DataFrame({
        "Close":[100,94,94,94,94],
        "Low":[99,93,93,93,93],
        "High":[101,95,95,95,95],
    },index=idx)
    plan={"rows":[
        {"buy_price":95,"capital":95,"additional_quantity":1},
        {"buy_price":80,"capital":80,"additional_quantity":1}],
        "forecast_exit_price":120,"final_average":90,"horizon":"3M",
        "existing_qty":2,"existing_avg":100}
    result=_simulate_plan(prices,idx[0],plan)
    assert result["entries_reached"] == 1
    assert result["all_entries_reached"] is False
