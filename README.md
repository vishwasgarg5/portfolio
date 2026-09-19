# Portfolio Forecast & Averaging Report

This repository produces a **report**, not an app or dashboard.

## What it does

For the 15 portfolio holdings it:
- stores the quantity and purchase price extracted from the portfolio screenshot
- downloads/updates historical OHLCV data
- adds technical, NIFTY 50 regime and relative-strength features
- trains separate 3M, 6M, 9M and 12M return forecasts
- compares HistGradientBoosting, ExtraTrees and a zero-return baseline on chronological holdout data
- performs leakage-safe walk-forward backtesting with model selection inside each historical fold
- calibrates forecasts using completed real forecast errors for the same stock/horizon when enough exist, otherwise walk-forward errors
- builds empirical historical-error bands
- records every forecast and later compares it with the actual price
- records whether the actual evaluated price reached the purchase-price break-even level
- calculates current P/L and forecast-horizon P/L
- calculates averaging quantities/capital at the current price and at 5%, 10%, 15% and 20% lower hypothetical prices

NIFTY 50 benchmark data uses Yahoo Finance symbol ^NSEI. If benchmark data is temporarily unavailable, the stock model still runs without those benchmark features.

## Outputs

- predictions/latest.csv — latest forecasts and model-selection details
- predictions/backtest.csv — walk-forward metrics and historical error bands
- predictions/history.csv — forecast-to-actual tracking and break-even outcomes
- predictions/portfolio_report.csv — portfolio P/L and forecast analysis
- predictions/portfolio_report.md — readable report
- predictions/averaging_scenarios.csv — averaging stress-test calculations

## Automatic retraining

The scheduled GitHub Actions workflow runs on weekdays around 18:15 IST:
1. downloads the newest stock and NIFTY data
2. rebuilds features
3. retrains the forecasting models from the updated history
4. runs walk-forward validation
5. calibrates using completed historical forecast errors
6. generates the new portfolio and averaging reports
7. commits updated CSV/Markdown outputs

No model is assumed to be permanently correct. Historical accuracy is continuously measured.

## Important interpretation

A forecast is an estimate, not a guarantee. A forecast horizon reaching the purchase price means the model's point estimate is at/above that price; it is not a guaranteed date.

Averaging calculations are mathematical cost-basis scenarios. They do not determine whether an additional purchase is appropriate.
