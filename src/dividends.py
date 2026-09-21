from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DIVIDENDS = ROOT / "data" / "dividends.csv"
HISTORICAL = ROOT / "predictions" / "dividend_history.csv"
CAPTURE = ROOT / "predictions" / "dividend_capture_backtest.csv"
CAPTURE_SUMMARY = ROOT / "predictions" / "dividend_capture_summary.csv"

NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}

def _nse_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(NSE_HEADERS)
    r = s.get("https://www.nseindia.com/", timeout=20)
    r.raise_for_status()
    return s

def _nse_symbol(symbol: str) -> str:
    return str(symbol).removesuffix(".NS").upper()

def _amount(text: str) -> float | None:
    # NSE usually returns "Dividend - Rs 5"; BSE may return
    # "Dividend - Rs. - 5.0000". Accept both forms.
    m = re.search(
        r"(?:Rs\.?|Re\.?|INR)\s*[-:]?\s*([0-9]+(?:\.[0-9]+)?)",
        str(text),
        re.I,
    )
    if m:
        return float(m.group(1))
    return None

def _bse_corporate_actions(from_date: pd.Timestamp, to_date: pd.Timestamp) -> list[dict]:
    """Fallback for GitHub Actions/cloud IPs blocked by NSE.

    BSE exposes forthcoming corporate actions through its public JSON endpoint.
    """
    url = "https://api.bseindia.com/BseIndiaAPI/api/DefaultData/w"
    params = {
        "Fdate": from_date.strftime("%Y%m%d"),
        "TDate": to_date.strftime("%Y%m%d"),
        "ddlcategorys": "E",
        "ddlindustrys": "",
        "scripcode": "",
        "segment": "0",
        "strSearch": "S",
        "Purposecode": "P9",  # dividend
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.bseindia.com/",
        "Origin": "https://www.bseindia.com",
    }
    r = requests.get(url, params=params, headers=headers, timeout=60)
    r.raise_for_status()
    payload = r.json()
    if isinstance(payload, dict):
        for key in ("Table", "data", "Data"):
            if isinstance(payload.get(key), list):
                return payload[key]
        return []
    if isinstance(payload, list):
        return payload
    raise RuntimeError(f"Unexpected BSE corporate-actions response: {type(payload).__name__}")

