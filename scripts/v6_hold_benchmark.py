from pathlib import Path
import sys
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "predictions" / "strategy_backtest.csv"
OUT_CSV = ROOT / "predictions" / "v6_hold_benchmark.csv"
OUT_MD = ROOT / "predictions" / "v6_hold_benchmark.md"

def main():
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from src.data import load_history
    if not INPUT.exists():
        raise SystemExit("strategy_backtest.csv missing")
    df = pd.read_csv(INPUT)
    stocks = pd.read_csv(ROOT / "config" / "stocks.csv").set_index("symbol")
    plans = df[(df.decision == "plan") & df.partial_exit_reached.astype(bool)].copy()
    rows = []
    for _, r in plans.iterrows():
        symbol = str(r.symbol)
        if symbol not in stocks.index:
            continue
        prices = load_history(symbol).sort_index()
        plan_date = pd.Timestamp(r.plan_date)
        exit_date = pd.Timestamp(r.exit_date)
        future = prices.loc[prices.index >= plan_date]
        if future.empty:
            continue
        entry_date = future.index[0]
        exit_candidates = prices.index[prices.index >= exit_date]
        if len(exit_candidates) == 0:
            continue
        actual_date = exit_candidates[0]
        entry_close = float(prices.loc[entry_date, "Close"])
        exit_close = float(prices.loc[actual_date, "Close"])
        hold_return = exit_close / entry_close - 1.0
        shares = float(stocks.loc[symbol, "shares"])
        purchase_price = float(stocks.loc[symbol, "purchase_price"])
        existing_value = shares * purchase_price
        deployed = float(r.capital_deployed)
        strategy_base = existing_value + deployed
        strategy_return = float(r.partial_profit_percent)
        strategy_profit = strategy_base * strategy_return
        hold_profit = existing_value * hold_return
        rows.append({
            "version": r.version, "symbol": symbol, "plan_date": r.plan_date,
            "exit_date": r.exit_date, "horizon": r.horizon,
            "exit_type": r.exit_type, "entries_reached": r.entries_reached,
            "capital_deployed": deployed, "existing_value": existing_value,
            "strategy_return": strategy_return, "hold_return": hold_return,
            "strategy_profit": strategy_profit, "hold_profit": hold_profit,
            "incremental_profit_vs_hold": strategy_profit - hold_profit,
            "entry_close": entry_close, "exit_close": exit_close
        })
    out = pd.DataFrame(rows)
    if out.empty:
        raise SystemExit("No matched V6 exits for benchmark")
    out.to_csv(OUT_CSV, index=False)

    def stats(g):
        return {
            "n": len(g),
            "strategy_positive": (g.strategy_return > 0).mean(),
            "hold_positive": (g.hold_return > 0).mean(),
            "mean_strategy": g.strategy_return.mean(),
            "mean_hold": g.hold_return.mean(),
            "median_strategy": g.strategy_return.median(),
            "median_hold": g.hold_return.median(),
            "strategy_minus_hold": (g.strategy_return - g.hold_return).mean(),
            "profit_delta": g.incremental_profit_vs_hold.mean(),
        }
    all_s = stats(out)
    lines = [
        "# V6 Matched Hold-Only Benchmark",
        "",
        f"- Matched V6 plan exits: {len(out)}",
        "- Hold-only entry uses the market close on the V6 plan date.",
        "- Hold-only exit uses the market close on the same V6 strategy exit date.",
        "- V6 return is the persisted V6 partial-position outcome.",
        "- This is a matched counterfactual for evaluation; it does not use future information to construct the V6 decision.",
        "",
        "## Overall",
        f"- V6 positive outcome rate: {all_s['strategy_positive']:.1%}",
        f"- Hold-only positive outcome rate: {all_s['hold_positive']:.1%}",
        f"- V6 mean return: {all_s['mean_strategy']:.2%}",
        f"- Hold-only mean return: {all_s['mean_hold']:.2%}",
        f"- V6 median return: {all_s['median_strategy']:.2%}",
        f"- Hold-only median return: {all_s['median_hold']:.2%}",
        f"- Mean V6 return minus hold-only return: {all_s['strategy_minus_hold']:.2%}",
        f"- Mean incremental profit versus hold-only: ₹{all_s['profit_delta']:,.0f}",
        "",
        "## Horizon comparison",
        "| Horizon | N | V6 mean | Hold mean | Mean delta | V6 positive | Hold positive |",
        "|---|---:|---:|---:|---:|---:|---:|"
    ]
    for h, g in out.groupby("horizon", sort=True):
        s = stats(g)
        lines.append(f"| {h} | {s['n']} | {s['mean_strategy']:.2%} | {s['mean_hold']:.2%} | {s['strategy_minus_hold']:.2%} | {s['strategy_positive']:.1%} | {s['hold_positive']:.1%} |")
    lines += [
        "",
        "## Interpretation guardrail",
        "- This benchmark uses the V6 exit date to evaluate the counterfactual, so it is not a live trading rule.",
        "- It does not prove that V6 is superior; it quantifies what the existing position would have returned over the same realized exit window.",
        "- A future promotion decision should also consider drawdown, capital deployment and a separate out-of-sample control.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
