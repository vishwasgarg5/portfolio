from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data import load_history

SRC = ROOT / "predictions" / "strategy_backtest.csv"
OUT_CSV = ROOT / "predictions" / "v6_deterioration_followthrough.csv"
OUT_MD = ROOT / "predictions" / "v6_deterioration_followthrough.md"
WINDOWS = (20, 60, 120)

def pct(x):
    return f"{x * 100:.1f}%"

bt = pd.read_csv(SRC)
plans = bt[(bt["decision"] == "plan") & (bt["exit_type"] == "deterioration")].copy()
if plans.empty:
    raise SystemExit("No V6 deterioration exits available")

rows = []
cache = {}
for _, r in plans.iterrows():
    symbol = str(r["symbol"])
    if symbol not in cache:
        cache[symbol] = load_history(symbol).sort_index()
    future = cache[symbol].loc[cache[symbol].index > pd.Timestamp(r["exit_date"])]
    exit_price = float(r["actual_exit_price"])
    rec = {"symbol": symbol, "name": str(r["name"]), "plan_date": str(r["plan_date"]),
           "exit_date": str(r["exit_date"]), "horizon": str(r["horizon"]),
           "exit_price": exit_price, "partial_profit_percent": float(r["partial_profit_percent"]),
           "entries_reached": int(r["entries_reached"])}
    for w in WINDOWS:
        window = future.iloc[:w]
        if window.empty:
            rec[f"max_close_return_{w}d"] = float("nan")
            rec[f"max_high_return_{w}d"] = float("nan")
            rec[f"recovered_5pct_{w}d"] = False
            rec[f"recovered_to_exit_{w}d"] = False
        else:
            rec[f"max_close_return_{w}d"] = float(window["Close"].max() / exit_price - 1.0)
            rec[f"max_high_return_{w}d"] = float(window["High"].max() / exit_price - 1.0)
            rec[f"recovered_5pct_{w}d"] = rec[f"max_high_return_{w}d"] >= 0.05
            rec[f"recovered_to_exit_{w}d"] = rec[f"max_high_return_{w}d"] >= 0.0
    rows.append(rec)

df = pd.DataFrame(rows)
df.to_csv(OUT_CSV, index=False)

lines = ["# V6 Deterioration Follow-Through Analysis", "",
         f"- Deterioration exits analysed: {len(df)}",
         "- Purpose: measure post-exit behaviour before changing the deterioration rule."]
for w in WINDOWS:
    close = df[f"max_close_return_{w}d"].dropna()
    high = df[f"max_high_return_{w}d"].dropna()
    lines += ["", f"## Next {w} trading sessions",
              f"- Mean maximum close return after exit: {close.mean()*100:.2f}%",
              f"- Median maximum close return after exit: {close.median()*100:.2f}%",
              f"- Mean maximum high return after exit: {high.mean()*100:.2f}%",
              f"- Recovered to exit price: {pct(df[f'recovered_to_exit_{w}d'].mean())}",
              f"- Recovered at least +5% above exit: {pct(df[f'recovered_5pct_{w}d'].mean())}"]
lines += ["", "## By stock"]
for symbol, g in df.groupby("symbol"):
    lines.append(f"- {symbol}: exits {len(g)}, mean partial outcome {g['partial_profit_percent'].mean()*100:.2f}%, "
                 f"5% recovery within 60d {pct(g['recovered_5pct_60d'].mean())}")
lines += ["", "## Interpretation",
          "- Post-exit recovery is evidence for review, not proof that a deterioration exit was wrong.",
          "- The next strategy experiment should preserve V6 as the control and test any new confirmation rule on the same historical origins.",
          "- No new version should be promoted until downside, recovery, capital deployment and exit timing are compared together."]
OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
