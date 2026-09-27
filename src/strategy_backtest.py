from __future__ import annotations
from pathlib import Path
import math
import numpy as np
import pandas as pd
from .averaging import build_staged_averaging_plan
from .features import FEATURE_COLUMNS, HORIZONS, make_features
from .model import fit_forecast

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "predictions" / "strategy_backtest.csv"


def _simulate_plan(prices, plan_date, plan):
    """Simulate entries/exits strictly after the forecast decision date."""
    if plan is None:
        return None

    prices = prices.sort_index()
    future = prices.loc[prices.index > pd.Timestamp(plan_date)]
    rows = plan["rows"]
    if future.empty:
        return {
            "all_entries_reached": False, "exit_reached": False,
            "exit_date": "", "actual_exit_price": np.nan,
            "profit_percent": np.nan,
            "capital_deployed": 0.0, "entries_reached": 0,
            "max_holding_days": np.nan,
        }

    reached = []
    for r in rows:
        hits = future.index[future["Low"] <= float(r["buy_price"])]
        reached.append(hits[0] if len(hits) else None)

    reached_count = sum(x is not None for x in reached)
    capital_deployed = sum(
        float(rows[i]["capital"]) for i in range(reached_count)
    )

    if any(x is None for x in reached):
        return {
            "all_entries_reached": False, "exit_reached": False,
            "exit_date": "", "actual_exit_price": np.nan,
            "profit_percent": np.nan,
            "capital_deployed": capital_deployed,
            "entries_reached": reached_count,
            "max_holding_days": np.nan,
        }

    start_exit = max(reached)
    exit_window = prices.loc[prices.index >= start_exit]
    exits = exit_window.index[
        exit_window["High"] >= float(plan["forecast_exit_price"])
    ]
    if len(exits):
        exit_date = exits[0]
        profit = (
            float(plan["forecast_exit_price"])
            / float(plan["final_average"])
            - 1.0
        )
        holding_days = (
            pd.Timestamp(exit_date) - pd.Timestamp(plan_date)
        ).days
        return {
            "all_entries_reached": True, "exit_reached": True,
            "exit_date": exit_date.date().isoformat(),
            "actual_exit_price": float(plan["forecast_exit_price"]),
            "profit_percent": profit,
            "capital_deployed": capital_deployed,
            "entries_reached": len(rows),
            "max_holding_days": holding_days,
        }

    return {
        "all_entries_reached": True, "exit_reached": False,
        "exit_date": "", "actual_exit_price": np.nan,
        "profit_percent": np.nan,
        "capital_deployed": capital_deployed,
        "entries_reached": len(rows),
        "max_holding_days": np.nan,
    }


def run_strategy_backtest(prices, symbol, name, shares, purchase_price,
                          max_folds=8, step=63):
    if prices.empty or len(prices) < 260:
        return []
    prices = prices.sort_index()
    features = make_features(prices)
    usable = features.dropna(subset=FEATURE_COLUMNS)
    if len(usable) < 260:
        return []

    origins = list(
        range(200, len(usable) - 63, max(21, step))
    )[-max_folds:]
    results = []

    for origin in origins:
        date = usable.index[origin]
        current = float(prices.loc[date, "Close"])
        if not math.isfinite(current) or current <= 0:
            continue

        forecasts, lowers = {}, {}
        for h, days in HORIZONS.items():
            # Require a complete future target window from this origin.
            if origin + days >= len(usable):
                continue
            train_slice = usable.iloc[:origin + 1].copy()
            try:
                result = fit_forecast(
                    train_slice, FEATURE_COLUMNS, f"target_{h}"
                )
            except Exception:
                continue
            forecasts[h] = float(result.predicted_price)
            lowers[h] = max(
                0.01, current * (1.0 + result.lower_return)
            )

        if not forecasts:
            continue

        plan = build_staged_averaging_plan(
            shares, purchase_price, current, forecasts,
            profit_target=0.05,
            max_add_capital_ratio=0.50,
            volatility=(
                float(usable.loc[date, "volatility_20"])
                if pd.notna(usable.loc[date, "volatility_20"])
                else None
            ),
            lower_forecasts=lowers,
        )

        if plan is None:
            results.append({
                "symbol": symbol, "name": name,
                "plan_date": date.date().isoformat(),
                "decision": "no_plan", "horizon": "",
                "forecast_exit_price": np.nan, "final_average": np.nan,
                "capital_deployed": 0.0,
                "all_entries_reached": False, "exit_reached": False,
                "exit_date": "", "actual_exit_price": np.nan,
                "profit_percent": np.nan, "entries_reached": 0,
                "max_holding_days": np.nan,
            })
            continue

        sim = _simulate_plan(prices, date, plan)
        results.append({
            "symbol": symbol, "name": name,
            "plan_date": date.date().isoformat(),
            "decision": "plan",
            "horizon": plan["horizon"],
            "forecast_exit_price": plan["forecast_exit_price"],
            "final_average": plan["final_average"],
            "capital_deployed": sim["capital_deployed"],
            "all_entries_reached": sim["all_entries_reached"],
            "exit_reached": sim["exit_reached"],
            "exit_date": sim["exit_date"],
            "actual_exit_price": sim["actual_exit_price"],
            "profit_percent": sim["profit_percent"],
            "entries_reached": sim["entries_reached"],
            "max_holding_days": sim["max_holding_days"],
        })
    return results


def run():
    from .data import load_history

    stocks = pd.read_csv(ROOT / "config" / "stocks.csv")
    rows = []
    for r in stocks.to_dict("records"):
        try:
            prices = load_history(str(r["symbol"]))
            rows.extend(run_strategy_backtest(
                prices, str(r["symbol"]), str(r["name"]),
                float(r["shares"]), float(r["purchase_price"])
            ))
        except Exception as exc:
            rows.append({
                "symbol": r["symbol"], "name": r["name"],
                "decision": f"error: {exc}"
            })

    df = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    return df


if __name__ == "__main__":
    df = run()
    print(f"Strategy backtest rows: {len(df)}")
