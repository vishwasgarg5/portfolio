from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "predictions" / "strategy_backtest.csv"
OUTPUT = ROOT / "predictions" / "strategy_backtest_report.md"

def main():
    if not INPUT.exists():
        OUTPUT.write_text("# Strategy Backtest Report\n\nNo backtest file found.\n", encoding="utf-8")
        return
    df = pd.read_csv(INPUT)
    lines = ["# V5 Historical Strategy Backtest", ""]
    lines.append(f"- Rows: {len(df)}")
    if df.empty:
        lines.append("- Status: no usable backtest rows yet.")
        OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    plan = df[df["decision"].eq("plan")].copy()
    lines.append(f"- Plan rows: {len(plan)}")
    lines.append(f"- No-plan rows: {int(df["decision"].eq("no_plan").sum())}")
    if len(plan):
        for col, label in [
            ("exit_reached", "Target exit rate"),
            ("all_entries_reached", "Full-entry rate"),
            ("partial_exit_reached", "Partial-exit rate"),
        ]:
            lines.append(f"- {label}: {plan[col].fillna(False).mean():.1%}")
        counts = plan["exit_type"].fillna("unknown").value_counts()
        lines.append("")
        lines.append("## Exit types")
        for name, count in counts.items():
            lines.append(f"- {name}: {int(count)} ({count/len(plan):.1%})")
        numeric = plan["partial_profit_percent"].dropna()
        if len(numeric):
            lines.append("")
            lines.append("## Partial-position outcome")
            lines.append(f"- Mean: {numeric.mean():.2%}")
            lines.append(f"- Median: {numeric.median():.2%}")
        deployed = plan["capital_deployed"].dropna()
        if len(deployed):
            lines.append(f"- Mean additional capital deployed: ₹{deployed.mean():,.0f}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
