from __future__ import annotations
import math

def new_average(existing_qty: float, existing_avg: float, add_qty: float, add_price: float) -> float:
    if min(existing_qty, existing_avg, add_qty, add_price) < 0:
        raise ValueError("quantities and prices must be non-negative")
    total = existing_qty + add_qty
    return 0.0 if total == 0 else (existing_qty * existing_avg + add_qty * add_price) / total

def quantity_for_target_average(existing_qty, existing_avg, buy_price, target_avg):
    if existing_qty <= 0 or target_avg <= 0 or buy_price >= target_avg:
        return None
    return max(0.0, existing_qty * (existing_avg - target_avg) / (target_avg - buy_price))

def averaging_scenarios(existing_qty, existing_avg, buy_price, target_fractions=(0.95, 0.90, 0.85)):
    if not all(math.isfinite(float(x)) for x in (existing_qty, existing_avg, buy_price)):
        return []
    out = []
    for f in target_fractions:
        target = existing_avg * f
        qty = quantity_for_target_average(existing_qty, existing_avg, buy_price, target)
        out.append({
            "target_average": target,
            "buy_price": buy_price,
            "additional_quantity": qty,
            "additional_capital": None if qty is None else qty * buy_price,
        })
    return out

def _clean_levels(current_price: float, volatility: float | None = None):
    """Return conditional buy levels using volatility-aware spacing.
    Levels remain bounded so the plan cannot suggest extreme orders from a noisy
    volatility estimate. The first level is always the current-price trigger.
    """
    if volatility is None or not math.isfinite(float(volatility)):
        volatility = 0.04
    step = min(max(float(volatility), 0.03), 0.10)
    return (0.0, -step, -2*step, -3*step, -4*step, -5*step)

def build_staged_averaging_plan(
    existing_qty,
    existing_avg,
    current_price,
    forecasts,
    profit_target=0.05,
    max_add_capital_ratio=0.50,
    levels=None,
    volatility=None,
    lower_forecasts=None,
):
    """Build a conditional multi-entry averaging plan.

    Entries are spaced from current price using recent volatility when supplied.
    The plan is accepted only if the conservative forecast (lower forecast bound,
    when supplied) still leaves the combined position at least profit_target
    above its final average. Whole shares are used and capital is capped.
    """
    if existing_qty <= 0 or existing_avg <= 0 or current_price <= 0:
        return None
    clean = [(h, float(p)) for h, p in forecasts.items()
             if p is not None and math.isfinite(float(p)) and float(p) > 0]
    if not clean:
        return None

    levels = tuple(levels) if levels is not None else _clean_levels(current_price, volatility)
    lower_forecasts = lower_forecasts or {}
    max_capital = existing_qty * existing_avg * max_add_capital_ratio
    best = None
    horizon_order = list(forecasts.keys())

    for h, forecast in clean:
        conservative_exit = float(lower_forecasts.get(h, forecast))
        if conservative_exit <= current_price:
            continue
        for n in range(2, len(levels) + 1):
            chosen = levels[:n]
            tranche_budget = max_capital / n
            total_qty = 0
            total_capital = 0.0
            rows = []
            for idx, level in enumerate(chosen, 1):
                buy = current_price * (1.0 + level)
                if buy <= 0:
                    continue
                add_qty = math.floor(tranche_budget / buy)
                if add_qty < 1:
                    continue
                capital = add_qty * buy
                total_qty += add_qty
                total_capital += capital
                avg = (
                    existing_qty * existing_avg
                    + sum(r["capital"] for r in rows)
                    + capital
                ) / (existing_qty + total_qty)
                rows.append({
                    "entry": idx,
                    "buy_price": buy,
                    "additional_quantity": add_qty,
                    "capital": capital,
                    "cumulative_quantity": total_qty,
                    "cumulative_average": avg,
                    "level": level,
                })
            if len(rows) < 2 or total_qty <= 0 or total_capital > max_capital + 1e-9:
                continue

            final_avg = rows[-1]["cumulative_average"]
            conservative_profit = conservative_exit / final_avg - 1.0
            if conservative_profit < profit_target:
                continue

            candidate = {
                "horizon": h,
                "forecast_exit_price": forecast,
                "conservative_exit_price": conservative_exit,
                "forecast_profit_percent": forecast / final_avg - 1.0,
                "conservative_profit_percent": conservative_profit,
                "total_additional_quantity": total_qty,
                "total_capital": total_capital,
                "final_average": final_avg,
                "rows": rows,
            }
            rank = (horizon_order.index(h), n, total_capital)
            if best is None or rank < best["_rank"]:
                candidate["_rank"] = rank
                best = candidate

    if best is not None:
        best.pop("_rank", None)
    return best
