from __future__ import annotations

import html
import os
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "predictions" / "portfolio_report.csv"
AVG_REPORT = ROOT / "predictions" / "averaging_scenarios.csv"


def money(v):
    if pd.isna(v):
        return "-"
    v = float(v)
    if abs(v) >= 1000:
        return f"₹{v:,.0f}"
    return f"₹{v:,.2f}"


def pct(v):
    if pd.isna(v):
        return "-"
    return f"{float(v) * 100:+.1f}%"


def send_message(token: str, chat_id: str, text: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "true",
    }).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"Telegram API returned HTTP {response.status}")


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID GitHub Actions secret."
        )

    if not REPORT.exists():
        raise RuntimeError(f"Missing report: {REPORT}")

    df = pd.read_csv(REPORT)
    if df.empty:
        raise RuntimeError("Portfolio report is empty.")

    date = str(pd.to_datetime(df.get("run_at_utc", pd.Series([pd.Timestamp.utcnow()]))).max().date()) if "run_at_utc" in df else pd.Timestamp.utcnow().date().isoformat()

    invested = pd.to_numeric(df.get("invested_value"), errors="coerce").sum()
    current = pd.to_numeric(df.get("current_value"), errors="coerce").sum()
    pl = pd.to_numeric(df.get("current_profit_loss"), errors="coerce").sum()
    ret = (current / invested - 1) if invested else float("nan")

    lines = [
        "📊 <b>PORTFOLIO FORECAST</b>",
        f"📅 {date}  •  {len(df)} holdings",
        "",
        f"Invested: <b>{money(invested)}</b>",
        f"Current:  <b>{money(current)}</b>",
        f"P/L:      <b>{money(pl)} ({pct(ret)})</b>",
        "",
        "<pre>",
        "STOCK       NOW       3M      6M      9M     12M",
    ]

    for _, r in df.iterrows():
        symbol = str(r["symbol"])[:10]
        now = money(r["current_price"]).replace("₹", "")
        vals = [
            money(r.get(f"{h}_predicted_price")).replace("₹", "")
            for h in ("3M", "6M", "9M", "12M")
        ]
        lines.append(f"{symbol:<10} {now:>7} {vals[0]:>7} {vals[1]:>7} {vals[2]:>7} {vals[3]:>7}")

    lines += [
        "</pre>",
        "Forecast prices are model estimates, not guaranteed outcomes.",
    ]
    send_message(token, chat_id, "\n".join(lines))

    recovery = [
        "🎯 <b>RECOVERY CHECKPOINT</b>",
        "",
        "<pre>",
        "STOCK       AVG COST   CHECKPOINT",
    ]
    for _, r in df.iterrows():
        symbol = str(r["symbol"])[:10]
        avg = money(r["purchase_price"])
        checkpoint = str(r["first_forecast_horizon_at_or_above_purchase_price"])
        recovery.append(f"{symbol:<10} {avg:>9}   {checkpoint}")
    recovery += ["</pre>", "Checkpoint = first forecast horizon at/above average cost."]
    send_message(token, chat_id, "\n".join(recovery))

    if AVG_REPORT.exists():
        avg = pd.read_csv(AVG_REPORT)
        if not avg.empty:
            current_rows = avg[avg["price_scenario"].eq("current")].copy()
            current_rows = current_rows.drop_duplicates("symbol")
            by_symbol = {str(r["symbol"]): r for _, r in current_rows.iterrows()}

            averaging = [
                "➗ <b>AVERAGING SCENARIOS</b>",
                "",
                "<pre>",
                "STOCK       CURRENT    -5%    -10%    -15%    -20%",
            ]
            for _, r in df.iterrows():
                symbol = str(r["symbol"])[:10]
                rows = avg[avg["symbol"].eq(r["symbol"])].drop_duplicates("price_scenario")
                prices = {}
                for _, a in rows.iterrows():
                    prices[str(a["price_scenario"])] = money(a["buy_price"]).replace("₹", "")
                averaging.append(
                    f"{symbol:<10} "
                    f"{prices.get('current','-'):>7} "
                    f"{prices.get('5% below current','-'):>7} "
                    f"{prices.get('10% below current','-'):>7} "
                    f"{prices.get('15% below current','-'):>7} "
                    f"{prices.get('20% below current','-'):>7}"
                )
            averaging += [
                "</pre>",
                "These are mathematical averaging scenarios, not buy recommendations.",
            ]
            send_message(token, chat_id, "\n".join(averaging))


if __name__ == "__main__":
    main()
