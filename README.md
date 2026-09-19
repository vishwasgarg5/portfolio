# Portfolio Forecast & Averaging Report

This repository produces a report, not an app or dashboard.

It uses portfolio quantity and purchase price, historical OHLCV data and out-of-sample model forecasts to produce:
- 3M, 6M, 9M and 12M predicted prices
- forecast-vs-actual tracking and walk-forward backtesting
- current profit/loss relative to purchase price
- first forecast horizon at or above purchase price
- averaging scenarios showing additional quantity and capital needed to reduce average cost

## Required portfolio input

config/stocks.csv contains the 15 holdings and quantities. purchase_price must contain the actual per-share purchase price from the user's portfolio screenshot. Do not invent or estimate this field.

## Run

pip install -r requirements.txt
python scripts/update_forecasts.py

Outputs:
- predictions/latest.csv
- predictions/backtest.csv
- predictions/history.csv
- predictions/portfolio_report.csv
- predictions/portfolio_report.md

The first forecast horizon at or above purchase price is only the first model point estimate among 3M/6M/9M/12M. It is not a guaranteed date.

Averaging calculations are mathematical scenarios showing how adding shares at a specified price changes weighted average cost. They are not a recommendation to buy.
