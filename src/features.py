from __future__ import annotations

import numpy as np
import pandas as pd


HORIZONS = {
    "3M": 63,
    "6M": 126,
    "9M": 189,
    "12M": 252,
}


def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period, min_periods=max(5, period // 2)).mean()
    loss = -delta.clip(upper=0).rolling(period, min_periods=max(5, period // 2)).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def make_features(price: pd.DataFrame) -> pd.DataFrame:
    df = price.copy().sort_index()
    close = df["Close"]
    volume = df["Volume"].replace(0, np.nan)

    out = df.copy()
    out["return_1d"] = close.pct_change()
    out["return_5d"] = close.pct_change(5)
    out["return_20d"] = close.pct_change(20)
    out["return_60d"] = close.pct_change(60)

    for n in (5, 10, 20, 50, 100, 200):
        ma = close.rolling(n, min_periods=min(n, 20)).mean()
        out[f"ma_ratio_{n}"] = close / ma - 1
        out[f"volatility_{n}"] = close.pct_change().rolling(n, min_periods=min(n, 20)).std()

    out["rsi_14"] = _rsi(close)
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    out["macd"] = ema12 - ema26
    out["macd_signal"] = out["macd"].ewm(span=9, adjust=False).mean()

    mid = close.rolling(20, min_periods=10).mean()
    std = close.rolling(20, min_periods=10).std()
    out["bb_position"] = (close - (mid - 2 * std)) / (4 * std)

    out["atr_pct"] = (
        pd.concat(
            [
                df["High"] - df["Low"],
                (df["High"] - close.shift()).abs(),
                (df["Low"] - close.shift()).abs(),
            ],
            axis=1,
        )
        .max(axis=1)
        .rolling(14)
        .mean()
        / close
    )

    out["volume_ratio_20"] = volume / volume.rolling(20, min_periods=10).mean()
    out["high_low_range"] = (df["High"] - df["Low"]) / close

    for label, days in HORIZONS.items():
        out[f"target_{label}"] = close.shift(-days) / close - 1

    return out.replace([np.inf, -np.inf], np.nan)


FEATURE_COLUMNS = [
    "return_1d", "return_5d", "return_20d", "return_60d",
    "ma_ratio_5", "ma_ratio_10", "ma_ratio_20", "ma_ratio_50",
    "ma_ratio_100", "ma_ratio_200",
    "volatility_5", "volatility_20", "volatility_50", "volatility_100",
    "rsi_14", "macd", "macd_signal", "bb_position", "atr_pct",
    "volume_ratio_20", "high_low_range",
]
