# Portfolio forecast report

Models retrain from the latest market history on every scheduled run.
The selected model is chosen using chronological holdout error, with a zero-return baseline included.
Forecast calibration uses completed real forecast errors for the same stock/horizon when available, then walk-forward errors.
Error bands are empirical historical-error bands, not guarantees.
Averaging plans require medium/high model confidence, validation MAE <= 20%, error band <= 30%, a conservative lower-forecast profit check, and no severe 20-day deterioration.
Portfolio-wide additional averaging capital is capped at 20% of configured invested cost; each stock is capped at 50%.
Forecast horizons marked unavailable have insufficient labelled historical data and are not treated as failed forecasts.
The first forecast horizon is a model checkpoint, not a guaranteed date.
Averaging scenarios are mathematical cost-basis calculations. The profit-signal table is a model-generated scenario, not a guarantee or personalized financial advice.

## Vedanta Iron & Steel (VISL.NS)
- Quantity: 1000.0
- Purchase price: 31.84
- Current price: 26.63999938964844
- Current P/L: ₹-5200.00
- First forecast horizon at/above purchase price: Unavailable: insufficient history

- 3M: N/A — Insufficient history for target_3M: 0 labelled rows < 80
- 6M: N/A — Insufficient history for target_6M: 0 labelled rows < 80
- 9M: N/A — Insufficient history for target_9M: 0 labelled rows < 80
- 12M: N/A — Insufficient history for target_12M: 0 labelled rows < 80
- 18M: N/A — Insufficient history for target_18M: 0 labelled rows < 80
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Yes Bank (YESBANK.NS)
- Quantity: 902.0
- Purchase price: 23.57
- Current price: 17.030000686645508
- Current P/L: ₹-5899.08
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹16.99 | model=historical_median | error band=±17.82%
- 6M: ₹16.70 | model=historical_median | error band=±14.99%
- 9M: ₹16.30 | model=historical_median | error band=±23.03%
- 12M: ₹17.41 | model=extra_trees | error band=±21.61%
- 18M: ₹13.10 | model=historical_median | error band=±22.04%
- 24M: ₹14.22 | model=extra_trees | error band=±13.24%
- 36M: ₹5.21 | model=hist | error band=±16.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1324.4000244140625
- Current P/L: ₹-26.26
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1341.29 | model=historical_median | error band=±14.10%
- 6M: ₹1371.88 | model=historical_median | error band=±21.97%
- 9M: ₹1322.66 | model=hist | error band=±25.66%
- 12M: ₹1682.87 | model=hist | error band=±26.03%
- 18M: ₹1735.29 | model=hist | error band=±33.73%
- 24M: ₹1712.22 | model=extra_trees | error band=±37.58%
- 36M: ₹2382.30 | model=historical_median | error band=±43.29%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 328.75
- Current P/L: ₹-999.18
- First forecast horizon at/above purchase price: 12M

