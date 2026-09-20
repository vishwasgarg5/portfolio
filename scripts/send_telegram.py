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
DIVIDENDS = ROOT / "data" / "dividends.csv"
DIV_HISTORY = ROOT / "predictions" / "dividend_history.csv"
DIV_CAPTURE_SUMMARY = ROOT / "predictions" / "dividend_capture_summary.csv"


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
        "Index   | Stock      | Qty    | Avg       | Now       | P/L %     | 3M        | 6M        | 9M        | 12M       | 18M       | 24M       | 36M",
        "--------|------------|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------",
    ]
    for i, (_, r) in enumerate(df.iterrows(), 1):
        symbol = str(r["symbol"])[:10]
        qty = f"{float(r['quantity']):g}"
        avg = money(r["purchase_price"])
        now = money(r["current_price"])
        pl_pct = pct(r["current_return"])
        vals = [money(r.get(f"{h}_predicted_price")) for h in ("3M", "6M", "9M", "12M", "18M", "24M", "36M")]
        lines.append(f"{i:>5} | {symbol:<10} | {qty:>6} | {avg:>9} | {now:>9} | {pl_pct:>9} | " + " | ".join(f"{v:>9}" for v in vals))
    lines += [
        "</pre>",
        "AVG = configured purchase price; NOW = latest available market close.",
        "Forecast prices are model estimates, not guaranteed outcomes.",
    ]
    send_message(token, chat_id, "\n".join(lines))

    recovery = [
        "🎯 <b>RECOVERY CHECKPOINT</b>",
        "",
        "<pre>",
        "Index | Stock      | Avg       | 3M        | 6M        | 9M        | 12M       | 18M       | 24M       | 36M       | First",
        "------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------",
    ]
    for i, (_, r) in enumerate(df.iterrows(), 1):
        symbol = str(r["symbol"])[:10]
        avg = money(r["purchase_price"])
        vals = ["YES" if pd.notna(r.get(f"{h}_predicted_price")) and float(r[f"{h}_predicted_price"]) >= float(r["purchase_price"]) else "-" for h in ("3M","6M","9M","12M","18M","24M","36M")]
        first = str(r["first_forecast_horizon_at_or_above_purchase_price"])
        recovery.append(f"{i:>5} | {symbol:<10} | {avg:>9} | " + " | ".join(f"{v:>9}" for v in vals) + f" | {first:<6}")
    recovery += ["</pre>", "YES = forecast reaches/exceeds configured average cost at that horizon. First = earliest model horizon; not a guaranteed date."]
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
                "Index | Stock      | Current   | -5%       | -10%      | -15%      | -20%",
                "------|------------|-----------|-----------|-----------|-----------|-----------",
            ]
            for i, (_, r) in enumerate(df.iterrows(), 1):
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

            plan = [
                "🧮 <b>AVERAGING → FORECAST BREAK-EVEN</b>",
                "",
                "<pre>",
                "Index | Stock      | Buy Now   | Horizon | Add Qty    | New Avg   | Capital",
                "------|------------|-----------|---------|------------|-----------|-----------",
            ]
            for i, (_, r) in enumerate(df.iterrows(), 1):
                best = None
                for h in ("3M","6M","9M","12M","18M","24M","36M"):
                    q = r.get(f"{h}_break_even_additional_qty_at_current")
                    p = r.get(f"{h}_predicted_price")
                    if pd.notna(q) and pd.notna(p) and float(q) > 0:
                        best = (h, float(q), float(p))
                        break
                if best is None:
                    plan.append(f"{i:>5} | {str(r['symbol'])[:10]:<10} | {money(r['current_price']):>9} | {'-':<7} | {'-':>10} | {'-':>9} | {'-':>9}")
                else:
                    h,q,p=best
                    plan.append(f"{i:>5} | {str(r['symbol'])[:10]:<10} | {money(r['current_price']):>9} | {h:<7} | {q:>10.0f} | {money(p):>9} | {money(q*float(r['current_price'])):>9}")
            plan += ["</pre>", "This is break-even arithmetic at the current price, not a buy recommendation or profit guarantee."]
            send_message(token, chat_id, "\n".join(plan))

    if DIVIDENDS.exists():
        div = pd.read_csv(DIVIDENDS)
        if not div.empty:
            msg = [
                "💰 <b>DIVIDEND OPPORTUNITIES</b>",
                "",
                "<pre>",
                "Index | Stock      | Div/SH   | Ex-Date    | Buy-By     | Yield",
                "------|------------|----------|------------|------------|-------",
            ]
            for i, (_, r) in enumerate(div.sort_values("ex_date").iterrows(), 1):
                sym = str(r["symbol"])[:10]
                ds = money(r["dividend_per_share"]).replace("₹", "")
                y = pct(r["dividend_yield"])
                msg.append(f"{i:>5} | {sym:<10} | {ds:>8} | {str(r['ex_date']):<10} | {str(r['cum_date']):<10} | {y:>7}")
            msg += ["</pre>", "Buy-by = cum-dividend date for dividend eligibility; not a price prediction."]
            send_message(token, chat_id, "\n".join(msg))

    if DIV_HISTORY.exists():
        dh = pd.read_csv(DIV_HISTORY)
        if not dh.empty:
            g = dh.groupby(["symbol", "name"], as_index=False).agg(
                ex_day_return=("ex_day_return", "mean"),
                recovery_days=("recovery_days", "mean"),
                total_return_5d=("total_return_5d_including_dividend", "mean"),
            )
            msg = [
                "📈 <b>DIVIDEND HISTORY</b>",
                "",
                "<pre>",
                "Index | Stock      | Ex-Day    | 5D Total  | Recovery",
                "------|------------|-----------|-----------|---------",
            ]
            for i, (_, r) in enumerate(g.iterrows(), 1):
                day = "-" if pd.isna(r["recovery_days"]) else f"{float(r['recovery_days']):.0f}d"
                msg.append(f"{i:>5} | {str(r['symbol'])[:10]:<10} | {pct(r['ex_day_return']):>9} | {pct(r['total_return_5d']):>9} | {day:>9}")
            msg += ["</pre>", "Historical averages only; past dividend behaviour does not predict future price moves."]
            send_message(token, chat_id, "\n".join(msg))


    if DIV_CAPTURE_SUMMARY.exists():
        cs = pd.read_csv(DIV_CAPTURE_SUMMARY)
        if not cs.empty:
            msg = [
                "🧪 <b>NIFTY 500 DIVIDEND CAPTURE BACKTEST</b>",
                "",
                "<pre>",
                "Index | Exit | Events | Win %   | Avg Total | Worst",
                "------|------|--------|---------|-----------|-------",
            ]
            for i, (_, r) in enumerate(cs.iterrows(), 1):
                msg.append(
                    f"{int(r['exit_days']):>3}d "
                    f"{int(r['events']):>7} "
                    f"{float(r['win_rate'])*100:>6.1f}% "
                    f"{float(r['average_total_return'])*100:>10.1f}% "
                    f"{float(r['worst_total_return'])*100:>7.1f}%"
                )
            msg += [
                "</pre>",
                "Historical gross return study across the current Nifty 500 universe; not a buy/sell recommendation.",
            ]
            send_message(token, chat_id, "\n".join(msg))


if __name__ == "__main__":
    main()
