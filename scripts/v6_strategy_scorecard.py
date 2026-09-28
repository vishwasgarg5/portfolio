from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "predictions" / "strategy_backtest.csv"
OUT_CSV = ROOT / "predictions" / "v6_strategy_scorecard.csv"
OUT_MD = ROOT / "predictions" / "v6_strategy_scorecard.md"

def pct(x):
    return f"{x*100:.2f}%" if pd.notna(x) else "n/a"

def summarize(df, scope):
    plans = df[df.decision == "plan"].copy()
    outcomes = pd.to_numeric(plans.partial_profit_percent, errors="coerce")
    capital = pd.to_numeric(plans.capital_deployed, errors="coerce")
    holding = pd.to_numeric(plans.max_holding_days, errors="coerce")
    losses = outcomes[outcomes < 0]
    total = len(df)
    return {
        "scope": scope, "plan_rows": len(plans),
        "positive_rate": (outcomes > 0).mean() if len(outcomes) else None,
        "negative_rate": (outcomes < 0).mean() if len(outcomes) else None,
        "mean_outcome": outcomes.mean() if len(outcomes) else None,
        "median_outcome": outcomes.median() if len(outcomes) else None,
        "worst_outcome": outcomes.min() if len(outcomes) else None,
        "mean_loss": losses.mean() if len(losses) else None,
        "target_rate": (plans.exit_type == "target").mean() if len(plans) else None,
        "deterioration_rate": (plans.exit_type == "deterioration").mean() if len(plans) else None,
        "stop_loss_rate": (plans.exit_type == "stop_loss").mean() if len(plans) else None,
        "full_entry_rate": plans.all_entries_reached.astype(bool).mean() if len(plans) else None,
        "mean_capital": capital.mean() if len(capital) else None,
        "median_capital": capital.median() if len(capital) else None,
        "mean_days": holding.mean() if len(holding) else None,
        "median_days": holding.median() if len(holding) else None,
        "trend_block_rate": (df.decision == "trend_blocked").mean() if total else None,
        "no_plan_rate": (df.decision == "no_plan").mean() if total else None,
    }

def main():
    if not INPUT.exists():
        raise SystemExit("strategy_backtest.csv missing")
    df = pd.read_csv(INPUT)
    required = {"version","symbol","decision","horizon","exit_type","partial_profit_percent",
                "capital_deployed","all_entries_reached","max_holding_days"}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    if df.empty or not df.version.eq("V6").all():
        raise SystemExit("Expected non-empty V6 evidence")

    rows = [summarize(df, "ALL")]
    plans = df[df.decision == "plan"]
    for key, g in plans.groupby("horizon", sort=True):
        rows.append(summarize(g, str(key)))
    for key, g in plans.groupby("symbol", sort=True):
        rows.append(summarize(g, str(key)))
    score = pd.DataFrame(rows)
    score.to_csv(OUT_CSV, index=False)

    s = rows[0]
    lines = [
        "# V6 Strategy Scorecard", "",
        f"- Evidence rows: {len(df)}",
        f"- Plan rows: {len(plans)}",
        f"- Trend-blocked: {(df.decision == 'trend_blocked').sum()}",
        f"- No-plan: {(df.decision == 'no_plan').sum()}",
        "", "## Overall",
        f"- Positive partial outcome rate: {pct(s['positive_rate'])}",
        f"- Negative partial outcome rate: {pct(s['negative_rate'])}",
        f"- Mean partial outcome: {pct(s['mean_outcome'])}",
        f"- Median partial outcome: {pct(s['median_outcome'])}",
        f"- Worst partial outcome: {pct(s['worst_outcome'])}",
        f"- Target exit rate: {pct(s['target_rate'])}",
        f"- Deterioration exit rate: {pct(s['deterioration_rate'])}",
        f"- Stop-loss rate: {pct(s['stop_loss_rate'])}",
        f"- Full-entry rate: {pct(s['full_entry_rate'])}",
        f"- Mean additional capital: ₹{s['mean_capital']:,.0f}",
        f"- Median additional capital: ₹{s['median_capital']:,.0f}",
        f"- Mean exit/holding days: {s['mean_days']:.1f}",
        f"- Median exit/holding days: {s['median_days']:.1f}",
        "", "## Horizon evidence",
        "| Horizon | Plans | Positive | Mean | Median | Target | Deterioration | Stop | Mean capital | Mean days |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    horizons = {str(x) for x in plans.horizon.dropna().unique()}
    for r in rows[1:]:
        if r["scope"] in horizons:
            lines.append(f"| {r['scope']} | {r['plan_rows']} | {pct(r['positive_rate'])} | {pct(r['mean_outcome'])} | {pct(r['median_outcome'])} | {pct(r['target_rate'])} | {pct(r['deterioration_rate'])} | {pct(r['stop_loss_rate'])} | ₹{r['mean_capital']:,.0f} | {r['mean_days']:.1f} |")
    lines += [
        "", "## Stock evidence",
        "| Stock | Plans | Positive | Mean | Worst | Target | Deterioration | Stop | Mean capital |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    symbols = {str(x) for x in plans.symbol.unique()}
    for r in rows[1:]:
        if r["scope"] in symbols:
            lines.append(f"| {r['scope']} | {r['plan_rows']} | {pct(r['positive_rate'])} | {pct(r['mean_outcome'])} | {pct(r['worst_outcome'])} | {pct(r['target_rate'])} | {pct(r['deterioration_rate'])} | {pct(r['stop_loss_rate'])} | ₹{r['mean_capital']:,.0f} |")
    lines += [
        "", "## Benchmark status",
        "- This is an evidence scorecard for the existing rolling V6 origins.",
        "- A true hold-only counterfactual is not claimed because the persisted backtest does not contain every required entry-price path.",
        "- No V6 parameter change or promotion should be based on this scorecard alone.",
        "", "## Next gate",
        "- Build a matched hold-only counterfactual using the same historical origins and price data.",
        "- Compare V6 and hold-only with identical horizon and capital accounting.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
