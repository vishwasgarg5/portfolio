# Portfolio AI Forecast

A free, open-source portfolio forecasting dashboard for Indian equities.

## Goals

- Track the user's portfolio stocks.
- Download/update historical OHLCV data automatically.
- Create technical and market features.
- Produce 3M, 6M, 9M and 12M model forecasts.
- Store each forecast so it can later be compared with the actual price.
- Report prediction error by horizon.
- Show expected return and a forecast range rather than a single number.
- Improve/calibrate the model from out-of-sample historical errors.

> Forecasts are statistical model estimates, not guaranteed future prices or investment advice.

## Current stack

- Python
- Streamlit
- yfinance
- pandas / NumPy
- scikit-learn
- Plotly
- GitHub Actions for scheduled data/model updates

## Project structure

~~~~
portfolio/
├── app.py
├── config/
│   └── stocks.csv
├── data/
│   └── .gitkeep
├── predictions/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── pipeline.py
├── scripts/
│   └── update_forecasts.py
├── tests/
│   └── test_features.py
├── .github/
│   └── workflows/
│       └── update-forecasts.yml
├── requirements.txt
└── .gitignore
~~~~

## Run locally

~~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/update_forecasts.py
streamlit run app.py
~~~~

On Windows PowerShell:

~~~~powershell
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
~~~~

## Forecast methodology

The first model is deliberately conservative and reproducible:

1. Historical daily OHLCV is downloaded with yfinance.
2. Technical features are generated using only information available on or before each observation.
3. Separate regression models are trained for 3M/6M/9M/12M forward returns.
4. Time-ordered validation is used instead of random train/test splitting.
5. The latest row is passed to the trained model to create the current forecast.
6. Historical forecasts are retained so future runs can calculate prediction-vs-actual errors.

The initial implementation uses scikit-learn's HistGradientBoostingRegressor, avoiding paid APIs or proprietary model services. Each horizon is evaluated independently: newer stocks can receive forecasts for horizons with enough labelled history, while unavailable long horizons are explicitly marked as insufficient history instead of failing the whole stock. Forecast confidence is also shown as a descriptive history-size indicator, not a probability of success.

## Important limitation

Long-horizon stock forecasting is intrinsically uncertain. A forecast should be evaluated by out-of-sample error and calibration over time. The application therefore exposes historical model performance rather than presenting a forecast as a certainty.
