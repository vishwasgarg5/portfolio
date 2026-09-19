from __future__ import annotations
import math

def new_average(existing_qty: float, existing_avg: float, add_qty: float, add_price: float) -> float:
    if min(existing_qty, existing_avg, add_qty, add_price) < 0:
        raise ValueError("quantities and prices must be non-negative")
    total = existing_qty + add_qty
    return 0.0 if total == 0 else (existing_qty*existing_avg + add_qty*add_price)/total

def quantity_for_target_average(existing_qty, existing_avg, buy_price, target_avg):
    if existing_qty <= 0 or target_avg <= 0 or buy_price >= target_avg:
        return None
    return max(0.0, existing_qty*(existing_avg-target_avg)/(target_avg-buy_price))

def averaging_scenarios(existing_qty, existing_avg, buy_price, target_fractions=(0.95,0.90,0.85)):
    if not all(math.isfinite(float(x)) for x in (existing_qty,existing_avg,buy_price)):
        return []
    out=[]
    for f in target_fractions:
        target=existing_avg*f
        qty=quantity_for_target_average(existing_qty,existing_avg,buy_price,target)
        out.append({"target_average":target,"buy_price":buy_price,"additional_quantity":qty,
                    "additional_capital":None if qty is None else qty*buy_price})
    return out
