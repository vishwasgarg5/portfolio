from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data import load_history
from src.strategy_backtest import run_strategy_backtest

OUT_CSV = ROOT / "predictions" / "v62_confirmation_experiment.csv"
OUT_MD = ROOT / "predictions" / "v62_confirmation_experiment.md"

stocks = pd.read_csv(ROOT / "config" / "stocks.csv")
rows = []

for mode, confirmation_mode in (("V6_control", "none"), ("V6.2_prior_low", "prior_low"), ("V6.3_next_close", "next_close")):
    for r in stocks.to_dict("records"):
        try:
            prices = load_history(str(r["symbol"]))
            out = run_strategy_backtest(
                prices, str(r["symbol"]), str(r["name"]),
                float(r["shares"]), float(r["purchase_price"]),
                deterioration_days=3, confirmation_mode=confirmation_mode
            )
            for x in out:
                y = dict(x)
                y["variant"] = mode
                rows.append(y)
        except Exception as exc:
            rows.append({
                "variant": mode, "symbol": r["symbol"], "name": r["name"],
                "decision": f"error: {exc}"
            })

df = pd.DataFrame(rows)
df.to_csv(OUT_CSV, index=False)

plans = df[df["decision"].eq("plan")].copy()
lines = ["# V6.2 Deterioration Confirmation Experiment", "",
         "- V6 control: 3-day deterioration condition only.",
         "- V6.2 confirmation: 3-day deterioration condition PLUS close below the prior 10-session low.",
         "- The confirmation is evaluated only after a plan has been created; the entry/origin set is otherwise unchanged.",
         ""]
for variant, g in plans.groupby("variant"):
    lines += [
        f"## {variant}",
        f"- Plan rows: {len(g)}",
        f"- Target exits: {(g.exit_type == 'target').sum()} ({(g.exit_type == 'target').mean()*100:.1f}%)",
        f"- Deterioration exits: {(g.exit_type == 'deterioration').sum()} ({(g.exit_type == 'deterioration').mean()*100:.1f}%)",
        f"- Stop-loss exits: {(g.exit_type == 'stop_loss').sum()} ({(g.exit_type == 'stop_loss').mean()*100:.1f}%)",
        f"- Positive partial outcomes: {(g.partial_profit_percent > 0).mean()*100:.1f}%",
        f"- Mean partial outcome: {g.partial_profit_percent.mean()*100:.2f}%",
        f"- Median partial outcome: {g.partial_profit_percent.median()*100:.2f}%",
        f"- Mean capital deployed: ₹{g.capital_deployed.mean():,.0f}",
        f"- Mean exit days: {((pd.to_datetime(g.exit_date, errors='coerce') - pd.to_datetime(g.plan_date, errors='coerce')).dt.days).mean():.1f}",
        ""
    ]

lines += [
    "## Decision rule",
    "- V6 remains the control.",
    "- V6.2 should only proceed to deeper testing if confirmation changes downside/recovery behaviour without an unacceptable increase in capital deployment or holding time.",
    "- This experiment does not by itself establish a preferred strategy."
]
OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
