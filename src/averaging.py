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

def build_staged_averaging_plan(
    existing_qty,
    existing_avg,
    current_price,
    forecasts,
    profit_target=0.05,
    max_add_capital_ratio=0.50,
    levels=(0.0, -0.05, -0.10, -0.15, -0.20, -0.25, -0.30),
):
    """Build a conditional multi-entry averaging plan.

    Each level is a separate conditional buy trigger. Capital is split equally
    across the selected levels and whole shares are used. A plan qualifies only
    when its cumulative average is at least profit_target below an available
    forecast exit, within the configured additional-capital budget.
    """
    if existing_qty <= 0 or existing_avg <= 0 or current_price <= 0:
        return None
    clean = [(h, float(p)) for h, p in forecasts.items()
             if p is not None and math.isfinite(float(p)) and float(p) > 0]
    if not clean:
        return None

    max_capital = existing_qty * existing_avg * max_add_capital_ratio
    best = None

    # Require at least two conditional entries to make this a staged plan.
    for h, forecast in clean:
        if forecast <= current_price:
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
                avg = new_average(existing_qty, existing_avg, total_qty, 0) if False else (
                    existing_qty * existing_avg + sum(r["capital"] for r in rows) + capital
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
            expected_profit = forecast / final_avg - 1.0
            if expected_profit < profit_target:
                continue
            candidate = {
                "horizon": h,
                "forecast_exit_price": forecast,
                "forecast_profit_percent": expected_profit,
                "total_additional_quantity": total_qty,
                "total_capital": total_capital,
                "final_average": final_avg,
                "rows": rows,
            }
            # Prefer earliest qualifying horizon, then fewer entries, then less capital.
            rank = (list(forecasts.keys()).index(h), n, total_capital)
            if best is None or rank < best["_rank"]:
                candidate["_rank"] = rank
                best = candidate
    if best is not None:
        best.pop("_rank", None)
    return best
