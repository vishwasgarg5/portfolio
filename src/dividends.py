from __future__ import annotations

import io
import re
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DIVIDENDS = ROOT / "data" / "dividends.csv"
HISTORICAL = ROOT / "predictions" / "dividend_history.csv"

NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}


def _nse_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(NSE_HEADERS)
    s.get("https://www.nseindia.com/", timeout=20)
    return s


def _nse_symbol(symbol: str) -> str:
    return str(symbol).removesuffix(".NS")


def _amount(text: str) -> float | None:
    m = re.search(r"(?:Rs\.?|Re\.?|INR)\s*([0-9]+(?:\.[0-9]+)?)", str(text), re.I)
    return float(m.group(1)) if m else None


def nifty500_universe() -> pd.DataFrame:
    """Return the current Nifty 500 universe and latest NSE prices."""
    s = _nse_session()
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"
    r = s.get(url, timeout=30)
    r.raise_for_status()
    payload = r.json()
    rows = []
    for item in payload.get("data", []):
        symbol = str(item.get("symbol", "")).strip()
        if not symbol or symbol == "NIFTY 500":
            continue
        rows.append({
            "symbol": f"{symbol}.NS",
            "nse_symbol": symbol,
            "name": item.get("meta", {}).get("companyName") or symbol,
            "current_price": item.get("lastPrice"),
        })
    result = pd.DataFrame(rows).drop_duplicates("symbol")
    if result.empty:
        raise RuntimeError("NSE returned an empty Nifty 500 universe")
    return result


def _nse_all_corporate_actions() -> pd.DataFrame:
    """Fetch NSE's current equity corporate-action CSV in one request."""
    s = _nse_session()
    url = "https://www.nseindia.com/api/corporates-corporateActions?index=equities&csv=true"
    r = s.get(url, timeout=60)
    r.raise_for_status()
    text = r.content.decode("utf-8-sig", errors="replace")
    df = pd.read_csv(io.StringIO(text))
    df.columns = [str(c).strip().upper().replace(" ", "_") for c in df.columns]
    return df


def fetch_upcoming_dividends(stocks: pd.DataFrame, prices: dict[str, float] | None = None) -> pd.DataFrame:
    """Build an upcoming dividend calendar for the whole Nifty 500, not just the portfolio."""
    today = pd.Timestamp.utcnow().tz_localize(None).normalize()
    prices = prices or {}

    universe = nifty500_universe()
    universe_by_nse = universe.set_index("nse_symbol").to_dict("index")

    actions = _nse_all_corporate_actions()
    required = {"SYMBOL", "PURPOSE", "EX_DATE"}
    if not required.issubset(actions.columns):
        raise RuntimeError(f"NSE corporate-action feed missing columns: {required - set(actions.columns)}")

    actions = actions[actions["PURPOSE"].astype(str).str.contains("DIVIDEND", case=False, na=False)].copy()
    actions["ex_date"] = pd.to_datetime(actions["EX_DATE"], errors="coerce", dayfirst=True)
    record_col = "RECORD_DATE" if "RECORD_DATE" in actions.columns else None
    actions["record_date"] = pd.to_datetime(actions[record_col], errors="coerce", dayfirst=True) if record_col else pd.NaT
    actions["dividend_per_share"] = actions["PURPOSE"].map(_amount)
    actions = actions[actions["ex_date"].notna() & (actions["ex_date"] >= today)]
    actions = actions[actions["SYMBOL"].isin(universe_by_nse)]
    rows = []

    for r in actions.to_dict("records"):
        nse_symbol = str(r["SYMBOL"])
        meta = universe_by_nse.get(nse_symbol, {})
        ex = r["ex_date"]
        record = r["record_date"] if pd.notna(r["record_date"]) else ex
        buy_by = ex - pd.offsets.BDay(1)
        symbol = f"{nse_symbol}.NS"
        price = prices.get(symbol, meta.get("current_price"))
        div = r.get("dividend_per_share")
        rows.append({
            "symbol": symbol,
            "name": meta.get("name", nse_symbol),
            "universe": "NIFTY 500",
            "dividend_per_share": div,
            "announcement_date": pd.NA,
            "ex_date": ex.date().isoformat(),
            "record_date": record.date().isoformat() if pd.notna(record) else pd.NA,
            "cum_date": buy_by.date().isoformat(),
            "current_price": price,
            "dividend_yield": (float(div) / float(price)) if pd.notna(div) and price else pd.NA,
            "status": "UPCOMING",
            "source": "NSE corporate actions",
        })

    result = pd.DataFrame(rows)
    if not result.empty:
        result = result.drop_duplicates(["symbol", "ex_date", "dividend_per_share"]).sort_values(["ex_date", "symbol"])

    DIVIDENDS.parent.mkdir(parents=True, exist_ok=True)
    # Never erase the previous calendar just because NSE temporarily returns no rows.
    if result.empty and DIVIDENDS.exists():
        return pd.read_csv(DIVIDENDS)
    result.to_csv(DIVIDENDS, index=False)
    return result


def historical_dividend_patterns(stocks: pd.DataFrame) -> pd.DataFrame:
    """Keep the detailed historical capture study for configured portfolio stocks."""
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
                if pos >= len(idx) or pos == 0:
                    continue
                ex = idx[pos]
                pre = float(close.iloc[pos - 1])
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
                    "pre_div_10d_return": float(close.iloc[pos - 1] / close.iloc[max(0, pos - 11)] - 1) if pos >= 11 else pd.NA,
                    "ex_day_return": float(ex_close / pre - 1),
                    "post_3d_return": ret(3),
                    "post_5d_return": ret(5),
                    "post_10d_return": ret(10),
                    "post_20d_return": ret(20),
                    "recovery_days": recovery if recovery is not None else pd.NA,
                    "dividend_yield_on_pre_close": float(div / pre) if pre else pd.NA,
                    "total_return_5d_including_dividend": float(close.iloc[min(pos + 5, len(close) - 1)] / pre - 1 + div / pre) if pre else pd.NA,
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
