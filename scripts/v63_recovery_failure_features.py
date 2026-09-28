from pathlib import Path
import sys
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data import load_history

SRC = ROOT / "predictions" / "v6_deterioration_followthrough.csv"
OUT_CSV = ROOT / "predictions" / "v63_recovery_failure_features.csv"
OUT_MD = ROOT / "predictions" / "v63_recovery_failure_features.md"

df = pd.read_csv(SRC)
if df.empty:
    raise SystemExit("No V6 deterioration exits")

rows = []
cache = {}
for _, r in df.iterrows():
    symbol = str(r["symbol"])
    if symbol not in cache:
        cache[symbol] = load_history(symbol).sort_index()
    prices = cache[symbol]
    exit_date = pd.Timestamp(r["exit_date"])
    if exit_date not in prices.index:
        idx = prices.index.searchsorted(exit_date)
        if idx >= len(prices):
            continue
        exit_date = prices.index[idx]
    close = prices["Close"]
    ma20 = close.rolling(20, min_periods=20).mean()
    ma50 = close.rolling(50, min_periods=50).mean()
    ma20_5ago = ma20.shift(5)
    prior10 = prices["Low"].shift(1).rolling(10, min_periods=10).min()
    prior20 = prices["Low"].shift(1).rolling(20, min_periods=20).min()
    px = float(close.loc[exit_date])
    m20 = ma20.get(exit_date)
    m50 = ma50.get(exit_date)
    rec = {
        "symbol": symbol, "name": str(r["name"]), "plan_date": str(r["plan_date"]),
        "exit_date": str(r["exit_date"]), "horizon": str(r["horizon"]),
        "partial_profit_percent": float(r["partial_profit_percent"]),
        "entries_reached": int(r["entries_reached"]),
        "close": px,
        "ma20_gap_pct": px / float(m20) - 1 if pd.notna(m20) else np.nan,
        "ma50_gap_pct": px / float(m50) - 1 if pd.notna(m50) else np.nan,
        "ma20_slope_5d_pct": float(m20 / ma20_5ago.get(exit_date) - 1) if pd.notna(m20) and pd.notna(ma20_5ago.get(exit_date)) else np.nan,
        "below_prior10_low": bool(pd.notna(prior10.get(exit_date)) and px < float(prior10.get(exit_date))),
        "below_prior20_low": bool(pd.notna(prior20.get(exit_date)) and px < float(prior20.get(exit_date))),
        "recovered_5pct_20d": bool(r["recovered_5pct_20d"]),
        "recovered_5pct_60d": bool(r["recovered_5pct_60d"]),
        "recovered_5pct_120d": bool(r["recovered_5pct_120d"]),
    }
    rows.append(rec)

out = pd.DataFrame(rows)
out["outcome_60d"] = np.where(out["recovered_5pct_60d"], "recovered_5pct", "not_recovered_5pct")
out["outcome_120d"] = np.where(out["recovered_5pct_120d"], "recovered_5pct", "not_recovered_5pct")
out.to_csv(OUT_CSV, index=False)

lines = ["# V6.3 Recovery-vs-Failure Feature Analysis", "",
         f"- V6 deterioration exits analysed: {len(out)}",
         "- Features use only information available on the deterioration-exit date.",
         "- No future recovery information is used to construct the exit-date features.",
         "",
         "## Recovery definition",
         "- Primary: price reaches at least +5% above the V6 exit price within the next 60 trading sessions.",
         "- Secondary: same test within 120 trading sessions.",
         "",
         "## Outcome counts"]
for col, label in [("outcome_60d","60-session"),("outcome_120d","120-session")]:
    lines += [f"- {label}: {out[col].value_counts().to_dict()}"]

features = ["ma20_gap_pct","ma50_gap_pct","ma20_slope_5d_pct","below_prior10_low","below_prior20_low","entries_reached","partial_profit_percent"]
for f in features:
    g = out.groupby("outcome_60d")[f].agg(["count","mean","median"])
    lines += ["", f"## {f} by 60-session outcome", g.to_string()]
lines += ["", "## Candidate rule coverage",
          f"- Below prior 10-day low: {out.below_prior10_low.mean()*100:.1f}%",
          f"- Below prior 20-day low: {out.below_prior20_low.mean()*100:.1f}%",
          f"- Negative 5-day MA20 slope: {(out.ma20_slope_5d_pct < 0).mean()*100:.1f}%",
          "",
          "## Interpretation",
          "- This is feature discovery, not a strategy promotion test.",
          "- Any V6.3 rule must be fixed from this analysis and then tested on the same historical origins without using future outcomes.",
          "- No V7 promotion should occur from this analysis alone."]
OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
