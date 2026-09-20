from __future__ import annotations

import os
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "predictions" / "portfolio_report.csv"
AVG_REPORT = ROOT / "predictions" / "averaging_scenarios.csv"
AVG_SIGNALS = ROOT / "predictions" / "averaging_profit_signals.csv"
DIVIDENDS = ROOT / "data" / "dividends.csv"
DIV_HISTORY = ROOT / "predictions" / "dividend_history.csv"
DIV_CAPTURE_SUMMARY = ROOT / "predictions" / "dividend_capture_summary.csv"


def money(v):
    if pd.isna(v):
        return "-"
    v = float(v)
    return f"₹{v:,.0f}" if abs(v) >= 1000 else f"₹{v:,.2f}"


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


def table_message(title, headers, rows, footer=None):
    lines = [f"📊 <b>{title}</b>", "", "<pre>"]
    widths = [len(str(h)) for h in headers]
    for row in rows:
        widths = [max(w, len(str(v))) for w, v in zip(widths, row)]
    lines.append(" | ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)))
    lines.append("-+-".join("-" * w for w in widths))
    for row in rows:
        lines.append(" | ".join(str(v).ljust(widths[i]) for i, v in enumerate(row)))
    lines.append("</pre>")
    if footer:
        lines.append(footer)
    return "\n".join(lines)


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID GitHub Actions secret.")
    if not REPORT.exists():
        raise RuntimeError(f"Missing report: {REPORT}")

    df = pd.read_csv(REPORT)
    if df.empty:
        raise RuntimeError("Portfolio report is empty.")

    date = str(pd.to_datetime(df["market_data_date"], errors="coerce").max().date()) if "market_data_date" in df else pd.Timestamp.utcnow().date().isoformat()
    invested = pd.to_numeric(df["invested_value"], errors="coerce").sum()
    current = pd.to_numeric(df["current_value"], errors="coerce").sum()
    pl = pd.to_numeric(df["current_profit_loss"], errors="coerce").sum()
    ret = current / invested - 1 if invested else float("nan")

    send_message(token, chat_id, "\n".join([
        "📊 <b>PORTFOLIO DAILY SUMMARY</b>",
        f"📅 Market data: {date} • {len(df)} holdings",
        "",
        f"Invested: <b>{money(invested)}</b>",
        f"Current:  <b>{money(current)}</b>",
        f"P/L:      <b>{money(pl)} ({pct(ret)})</b>",
        "",
        "Forecasts are model estimates, not guaranteed outcomes.",
    ]))

    # Table 1: compact current portfolio
    portfolio_rows = []
    for i, (_, r) in enumerate(df.iterrows(), 1):
        portfolio_rows.append([
            str(i), str(r["symbol"])[:10], str(int(float(r["quantity"]))),
            money(r["purchase_price"]), money(r["current_price"]), pct(r["current_return"])
        ])
    send_message(token, chat_id, table_message("PORTFOLIO", ["#","Stock","Qty","Avg","Now","P/L"], portfolio_rows))

    # Table 2: requested forecast horizons only.
    forecast_rows = []
    for i, (_, r) in enumerate(df.iterrows(), 1):
        forecast_rows.append([
            str(i), str(r["symbol"])[:10],
            *[money(r.get(f"{h}_predicted_price")) if pd.notna(r.get(f"{h}_predicted_price")) else "N/A"
              for h in ("3M","6M","12M","18M","24M","36M")]
        ])
    send_message(token, chat_id, table_message(
        "FORECAST", ["#","Stock","3M","6M","12M","18M","24M","36M"], forecast_rows,
        "N/A = no valid forecast for that horizon."
    ))

    # Table 3: only stocks with a qualifying early-profit averaging scenario.
    if AVG_SIGNALS.exists():
        sig = pd.read_csv(AVG_SIGNALS)
        signal_rows = []
        for i, (_, x) in enumerate(sig.iterrows(), 1):
            if str(x.get("signal")) != "AVERAGING CANDIDATE":
                continue
            signal_rows.append([
                str(i), str(x["symbol"])[:10], money(x["buy_price"]), str(x["horizon"]),
                str(int(float(x["additional_quantity"]))), money(x["new_average"]),
                money(x["forecast_exit_price"]), pct(x["forecast_profit_percent"])
            ])
        if signal_rows:
            send_message(token, chat_id, table_message(
                "EARLY-PROFIT AVERAGING",
                ["#","Stock","Buy","Horizon","Add Qty","New Avg","Exit","Profit"],
                signal_rows,
                "Only qualifying model scenarios are shown; not a guarantee."
            ))

    # Final table: upcoming dividend opportunities only.
    if DIVIDENDS.exists():
        div = pd.read_csv(DIVIDENDS)
        if not div.empty:
            rows = []
            for i, (_, r) in enumerate(div.sort_values("ex_date").iterrows(), 1):
                rows.append([str(i), str(r["symbol"])[:10], money(r["dividend_per_share"]),
                             str(r["ex_date"]), str(r["cum_date"]), pct(r["dividend_yield"])])
            send_message(token, chat_id, table_message(
                "DIVIDEND", ["#","Stock","Div/SH","Ex-Date","Buy-By","Yield"], rows,
                "Upcoming dividend opportunities for the configured portfolio."
            ))

if __name__ == "__main__":
    main()
