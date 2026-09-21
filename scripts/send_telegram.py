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
LEARNING = ROOT / "predictions" / "model_learning.csv"
SCORECARD = ROOT / "predictions" / "model_scorecard.csv"
AVG_LEARNING = ROOT / "predictions" / "averaging_learning.csv"


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

    portfolio_rows = []
    for i, (_, r) in enumerate(df.iterrows(), 1):
        portfolio_rows.append([
            str(i), str(r["symbol"])[:10], str(int(float(r["quantity"]))),
            money(r["purchase_price"]), money(r["current_price"]), pct(r["current_return"])
        ])
    send_message(token, chat_id, table_message("PORTFOLIO", ["#","Stock","Qty","Avg","Now","P/L"], portfolio_rows))

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

    # User-facing averaging output: only the current actionable staged plan.
    # averaging_learning.csv remains an internal learning/evaluation dataset and
    # is intentionally never sent to Telegram.
    plan_path = ROOT / "predictions" / "averaging_plan.csv"
    if plan_path.exists():
        plan = pd.read_csv(plan_path)
        if not plan.empty:
            signal_rows = []
            for i, (_, x) in enumerate(plan.iterrows(), 1):
                signal_rows.append([
                    str(i), str(x["symbol"])[:10], f'B{x["entry"]}',
                    money(x["buy_price"]), str(int(float(x["additional_quantity"]))),
                    money(x["capital"]), money(x["cumulative_average"]),
                    money(x["forecast_exit_price"]), str(x["horizon"]), pct(x["forecast_profit_percent"])
                ])
            if signal_rows:
                send_message(token, chat_id, table_message(
                    "EARLY-PROFIT AVERAGING PLAN",
                    ["#","Stock","Buy","Price","Add Qty","Capital","Cum Avg","Exit","Horizon","Profit"],
                    signal_rows,
                    "Buy levels are conditional triggers. The model uses a staged plan and whole shares."
                ))
    elif AVG_SIGNALS.exists():
        sig = pd.read_csv(AVG_SIGNALS)
        signal_rows = []
        for i, (_, x) in enumerate(sig.iterrows(), 1):
            if str(x.get("signal")) != "AVERAGING PLAN":
                continue
            signal_rows.append([
                str(i), str(x["symbol"])[:10], money(x["total_capital"]),
                str(x["horizon"]), str(int(float(x["total_additional_quantity"]))),
                money(x["final_average"]), money(x["forecast_exit_price"]),
                pct(x["forecast_profit_percent"])
            ])
        if signal_rows:
            send_message(token, chat_id, table_message(
                "EARLY-PROFIT AVERAGING",
                ["#","Stock","Capital","Horizon","Add Qty","New Avg","Exit","Profit"],
                signal_rows
            ))

    # Model learning remains available internally; it is not a user-facing
    # Telegram table unless explicitly requested.
    # Forecast stability is also kept user-facing because it flags meaningful
    # changes in the current forecast.

    stability_rows=[]
    for i,(_,r) in enumerate(df.iterrows(),1):
        flags=[]
        for h in ("3M","6M","12M","18M","24M","36M"):
            s=str(r.get(f"{h}_prediction_stability",""))
            if s in {"watch","large_change"}:
                flags.append(f"{h}:{s}")
        if flags:
            stability_rows.append([str(i),str(r["symbol"])[:10]," ".join(flags)])
    if stability_rows:
        send_message(token,chat_id,table_message(
            "FORECAST STABILITY",["#","Stock","Change"],stability_rows,
            "Watch = >10% change; large_change = >20% change versus previous run."
        ))

    if DIVIDENDS.exists():
        div = pd.read_csv(DIVIDENDS)
        if not div.empty:
            rows = []
            for i, (_, r) in enumerate(div.sort_values("ex_date").iterrows(), 1):
                qty = df.loc[df["symbol"].eq(r["symbol"]), "quantity"]
                held_qty = int(float(qty.iloc[0])) if not qty.empty and pd.notna(qty.iloc[0]) else 0
                income = float(r["dividend_per_share"]) * held_qty if pd.notna(r["dividend_per_share"]) else float("nan")
                rows.append([
                    str(i), str(r["symbol"])[:10], str(held_qty), money(r["dividend_per_share"]),
                    money(income), str(r["ex_date"]), str(r["cum_date"]), pct(r["dividend_yield"])
                ])
            send_message(token, chat_id, table_message(
                "DIVIDEND", ["#","Stock","Qty","Div/SH","Income","Ex-Date","Buy-By","Yield"], rows,
                "Upcoming dividend opportunities for the configured portfolio."
            ))


if __name__ == "__main__":
    main()
