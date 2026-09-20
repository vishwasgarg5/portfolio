from __future__ import annotations
from pathlib import Path
import pandas as pd
import yfinance as yf
ROOT=Path(__file__).resolve().parents[1]; DATA_DIR=ROOT/"data"

def _normalise_columns(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns,pd.MultiIndex): df.columns=[c[0] if isinstance(c,tuple) else c for c in df.columns]
    df=df.rename(columns={str(c).strip().title():str(c).strip().title() for c in df.columns})
    needed=["Open","High","Low","Close","Volume"]; missing=[c for c in needed if c not in df.columns]
    if missing: raise ValueError(f"Missing market columns: {missing}")
    out=df[needed].copy();out.index=pd.to_datetime(out.index,errors="coerce")
    if getattr(out.index,"tz",None) is not None: out.index=out.index.tz_localize(None)
    out=out[~out.index.isna()];out=out[~out.index.duplicated(keep="last")].sort_index()
    return out.dropna(subset=["Close"])

def download_history(symbol:str,years:int=10)->pd.DataFrame:
    df=yf.download(symbol,period=f"{years}y",interval="1d",auto_adjust=True,progress=False,threads=False)
    if df.empty: raise ValueError(f"No market data returned for {symbol}")
    return _normalise_columns(df)

def update_history(symbol:str,years:int=10)->pd.DataFrame:
    DATA_DIR.mkdir(parents=True,exist_ok=True);path=DATA_DIR/f"{symbol.replace('.','_')}.csv"
    fresh=download_history(symbol,years)
    if path.exists():
        old=_normalise_columns(pd.read_csv(path,index_col=0,parse_dates=True))
        combined=pd.concat([old,fresh]).sort_index();combined=combined[~combined.index.duplicated(keep="last")]
    else: combined=fresh
    combined.to_csv(path);return combined

def load_history(symbol:str)->pd.DataFrame:
    path=DATA_DIR/f"{symbol.replace('.','_')}.csv"
    if not path.exists(): return update_history(symbol)
    return _normalise_columns(pd.read_csv(path,index_col=0,parse_dates=True))

def update_benchmark(years:int=10)->pd.DataFrame:
    return update_history("^NSEI",years)

def load_benchmark()->pd.DataFrame:
    return load_history("^NSEI")
