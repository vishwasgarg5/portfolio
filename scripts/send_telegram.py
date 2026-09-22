from __future__ import annotations

import os
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "predictions" / "portfolio_report.csv"
DIVIDENDS = ROOT / "data" / "dividends.csv"
MAX_TELEGRAM_CHARS = 3900


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


def table_messages(title, headers, rows, max_chars=MAX_TELEGRAM_CHARS):
    """Build one or more row-safe Telegram messages below the API limit."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        widths = [max(w, len(str(v))) for w, v in zip(widths, row)]

    header = " ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers))
    separator = " ".join("-" * w for w in widths)

    def row_text(row):
        return " ".join(str(v).ljust(widths[i]) for i, v in enumerate(row))

    messages = []
    current = [f"📊 <b>{title}</b>", "<pre>", header, separator]
    current_len = sum(len(x) + 1 for x in current) + len("</pre>")

    for row in rows:
        line = row_text(row)
        # Keep every row intact; split only between rows.
        added = len(line) + 1
        if len(current) > 3 and current_len + added + len("</pre>") > max_chars:
            current.append("</pre>")
            messages.append("\n".join(current))
            current = [f"📊 <b>{title}</b>", "<pre>", header, separator]
            current_len = sum(len(x) + 1 for x in current) + len("</pre>")
        current.append(line)
        current_len += added

    current.append("</pre>")
    messages.append("\n".join(current))
    return messages


def send_table(token, chat_id, title, headers, rows):
    for message in table_messages(title, headers, rows):
        send_message(token, chat_id, message)


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

    date = (
        str(pd.to_datetime(df["market_data_date"], errors="coerce").max().date())
        if "market_data_date" in df else pd.Timestamp.utcnow().date().isoformat()
    )
    invested = pd.to_numeric(df["invested_value"], errors="coerce").sum()
    current = pd.to_numeric(df["current_value"], errors="coerce").sum()
    pl = pd.to_numeric(df["current_profit_loss"], errors="coerce").sum()
    ret = current / invested - 1 if invested else float("nan")

    send_message(token, chat_id, "\n".join([
        "📊 <b>PORTFOLIO | DAILY</b>",
        f"📅 {date}  •  {len(df)} holdings",
        "",
        f"INVESTED  <b>{money(invested)}</b>",
        f"CURRENT   <b>{money(current)}</b>",
        f"P/L       <b>{money(pl)}  {pct(ret)}</b>",
    ]))

    rows = []
    for i, (_, r) in enumerate(df.iterrows(), 1):
        rows.append([
            str(i), str(r["symbol"]).replace(".NS", "")[:8],
            str(int(float(r["quantity"]))),
            money(r["purchase_price"]), money(r["current_price"]),
            pct(r["current_return"]),
        ])
    send_table(token, chat_id, "PORTFOLIO",
               ["#","Stock","Qty","Avg","Now","P/L"], rows)

    for title, horizons in [
        ("FORECAST | 3–12M", ("3M", "6M", "9M", "12M")),
        ("FORECAST | 18–36M", ("18M", "24M", "36M")),
    ]:
        rows = []
        for i, (_, r) in enumerate(df.iterrows(), 1):
            rows.append([
                str(i), str(r["symbol"]).replace(".NS", "")[:8],
                *[
                    money(r.get(f"{h}_predicted_price"))
                    if pd.notna(r.get(f"{h}_predicted_price")) else "-"
                    for h in horizons
                ],
            ])
        send_table(token, chat_id, title, ["#","Stock",*horizons], rows)

    plan_path = ROOT / "predictions" / "averaging_plan.csv"
    if plan_path.exists():
        plan = pd.read_csv(plan_path)
        if not plan.empty:
            rows = []
            for i, (_, x) in enumerate(plan.iterrows(), 1):
                rows.append([
                    str(i), str(x["symbol"]).replace(".NS", "")[:8],
                    f'B{x["entry"]}', money(x["buy_price"]),
                    str(int(float(x["additional_quantity"]))),
                    money(x["cumulative_average"]),
                    str(x["horizon"]), pct(x["forecast_profit_percent"]),
                ])
            if rows:
                send_table(token, chat_id, "AVERAGING | ACTION PLAN",
                           ["#","Stock","Buy","Price","Add","New Avg","Exit","Profit"], rows)

    stability_rows = []
    for i, (_, r) in enumerate(df.iterrows(), 1):
        flags = []
        for h in ("3M","6M","12M","18M","24M","36M"):
            s = str(r.get(f"{h}_prediction_stability", ""))
            if s in {"watch", "large_change"}:
                flags.append(f"{h}:{s}")
        if flags:
            stability_rows.append([
                str(i), str(r["symbol"]).replace(".NS", "")[:8], " ".join(flags)
            ])
    if stability_rows:
        send_table(token, chat_id, "FORECAST | CHANGES",
                   ["#","Stock","Change"], stability_rows)

    rows = []
    if DIVIDENDS.exists():
        div = pd.read_csv(DIVIDENDS)
        if not div.empty and "ex_date" in div.columns:
            div["_ex_date"] = pd.to_datetime(div["ex_date"], errors="coerce")
            today = pd.Timestamp.now(tz="Asia/Kolkata").tz_localize(None).normalize()
            div = div[
                div["_ex_date"].notna() & (div["_ex_date"] >= today)
            ].sort_values(["_ex_date", "symbol"] if "symbol" in div.columns else "_ex_date")
            for i, (_, r) in enumerate(div.iterrows(), 1):
                rows.append([
                    str(i), str(r.get("symbol", "")).replace(".NS", "")[:8],
                    money(r.get("dividend_per_share")),
                    str(r.get("ex_date", ""))[:10],
                    str(r.get("cum_date", ""))[:10],
                    pct(r.get("dividend_yield")),
                ])

    if rows:
        send_table(token, chat_id, "DIVIDEND | NIFTY 500",
                   ["#","Stock","Div/SH","Ex-Date","Buy-By","Yield"], rows)
    else:
        send_table(token, chat_id, "DIVIDEND | NIFTY 500",
                   ["#","Stock","Div/SH","Ex-Date","Buy-By","Yield"],
                   [["-","NONE","-","-","-","-"]])


if __name__ == "__main__":
    main()
