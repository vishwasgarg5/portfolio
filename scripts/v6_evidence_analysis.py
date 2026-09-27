from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "predictions" / "strategy_backtest.csv"
OUT = ROOT / "predictions" / "v6_evidence_analysis.md"

def pct(x):
    return f"{x * 100:.1f}%"

df = pd.read_csv(SRC)
plans = df[df["decision"].eq("plan")].copy()
if plans.empty:
    raise SystemExit("No V6 plan rows available")

plans["exit_days"] = (
    pd.to_datetime(plans["exit_date"], errors="coerce")
    - pd.to_datetime(plans["plan_date"], errors="coerce")
).dt.days

lines = [
    "# V6 Evidence Analysis",
    "",
    f"- Plan rows: {len(plans)}",
    f"- Deterioration exits: {(plans['exit_type'] == 'deterioration').sum()} ({pct((plans['exit_type'] == 'deterioration').mean())})",
    f"- Target exits: {(plans['exit_type'] == 'target').sum()} ({pct((plans['exit_type'] == 'target').mean())})",
    f"- Stop-loss exits: {(plans['exit_type'] == 'stop_loss').sum()} ({pct((plans['exit_type'] == 'stop_loss').mean())})",
    f"- Mean days to exit: {plans['exit_days'].mean():.1f}",
    f"- Median days to exit: {plans['exit_days'].median():.1f}",
    f"- Mean partial outcome: {plans['partial_profit_percent'].mean() * 100:.2f}%",
    "",
    "## Deterioration timing",
]
det = plans[plans["exit_type"].eq("deterioration")]
if not det.empty:
    lines += [
        f"- Mean deterioration exit: {det['exit_days'].mean():.1f} days",
        f"- Median deterioration exit: {det['exit_days'].median():.1f} days",
        f"- Exits within 20 days: {(det['exit_days'] <= 20).sum()} / {len(det)}",
        f"- Exits within 60 days: {(det['exit_days'] <= 60).sum()} / {len(det)}",
    ]

lines += ["", "## By horizon"]
for h, g in plans.groupby("horizon", sort=True):
    target = g["exit_type"].eq("target").mean()
    det_rate = g["exit_type"].eq("deterioration").mean()
    positive = (g["partial_profit_percent"] > 0).mean()
    lines.append(
        f"- {h}: plans {len(g)}, target {pct(target)}, deterioration {pct(det_rate)}, "
        f"positive partial {pct(positive)}, mean partial {g['partial_profit_percent'].mean() * 100:.2f}%"
    )

lines += ["", "## By stock"]
for symbol, g in plans.groupby("symbol"):
    lines.append(
        f"- {symbol}: plans {len(g)}, target {g['exit_type'].eq('target').sum()}, "
        f"deterioration {g['exit_type'].eq('deterioration').sum()}, "
        f"mean partial {g['partial_profit_percent'].mean() * 100:.2f}%"
    )

lines += [
    "",
    "## Interpretation",
    "- Deterioration exits dominate V6 and are often early relative to the intended horizon.",
    "- This supports testing a deterioration grace period rather than immediately replacing the strategy.",
    "- The next experiment should preserve V6 as the baseline and test a V6.1 grace-period variant on the same historical origins.",
    "- No V7 promotion should occur until V6.1 is compared directly with V6 on target rate, downside, positive-outcome rate, capital deployment and exit timing.",
]
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
