from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "predictions" / "strategy_backtest.csv"
OUTPUT = ROOT / "predictions" / "strategy_backtest_report.md"


def main():
    lines = ["# V5 Historical Strategy Backtest", ""]
    if not INPUT.exists() or INPUT.stat().st_size == 0:
        lines.append("- Status: no backtest file/rows yet.")
        OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    try:
        df = pd.read_csv(INPUT)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame()

    lines.append(f"- Rows: {len(df)}")
    if df.empty:
        lines.append("- Status: no usable backtest rows yet.")
        OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    if "decision" not in df.columns:
        lines.append("- Status: invalid backtest schema (missing decision column).")
        OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    plan = df[df["decision"].eq("plan")].copy()
    no_plan = int(df["decision"].eq("no_plan").sum())
    errors = int(df["decision"].astype(str).str.startswith("error:").sum())
    lines.append(f"- Plan rows: {len(plan)}")
    lines.append(f"- No-plan rows: {no_plan}")
    lines.append(f"- Error rows: {errors}")

    if len(plan):
        for col, label in [
            ("exit_reached", "Target exit rate"),
            ("all_entries_reached", "Full-entry rate"),
            ("partial_exit_reached", "Partial-exit rate"),
        ]:
            if col in plan:
                lines.append(f"- {label}: {plan[col].fillna(False).astype(bool).mean():.1%}")

        if "exit_type" in plan:
            counts = plan["exit_type"].fillna("unknown").value_counts()
            lines.extend(["", "## Exit types"])
            for name, count in counts.items():
                lines.append(f"- {name}: {int(count)} ({count/len(plan):.1%})")

        if "partial_profit_percent" in plan:
            numeric = pd.to_numeric(plan["partial_profit_percent"], errors="coerce").dropna()
            if len(numeric):
                lines.extend(["", "## Partial-position outcome"])
                lines.append(f"- Mean: {numeric.mean():.2%}")
                lines.append(f"- Median: {numeric.median():.2%}")

        if "capital_deployed" in plan:
            deployed = pd.to_numeric(plan["capital_deployed"], errors="coerce").dropna()
            if len(deployed):
                lines.append(f"- Mean additional capital deployed: ₹{deployed.mean():,.0f}")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