- 3M: ₹339.47 | model=historical_median | error band=±15.12%
- 6M: ₹354.48 | model=historical_median | error band=±23.03%
- 9M: ₹361.58 | model=historical_median | error band=±18.26%
- 12M: ₹375.06 | model=historical_median | error band=±18.93%
- 18M: ₹434.87 | model=historical_median | error band=±23.16%
- 24M: ₹439.87 | model=historical_median | error band=±50.11%
- 36M: ₹515.99 | model=historical_median | error band=±63.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 119.6500015258789
- Current P/L: ₹-1697.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹99.40 | model=extra_trees | error band=±5.99%
- 6M: ₹96.25 | model=hist | error band=±9.02%
- 9M: ₹85.58 | model=extra_trees | error band=±2.25%
- 12M: ₹88.37 | model=historical_median | error band=±2.65%
- 18M: ₹67.92 | model=hist | error band=±3.88%
- 24M: ₹63.99 | model=extra_trees | error band=±7.16%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 83.5
- Current P/L: ₹-1442.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹69.87 | model=hist | error band=±12.89%
- 6M: ₹69.74 | model=hist | error band=±30.77%
- 9M: ₹64.18 | model=hist | error band=±59.58%
- 12M: ₹61.99 | model=hist | error band=±74.00%
- 18M: ₹165.04 | model=historical_median | error band=±206.28%
- 24M: ₹142.68 | model=hist | error band=±57.02%
- 36M: ₹664.71 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 360.0
- Current P/L: ₹-5442.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹365.73 | model=historical_median | error band=±12.16%
- 6M: ₹369.30 | model=historical_median | error band=±17.04%
- 9M: ₹368.97 | model=historical_median | error band=±14.33%
- 12M: ₹367.09 | model=historical_median | error band=±17.45%
- 18M: ₹483.88 | model=historical_median | error band=±43.39%
- 24M: ₹590.32 | model=historical_median | error band=±79.04%
- 36M: ₹526.22 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 199.0
- Current P/L: ₹-6575.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹190.74 | model=extra_trees | error band=±9.56%
- 6M: ₹182.91 | model=extra_trees | error band=±21.50%
- 9M: ₹173.72 | model=extra_trees | error band=±27.77%
- 12M: ₹185.73 | model=extra_trees | error band=±24.50%
- 18M: ₹183.19 | model=hist | error band=±29.78%
- 24M: ₹259.28 | model=historical_median | error band=±45.45%
- 36M: ₹278.32 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.83999633789062
- Current P/L: ₹-10473.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹81.80 | model=historical_median | error band=±18.12%
- 6M: ₹83.03 | model=extra_trees | error band=±16.41%
- 9M: ₹72.30 | model=extra_trees | error band=±26.21%
- 12M: ₹78.25 | model=extra_trees | error band=±40.49%
- 18M: ₹151.23 | model=hist | error band=±38.65%
- 24M: ₹136.25 | model=hist | error band=±66.34%
- 36M: ₹164.49 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 33.959999084472656
- Current P/L: ₹-47518.24
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.30 | model=historical_median | error band=±12.25%
- 6M: ₹24.55 | model=extra_trees | error band=±16.51%
- 9M: ₹22.38 | model=hist | error band=±9.69%
- 12M: ₹23.27 | model=historical_median | error band=±4.71%
- 18M: ₹17.38 | model=hist | error band=±4.54%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 176.0800018310547
- Current P/L: ₹-8128.72
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.16 | model=historical_median | error band=±20.77%
- 6M: ₹164.17 | model=extra_trees | error band=±20.87%
- 9M: ₹179.47 | model=historical_median | error band=±23.71%
- 12M: ₹181.32 | model=historical_median | error band=±16.77%
- 18M: ₹200.09 | model=historical_median | error band=±29.46%
- 24M: ₹290.31 | model=extra_trees | error band=±28.44%
- 36M: ₹242.36 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 57.720001220703125
- Current P/L: ₹-3577.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹51.91 | model=extra_trees | error band=±17.98%
- 6M: ₹55.92 | model=historical_median | error band=±29.42%
- 9M: ₹56.57 | model=historical_median | error band=±34.89%
- 12M: ₹57.96 | model=historical_median | error band=±42.65%
- 18M: ₹65.17 | model=historical_median | error band=±66.42%
- 24M: ₹73.63 | model=historical_median | error band=±86.22%
- 36M: ₹102.01 | model=historical_median | error band=±95.19%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.799999237060547
- Current P/L: ₹-47722.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.81 | model=historical_median | error band=±31.94%
- 6M: ₹18.16 | model=historical_median | error band=±27.39%
- 9M: ₹17.51 | model=historical_median | error band=±45.34%
- 12M: ₹18.85 | model=historical_median | error band=±61.50%
- 18M: ₹21.89 | model=historical_median | error band=±129.72%
- 24M: ₹21.79 | model=hist | error band=±99.85%
- 36M: ₹44.33 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 459.9500122070313
- Current P/L: ₹-27672.65
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹438.10 | model=extra_trees | error band=±14.99%
- 6M: ₹446.78 | model=historical_median | error band=±21.31%
- 9M: ₹449.35 | model=historical_median | error band=±32.40%
- 12M: ₹512.77 | model=historical_median | error band=±48.64%
- 18M: ₹586.02 | model=historical_median | error band=±68.18%
- 24M: ₹558.43 | model=historical_median | error band=±65.73%
- 36M: ₹827.80 | model=extra_trees | error band=±104.31%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.199999809265137
- Current P/L: ₹-6735.52
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹5.03 | model=historical_median | error band=±15.24%
- 6M: ₹5.04 | model=historical_median | error band=±21.60%
- 9M: ₹3.13 | model=hist | error band=±54.31%
- 12M: ₹3.80 | model=extra_trees | error band=±49.47%
- 18M: ₹5.74 | model=historical_median | error band=±55.81%
- 24M: ₹5.89 | model=historical_median | error band=±65.43%
- 36M: ₹4.74 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
