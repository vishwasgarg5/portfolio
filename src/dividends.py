from __future__ import annotations

import re
from io import StringIO
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "stocks.csv"
DIVIDENDS = ROOT / "data" / "dividends.csv"
HISTORICAL = ROOT / "predictions" / "dividend_history.csv"

NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.nseindia.com/",
}

def _nse_symbol(symbol: str) -> str:
    return symbol.removesuffix(".NS")

def _amount(text: str) -> float | None:
    m = re.search(r"(?:Rs\.?|Re\.?|INR)\s*([0-9]+(?:\.[0-9]+)?)", str(text), re.I)
    return float(m.group(1)) if m else None

def _nse_events(symbol: str) -> pd.DataFrame:
    url = f"https://www.nseindia.com/companies-listing/corporate-filings-actions?symbol={_nse_symbol(symbol)}"
    s = requests.Session()
    s.headers.update(NSE_HEADERS)
    s.get("https://www.nseindia.com/", timeout=20)
    r = s.get(url, timeout=20)
    r.raise_for_status()
    tables = pd.read_html(StringIO(r.text))
    if not tables:
        return pd.DataFrame()
    t = next((x for x in tables if "PURPOSE" in x.columns and "EX-DATE" in x.columns), tables[0])
    t.columns = [str(c).strip().upper().replace(" ", "_") for c in t.columns]
    purpose_col = next((c for c in t.columns if "PURPOSE" in c), None)
    if not purpose_col:
        return pd.DataFrame()
    t = t[t[purpose_col].astype(str).str.contains("DIVIDEND", case=False, na=False)].copy()
    if t.empty:
        return pd.DataFrame()
    t["dividend_per_share"] = t[purpose_col].map(_amount)
    t["ex_date"] = pd.to_datetime(t.get("EX-DATE"), errors="coerce", dayfirst=True)
    t["record_date"] = pd.to_datetime(t.get("RECORD_DATE"), errors="coerce", dayfirst=True)
    t["symbol"] = symbol
    t["purpose"] = t[purpose_col].astype(str)
    return t[["symbol", "purpose", "dividend_per_share", "ex_date", "record_date"]]

def fetch_upcoming_dividends(stocks: pd.DataFrame, prices: dict[str, float]) -> pd.DataFrame:
    today = pd.Timestamp.utcnow().tz_localize(None).normalize()
    rows = []
    for stock in stocks.to_dict("records"):
        symbol = stock["symbol"]
        try:
            t = _nse_events(symbol)
            if t.empty:
                continue
            for r in t.to_dict("records"):
                ex = r["ex_date"]
                if pd.isna(ex) or ex < today:
                    continue
                record = r["record_date"] if pd.notna(r["record_date"]) else ex
                # NSE describes cum-dividend as the last date to buy for eligibility;
                # for normal equity dividends this is the prior working/trading day.
                buy_by = ex - pd.offsets.BDay(1)
                price = prices.get(symbol)
                div = r["dividend_per_share"]
                rows.append({
                    "symbol": symbol,
                    "name": stock["name"],
                    "dividend_per_share": div,
                    "announcement_date": pd.NA,
                    "ex_date": ex.date().isoformat(),
                    "record_date": record.date().isoformat() if pd.notna(record) else pd.NA,
                    "cum_date": buy_by.date().isoformat(),
                    "current_price": price,
                    "dividend_yield": (div / price) if div is not None and price else pd.NA,
                    "status": "UPCOMING",
                    "source": "NSE corporate actions",
                })
        except Exception as exc:
            print(f"Dividend lookup failed for {symbol}: {exc}")
    result = pd.DataFrame(rows)
    if not result.empty:
        result = result.drop_duplicates(["symbol", "ex_date", "dividend_per_share"]).sort_values(["ex_date", "symbol"])
    DIVIDENDS.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(DIVIDENDS, index=False)
    return result

def historical_dividend_patterns(stocks: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for stock in stocks.to_dict("records"):
        symbol = stock["symbol"]
        try:
            tk = yf.Ticker(symbol)
            divs = tk.dividends
            if divs is None or divs.empty:
                continue
            divs.index = pd.to_datetime(divs.index).tz_localize(None)
            prices = tk.history(period="10y", auto_adjust=False, actions=False)
            if prices.empty:
                continue
            close = prices["Close"].dropna()
            idx = close.index
            for ex_date, div in divs.items():
                pos = idx.searchsorted(ex_date)
                if pos >= len(idx):
                    continue
                ex = idx[pos]
                pre_pos = pos - 1
                if pre_pos < 0:
                    continue
                pre = float(close.iloc[pre_pos])
                ex_close = float(close.iloc[pos])
                def ret(days):
                    j = min(pos + days, len(close) - 1)
                    return float(close.iloc[j] / pre - 1)
                recovery = None
                for j in range(pos + 1, len(close)):
                    if float(close.iloc[j]) >= pre:
                        recovery = j - pos
                        break
                rows.append({
                    "symbol": symbol,
                    "name": stock["name"],
                    "ex_date": ex.date().isoformat(),
                    "dividend_per_share": float(div),
                    "pre_div_10d_return": float(close.iloc[pre_pos] / close.iloc[max(0, pre_pos-10)] - 1) if pre_pos >= 10 else pd.NA,
                    "ex_day_return": float(ex_close / pre - 1),
                    "post_3d_return": ret(3),
                    "post_5d_return": ret(5),
                    "post_10d_return": ret(10),
                    "post_20d_return": ret(20),
                    "recovery_days": recovery if recovery is not None else pd.NA,
                    "dividend_yield_on_pre_close": float(div / pre) if pre else pd.NA,
                    "total_return_5d_including_dividend": float(ex_close / pre - 1 + div / pre) if pre else pd.NA,
                })
        except Exception as exc:
            print(f"Historical dividend analysis failed for {symbol}: {exc}")
    result = pd.DataFrame(rows)
    if not result.empty:
        result.to_csv(HISTORICAL, index=False)
    elif not HISTORICAL.exists():
        pd.DataFrame().to_csv(HISTORICAL, index=False)
    return result

def update_dividends(stocks: pd.DataFrame, prices: dict[str, float]) -> tuple[pd.DataFrame, pd.DataFrame]:
    upcoming = fetch_upcoming_dividends(stocks, prices)
    historical = historical_dividend_patterns(stocks)
    return upcoming, historical
