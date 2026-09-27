from __future__ import annotations

import os
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "predictions" / "portfolio_report.csv"
LEARNING = ROOT / "predictions" / "model_learning.csv"
SCORECARD = ROOT / "predictions" / "model_scorecard.csv"
BACKTEST = ROOT / "predictions" / "strategy_backtest_report.md"
MAX_CHARS = 3900


def money(v):
    if pd.isna(v):
        return "-"
    v = float(v)
    return f"₹{v:,.0f}" if abs(v) >= 1000 else f"₹{v:,.2f}"


def pct(v):
    if pd.isna(v):
        return "-"
    return f"{float(v) * 100:+.1f}%"


def price(v):
    return "-" if pd.isna(v) else f"₹{float(v):,.0f}"


def sym(v):
    return str(v).replace(".NS", "")


def send_message(token, chat_id, text):
    if len(text) > MAX_CHARS:
        raise RuntimeError(f"Telegram message exceeds {MAX_CHARS} chars: {len(text)}")
    data = urllib.parse.urlencode({
        "chat_id": chat_id, "text": text, "parse_mode": "HTML",
        "disable_web_page_preview": "true",
    }).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=data, method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"Telegram API returned HTTP {response.status}")


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.")
    if not REPORT.exists():
        raise RuntimeError(f"Missing report: {REPORT}")

    df = pd.read_csv(REPORT)
    if df.empty:
        raise RuntimeError("Portfolio report is empty.")

    date = str(pd.to_datetime(df["market_data_date"], errors="coerce").max().date())
    invested = pd.to_numeric(df["invested_value"], errors="coerce").sum()
    current = pd.to_numeric(df["current_value"], errors="coerce").sum()
    pl = pd.to_numeric(df["current_profit_loss"], errors="coerce").sum()
    ret = current / invested - 1 if invested else float("nan")

    work = df.copy()
    work["_ret"] = pd.to_numeric(work["current_return"], errors="coerce")
    gainers = work.nlargest(3, "_ret")
    losers = work.nsmallest(3, "_ret")

    m1 = [
        "📊 <b>PORTFOLIO · DAILY</b>",
        f"📅 {date} · {len(df)} holdings",
        "",
        f"💰 Invested  <b>{money(invested)}</b>",
        f"💼 Value     <b>{money(current)}</b>",
        f"📈 P/L       <b>{money(pl)}  {pct(ret)}</b>",
        "",
        "🟢 <b>TOP GAINERS</b>",
    ]
    for _, r in gainers.iterrows():
        m1.append(f"• {sym(r['symbol'])}: {pct(r['_ret'])}")
    m1.append("🔴 <b>TOP LOSERS</b>")
    for _, r in losers.iterrows():
        m1.append(f"• {sym(r['symbol'])}: {pct(r['_ret'])}")

    m1 += ["", "💵 <b>DIVIDEND</b>"]
    ex = pd.to_datetime(work.get("next_dividend_ex_date"), errors="coerce")
    upcoming = work[ex.notna()].sort_values("next_dividend_ex_date").head(5)
    if upcoming.empty:
        m1.append("• No upcoming dividend data")
    else:
        for _, r in upcoming.iterrows():
            m1.append(
                f"• {sym(r['symbol'])}: {money(r.get('next_dividend_per_share'))}/sh"
                f" · ex {str(r.get('next_dividend_ex_date',''))[:10]}"
            )

    m1 += ["", "⚠️ <b>ALERTS</b>"]
    if "trend_20d_health" in work:
        bad = int(work["trend_20d_health"].astype(str).eq("deteriorating").sum())
        m1.append(f"• Deteriorating trend: {bad}")
    changes = 0
    for h in ("3M","6M","12M","18M","24M","36M"):
        col = f"{h}_prediction_stability"
        if col in work:
            changes += int(work[col].astype(str).isin(["watch","large_change"]).sum())
    m1.append(f"• Forecast watch/large change: {changes}")

    m1 += ["", "📋 <b>HOLDINGS</b>", "<pre>Stock       Qty    Avg     Now     P/L"]
    for _, r in work.iterrows():
        m1.append(
            f"{sym(r['symbol'])[:10]:10} {int(float(r['quantity'])):5d} "
            f"{float(r['purchase_price']):7.2f} {float(r['current_price']):7.2f} "
            f"{pct(r['_ret']):>7}"
        )
    m1.append("</pre>")
    send_message(token, chat_id, "\n".join(m1))

    m2 = [
        "🧠 <b>PORTFOLIO INTELLIGENCE</b>",
        f"📅 {date}",
        "",
        "🔮 <b>FORECAST · 3M → 36M</b>",
        "<pre>Stock       Now   3M   6M  12M  18M  24M  36M",
    ]
    for _, r in work.iterrows():
        vals = [price(r.get(f"{h}_predicted_price")) for h in ("3M","6M","12M","18M","24M","36M")]
        m2.append(
            f"{sym(r['symbol'])[:10]:10} {price(r['current_price']):>5} "
            + " ".join(f"{v:>5}" for v in vals)
        )
    m2.append("</pre>")

    m2 += ["🎯 <b>ACTIONABLE AVERAGING</b>"]
    plan_path = ROOT / "predictions" / "averaging_plan.csv"
    plan = pd.read_csv(plan_path) if plan_path.exists() else pd.DataFrame()
    if plan.empty:
        m2.append("• No qualifying averaging plan")
    else:
        for _, x in plan.iterrows():
            m2.append(
                f"• {sym(x['symbol'])}: B{x['entry']} {money(x['buy_price'])}"
                f" +{int(float(x['additional_quantity']))} → avg {money(x['cumulative_average'])}"
                f" · target {pct(x['forecast_profit_percent'])}"
            )

    m2 += ["", "🧪 <b>MODEL LEARNING</b>"]
    learning = pd.read_csv(LEARNING) if LEARNING.exists() else pd.DataFrame()
    if learning.empty:
        m2.append("• Completed real-forecast evaluations: 0")
    else:
        m2.append(f"• Forecasts evaluated: {len(learning)}")
        for col, label in [("mae","MAE"),("rmse","RMSE"),("direction_accuracy","Direction")]:
            if col in learning.columns:
                v = pd.to_numeric(learning[col], errors="coerce").dropna()
                if len(v):
                    m2.append(f"• {label}: {pct(v.iloc[-1])}")

    score = pd.read_csv(SCORECARD) if SCORECARD.exists() else pd.DataFrame()
    if not score.empty and "validation_mae" in score:
        v = pd.to_numeric(score["validation_mae"], errors="coerce").dropna()
        if len(v):
            m2.append(f"• Current validation MAE: {v.mean():.1%} avg")

    m2 += ["", "🧪 <b>BACKTEST EVIDENCE</b>"]
    if BACKTEST.exists():
        lines = BACKTEST.read_text(encoding="utf-8").splitlines()
        useful = [x[2:] for x in lines if x.startswith("- ")][:7]
        m2.extend(f"• {x}" for x in useful)
    else:
        m2.append("• Report not available")

    m2 += [
        "",
        "🔄 Forecast = estimate, not guaranteed return.",
        "⚠️ Long-horizon forecasts have higher uncertainty.",
    ]
    send_message(token, chat_id, "\n".join(m2))


if __name__ == "__main__":
    main()
