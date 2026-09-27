from __future__ import annotations
from pathlib import Path
import math
import numpy as np
import pandas as pd
from .averaging import build_staged_averaging_plan
from .features import FEATURE_COLUMNS, HORIZONS, make_features
from .model import fit_forecast

STOP_LOSS_PCT = 0.15
DETERIORATION_DAYS = 3
MAX_HOLD_MULTIPLIER = 1.50
MIN_HOLD_DAYS = 60

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "predictions" / "strategy_backtest.csv"


def _simulate_plan(prices, plan_date, plan):
    """V5 out-of-sample simulation: next-day entries, partial fills, risk exits and timeout."""
    if plan is None:
        return None
    prices = prices.sort_index()
    future = prices.loc[prices.index > pd.Timestamp(plan_date)].copy()
    rows = plan["rows"]
    horizon_days = HORIZONS.get(plan.get("horizon"), 252)
    max_holding_days = max(MIN_HOLD_DAYS, int(horizon_days * MAX_HOLD_MULTIPLIER))
    if future.empty:
        return {"all_entries_reached": False, "exit_reached": False,
                "partial_exit_reached": False, "exit_type": "no_future_data",
                "exit_date": "", "actual_exit_price": np.nan,
                "profit_percent": np.nan, "partial_profit_percent": np.nan,
                "capital_deployed": 0.0, "entries_reached": 0, "max_holding_days": np.nan}

    reached = []
    for r in rows:
        hits = future.index[future["Low"] <= float(r["buy_price"])]
        reached.append(hits[0] if len(hits) else None)

    existing_qty = float(plan["existing_qty"])
    existing_avg = float(plan["existing_avg"])
    reached_count = 0
    capital_deployed = 0.0
    cumulative_qty = 0.0
    cumulative_capital = 0.0
    filled_flags = [False] * len(rows)
    deterioration_streak = 0
    ma20 = prices["Close"].rolling(20, min_periods=20).mean()
    ma50 = prices["Close"].rolling(50, min_periods=50).mean()

    for date, bar in future.iterrows():
        days = (pd.Timestamp(date) - pd.Timestamp(plan_date)).days
        if days > max_holding_days:
            break

        for i, hit_date in enumerate(reached):
            if hit_date is not None and hit_date <= date and not filled_flags[i]:
                filled_flags[i] = True
                cumulative_qty += float(rows[i]["additional_quantity"])
                cumulative_capital += float(rows[i]["capital"])
        reached_count = sum(filled_flags)
        capital_deployed = cumulative_capital

        if reached_count == 0:
            continue

        avg = (existing_qty * existing_avg + cumulative_capital) / (existing_qty + cumulative_qty)
        close = float(bar["Close"])
        if pd.notna(ma20.get(date)) and pd.notna(ma50.get(date)) and close < float(ma20.get(date)) and float(ma20.get(date)) < float(ma50.get(date)):
            deterioration_streak += 1
        else:
            deterioration_streak = 0

        stop_price = avg * (1.0 - STOP_LOSS_PCT)
        target_price = float(plan["forecast_exit_price"])

        if float(bar["Low"]) <= stop_price:
            profit = stop_price / avg - 1.0
            return {"all_entries_reached": reached_count == len(rows), "exit_reached": False,
                    "partial_exit_reached": True, "exit_type": "stop_loss",
                    "exit_date": date.date().isoformat(), "actual_exit_price": stop_price,
                    "profit_percent": profit if reached_count == len(rows) else np.nan,
                    "partial_profit_percent": profit, "capital_deployed": capital_deployed,
                    "entries_reached": reached_count, "max_holding_days": days}

        if deterioration_streak >= DETERIORATION_DAYS:
            profit = close / avg - 1.0
            return {"all_entries_reached": reached_count == len(rows), "exit_reached": False,
                    "partial_exit_reached": True, "exit_type": "deterioration",
                    "exit_date": date.date().isoformat(), "actual_exit_price": close,
                    "profit_percent": profit if reached_count == len(rows) else np.nan,
                    "partial_profit_percent": profit, "capital_deployed": capital_deployed,
                    "entries_reached": reached_count, "max_holding_days": days}

        if float(bar["High"]) >= target_price:
            profit = target_price / avg - 1.0
            return {"all_entries_reached": reached_count == len(rows), "exit_reached": True,
                    "partial_exit_reached": True, "exit_type": "target",
                    "exit_date": date.date().isoformat(), "actual_exit_price": target_price,
                    "profit_percent": profit if reached_count == len(rows) else np.nan,
                    "partial_profit_percent": profit, "capital_deployed": capital_deployed,
                    "entries_reached": reached_count, "max_holding_days": days}

    full = reached_count == len(rows)
    return {"all_entries_reached": full, "exit_reached": False,
            "partial_exit_reached": reached_count > 0,
            "exit_type": "timeout" if reached_count > 0 else "no_entry",
            "exit_date": "", "actual_exit_price": np.nan,
            "profit_percent": np.nan, "partial_profit_percent": np.nan,
            "capital_deployed": capital_deployed, "entries_reached": reached_count,
            "max_holding_days": max_holding_days if reached_count > 0 else np.nan}


