from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "predictions" / "strategy_backtest.csv"
OUTPUT = ROOT / "predictions" / "strategy_backtest_report.md"

def main():
    lines=["# V6 Historical Strategy Backtest",""]
    if not INPUT.exists() or INPUT.stat().st_size == 0:
        lines.append("- Status: no backtest rows yet.")
        OUTPUT.write_text("\n".join(lines)+"\n",encoding="utf-8"); return
    try: df=pd.read_csv(INPUT)
    except pd.errors.EmptyDataError: df=pd.DataFrame()
    lines.append(f"- Version: V6")
    lines.append(f"- Rows: {len(df)}")
    if df.empty:
        lines.append("- Status: no usable rows."); OUTPUT.write_text("\n".join(lines)+"\n",encoding="utf-8"); return
    plans=df[df["decision"].eq("plan")].copy()
    lines += [
        f"- Plan rows: {len(plans)}",
        f"- No-plan rows: {int(df['decision'].eq('no_plan').sum())}",
        f"- Trend-blocked rows: {int(df['decision'].eq('trend_blocked').sum())}",
        f"- Error rows: {int(df['decision'].astype(str).str.startswith('error:').sum())}",
    ]
    if plans.empty:
        lines.append("- Status: no qualifying V6 plans.")
    else:
        for col,label in [("exit_reached","Adaptive target exit rate"),("all_entries_reached","Full-entry rate"),("partial_exit_reached","Partial-exit rate")]:
            if col in plans: lines.append(f"- {label}: {plans[col].fillna(False).astype(bool).mean():.1%}")
        if "exit_type" in plans:
            lines += ["","## Exit types"]
            for name,count in plans["exit_type"].fillna("unknown").value_counts().items():
                lines.append(f"- {name}: {int(count)} ({count/len(plans):.1%})")
        if "horizon" in plans:
            lines += ["","## Horizon evidence"]
            for h,g in plans.groupby("horizon",sort=False):
                p=pd.to_numeric(g["partial_profit_percent"],errors="coerce").dropna()
                lines.append(f"- {h}: plans {len(g)}, target {g['exit_reached'].fillna(False).astype(bool).mean():.1%}, mean partial {p.mean():.2%}" if len(p) else f"- {h}: plans {len(g)}, target {g['exit_reached'].fillna(False).astype(bool).mean():.1%}, mean partial -")
        p=pd.to_numeric(plans.get("partial_profit_percent"),errors="coerce").dropna()
        if len(p):
            lines += ["","## Partial-position outcome",f"- Mean: {p.mean():.2%}",f"- Median: {p.median():.2%}",f"- Positive outcome rate: {(p>0).mean():.1%}"]
        cap=pd.to_numeric(plans.get("capital_deployed"),errors="coerce").dropna()
        if len(cap): lines += [f"- Mean additional capital deployed: ₹{cap.mean():,.0f}",f"- Median additional capital deployed: ₹{cap.median():,.0f}"]
    lines += ["","## V6 changes",
              "- Blocks new averaging plans when the decision-date trend is deteriorating.",
              "- Replaces the unreachable full forecast target with an adaptive target anchored to the forecast and a 5% minimum.",
              "- Preserves T+1 fills, partial entries, 15% stop-loss, deterioration exit and timeout.",
              "- Historical results are evidence for research, not a guarantee of future returns."]
    OUTPUT.write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__": main()