def _parse_nse_date(value):
    if value is None or pd.isna(value):
        return pd.NaT
    text = str(value).strip()
    for fmt in ("%d-%b-%Y", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return pd.Timestamp(datetime.strptime(text, fmt))
        except (ValueError, TypeError):
            pass
    return pd.to_datetime(text, errors="coerce", dayfirst=True)

def nifty500_universe() -> pd.DataFrame:
    s = _nse_session()
    r = s.get("https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500", timeout=30)
    r.raise_for_status()
    rows = []
    for item in r.json().get("data", []):
        symbol = str(item.get("symbol", "")).strip()
        if symbol and symbol != "NIFTY 500":
            rows.append({"symbol":f"{symbol}.NS","nse_symbol":symbol,"name":item.get("meta",{}).get("companyName") or symbol,"current_price":item.get("lastPrice")})
    result = pd.DataFrame(rows).drop_duplicates("symbol")
    if result.empty:
        raise RuntimeError("NSE returned an empty Nifty 500 universe")
    return result

def _nse_corporate_actions(from_date: pd.Timestamp, to_date: pd.Timestamp) -> list[dict]:
    s = _nse_session()
    url=("https://www.nseindia.com/api/corporates-corporateActions"
         f"?index=equities&from_date={from_date.strftime('%d-%m-%Y')}&to_date={to_date.strftime('%d-%m-%Y')}")
    r=s.get(url,timeout=60)
    r.raise_for_status()
    payload=r.json()
    if not isinstance(payload,list):
        raise RuntimeError(f"Unexpected NSE corporate-actions response: {type(payload).__name__}")
    return payload

def fetch_upcoming_dividends(stocks: pd.DataFrame, prices: dict[str,float]|None=None) -> pd.DataFrame:
    today=pd.Timestamp.now(tz="Asia/Kolkata").tz_localize(None).normalize()
    end=today+pd.Timedelta(days=120)
    prices=prices or {}
    portfolio_symbols={_nse_symbol(x) for x in stocks["symbol"].astype(str)}
    stock_meta=stocks.set_index("symbol").to_dict("index")
    rows=[]
    source_label = "NSE corporate actions JSON"
    try:
        actions = _nse_corporate_actions(today, end)
    except Exception as nse_exc:
        print(f"NSE corporate actions unavailable; using BSE fallback: {nse_exc}")
        actions = _bse_corporate_actions(today, end)
        source_label = "BSE corporate actions JSON fallback"

    for action in actions:
        nse_symbol = _nse_symbol(action.get("symbol") or action.get("short_name") or "")
        subject = str(action.get("subject") or action.get("Purpose") or "")
        if nse_symbol not in portfolio_symbols or "DIVIDEND" not in subject.upper():
            continue
        ex = _parse_nse_date(action.get("exDate") or action.get("Ex_date") or action.get("exdate"))
        if pd.isna(ex) or ex.normalize() < today:
            continue
        record = _parse_nse_date(action.get("recDate") or action.get("RD_Date"))
        if pd.isna(record): record=ex
        div=_amount(subject)
        symbol=f"{nse_symbol}.NS"
        price=prices.get(symbol)
        buy_by=ex-pd.offsets.BDay(1)
        rows.append({
            "symbol":symbol,"name":stock_meta.get(symbol,{}).get("name",nse_symbol),
            "universe":"PORTFOLIO","dividend_per_share":div,"announcement_date":pd.NA,
            "ex_date":ex.date().isoformat(),"record_date":record.date().isoformat(),
            "cum_date":buy_by.date().isoformat(),"current_price":price,
            "dividend_yield":(float(div)/float(price) if div is not None and price and float(price)>0 else pd.NA),
            "status":"UPCOMING","source":source_label,
        })
    result=pd.DataFrame(rows)
    if not result.empty:
        result=result.drop_duplicates(["symbol","ex_date","dividend_per_share"]).sort_values(["ex_date","symbol"])
    DIVIDENDS.parent.mkdir(parents=True,exist_ok=True)
    if result.empty and DIVIDENDS.exists():
        old=pd.read_csv(DIVIDENDS)
        if not old.empty and "ex_date" in old.columns:
            old["_ex"]=pd.to_datetime(old["ex_date"],errors="coerce")
            old=old[old["_ex"].notna()&(old["_ex"]>=today)].drop(columns=["_ex"])
            if not old.empty: return old
    result.to_csv(DIVIDENDS,index=False)
    return result

def historical_dividend_patterns(stocks: pd.DataFrame) -> pd.DataFrame:
    rows=[]
    for stock in stocks.to_dict("records"):
        symbol=stock["symbol"]
        try:
            tk=yf.Ticker(symbol); divs=tk.dividends
            if divs is None or divs.empty: continue
            divs.index=pd.to_datetime(divs.index).tz_localize(None)
            prices=tk.history(period="10y",auto_adjust=False,actions=False)
            if prices.empty: continue
            close=prices["Close"].dropna(); idx=close.index
            for ex_date,div in divs.items():
                pos=idx.searchsorted(ex_date)
                if pos>=len(idx) or pos==0: continue
                pre=float(close.iloc[pos-1]); ex_close=float(close.iloc[pos])
                def ret(days):
                    return float(close.iloc[min(pos+days,len(close)-1)]/pre-1)
                recovery=None
                for j in range(pos+1,len(close)):
                    if float(close.iloc[j])>=pre: recovery=j-pos; break
                rows.append({"symbol":symbol,"name":stock["name"],"ex_date":idx[pos].date().isoformat(),
                    "dividend_per_share":float(div),"pre_div_10d_return":float(close.iloc[pos-1]/close.iloc[max(0,pos-11)]-1) if pos>=11 else pd.NA,
                    "ex_day_return":float(ex_close/pre-1),"post_3d_return":ret(3),"post_5d_return":ret(5),
                    "post_10d_return":ret(10),"post_20d_return":ret(20),"recovery_days":recovery if recovery is not None else pd.NA,
                    "dividend_yield_on_pre_close":float(div/pre) if pre else pd.NA,
                    "total_return_5d_including_dividend":float(close.iloc[min(pos+5,len(close)-1)]/pre-1+div/pre) if pre else pd.NA})
        except Exception as exc:
            print(f"Historical dividend analysis failed for {symbol}: {exc}")
    result=pd.DataFrame(rows)
    if not result.empty: result.to_csv(HISTORICAL,index=False)
    elif not HISTORICAL.exists(): pd.DataFrame().to_csv(HISTORICAL,index=False)
    return result

def nifty500_dividend_capture_backtest(universe: pd.DataFrame, period: str="10y") -> tuple[pd.DataFrame,pd.DataFrame]:
    symbols=[s for s in universe["symbol"].dropna().astype(str).unique()]
    if not symbols: return pd.DataFrame(),pd.DataFrame()
    try:
        raw=yf.download(symbols,period=period,auto_adjust=False,actions=True,progress=False,threads=True,group_by="column")
    except Exception as exc:
        print(f"Nifty 500 dividend backtest download failed: {exc}"); return pd.DataFrame(),pd.DataFrame()
    if raw.empty: return pd.DataFrame(),pd.DataFrame()
    def series(field,symbol):
        try:
            if isinstance(raw.columns,pd.MultiIndex):
                if field in raw.columns.get_level_values(0): return raw[field][symbol] if symbol in raw[field].columns else pd.Series(dtype=float)
                if field in raw.columns.get_level_values(1): return raw[symbol][field] if symbol in raw[symbol].columns else pd.Series(dtype=float)
            return raw[field] if field in raw.columns else pd.Series(dtype=float)
        except Exception: return pd.Series(dtype=float)
    name_map=universe.set_index("symbol")["name"].to_dict(); rows=[]
    for symbol in symbols:
        close=pd.to_numeric(series("Close",symbol),errors="coerce").dropna()
        dividends=pd.to_numeric(series("Dividends",symbol),errors="coerce").fillna(0.0)
        if close.empty or dividends.empty: continue
        close.index=pd.to_datetime(close.index).tz_localize(None); dividends.index=pd.to_datetime(dividends.index).tz_localize(None)
        dividends=dividends.reindex(close.index).fillna(0.0)
        for ex_date in dividends[dividends>0].index:
            pos=close.index.searchsorted(ex_date)
            if pos<=0 or pos>=len(close): continue
            buy_date=close.index[pos-1]; buy_price=float(close.iloc[pos-1]); div=float(dividends.loc[ex_date])
            if buy_price<=0: continue
            for days in (1,3,5,10,20):
                exit_pos=pos+days
                if exit_pos>=len(close): continue
                sell_price=float(close.iloc[exit_pos]); price_return=sell_price/buy_price-1.0; dividend_return=div/buy_price; total_return=price_return+dividend_return
                rows.append({"symbol":symbol,"name":name_map.get(symbol,symbol),"ex_date":ex_date.date().isoformat(),"buy_date":buy_date.date().isoformat(),"buy_price":buy_price,"dividend_per_share":div,"exit_days":days,"exit_date":close.index[exit_pos].date().isoformat(),"sell_price":sell_price,"price_return":price_return,"dividend_return":dividend_return,"total_return":total_return,"profitable":total_return>0})
    result=pd.DataFrame(rows)
    if result.empty: return result,pd.DataFrame()
    summary=result.groupby("exit_days",as_index=False).agg(events=("total_return","size"),win_rate=("profitable","mean"),average_total_return=("total_return","mean"),median_total_return=("total_return","median"),worst_total_return=("total_return","min"),best_total_return=("total_return","max"),average_price_return=("price_return","mean"),average_dividend_return=("dividend_return","mean")).sort_values("exit_days")
    CAPTURE.parent.mkdir(parents=True,exist_ok=True); result.to_csv(CAPTURE,index=False); summary.to_csv(CAPTURE_SUMMARY,index=False)
    return result,summary

def update_dividends(stocks: pd.DataFrame, prices: dict[str,float]) -> tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    upcoming=fetch_upcoming_dividends(stocks,prices); historical=historical_dividend_patterns(stocks)
    try:
        universe=nifty500_universe(); capture,summary=nifty500_dividend_capture_backtest(universe)
        print(f"Nifty 500 dividend capture backtest: {len(capture)} rows, {len(summary)} horizons")
    except Exception as exc:
        print(f"Nifty 500 dividend capture backtest unavailable: {exc}"); capture,summary=pd.DataFrame(),pd.DataFrame()
    return upcoming,historical,summary