def run_strategy_backtest(prices, symbol, name, shares, purchase_price,
                          max_folds=8, step=63):
    if prices.empty or len(prices) < 260:
        return []
    prices = prices.sort_index()
    features = make_features(prices)
    usable = features.dropna(subset=FEATURE_COLUMNS)
    if len(usable) < 260:
        return []

    # An origin only needs enough labelled history for the selected horizon;
    # it does not need the horizon's target to exist after the origin.
    start_origin = min(200, max(150, len(usable) - MIN_HOLD_DAYS - max(21, step)))
    origins = list(
        range(start_origin, len(usable) - MIN_HOLD_DAYS, max(21, step))
    )[-max_folds:]
    results = []
    diagnostics = {"origins": len(origins), "forecast_successes": 0,
                   "no_forecast": 0, "plans": 0, "no_plan": 0, "fit_errors": 0}

    for origin in origins:
        date = usable.index[origin]
        current = float(prices.loc[date, "Close"])
        if not math.isfinite(current) or current <= 0:
            continue

        forecasts, lowers = {}, {}
        for h, days in HORIZONS.items():
            # fit_forecast needs at least 80 labelled rows. At an origin,
            # target_h is labelled only for rows at least days before origin.
            labelled_rows = origin + 1 - days
            if labelled_rows < 80:
                continue
            train_slice = usable.iloc[:origin + 1].copy()
            try:
                result = fit_forecast(
                    train_slice, FEATURE_COLUMNS, f"target_{h}"
                )
            except Exception:
                diagnostics["fit_errors"] += 1
                continue
            forecasts[h] = float(result.predicted_price)
            lowers[h] = max(
                0.01, current * (1.0 + result.lower_return)
            )

        if not forecasts:
            diagnostics["no_forecast"] += 1
            continue

        diagnostics["forecast_successes"] += 1

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
            diagnostics["no_plan"] += 1
            results.append({
                "symbol": symbol, "name": name,
                "plan_date": date.date().isoformat(),
                "decision": "no_plan", "horizon": "",
                "forecast_exit_price": np.nan, "final_average": np.nan,
                "capital_deployed": 0.0,
                "all_entries_reached": False, "exit_reached": False,
                "exit_date": "", "actual_exit_price": np.nan,
                "profit_percent": np.nan, "partial_profit_percent": np.nan,
                "partial_exit_reached": False, "exit_type": "no_plan",
                "entries_reached": 0, "max_holding_days": np.nan,
            })
            continue

        diagnostics["plans"] += 1
        plan["existing_qty"] = shares
        plan["existing_avg"] = purchase_price
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
            "partial_profit_percent": sim["partial_profit_percent"],
            "partial_exit_reached": sim["partial_exit_reached"],
            "exit_type": sim["exit_type"],
            "entries_reached": sim["entries_reached"],
            "max_holding_days": sim["max_holding_days"],
        })
    print(f"Backtest {symbol}: {diagnostics}, rows={len(results)}")
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
