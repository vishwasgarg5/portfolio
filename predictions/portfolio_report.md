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
- Current price: 25.959999084472656
- Current P/L: ₹-5880.00
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
- Current price: 18.020000457763672
- Current P/L: ₹-5006.10
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.98 | model=historical_median | error band=±17.82%
- 6M: ₹17.67 | model=historical_median | error band=±14.98%
- 9M: ₹17.23 | model=historical_median | error band=±23.03%
- 12M: ₹17.99 | model=extra_trees | error band=±21.48%
- 18M: ₹13.80 | model=historical_median | error band=±21.88%
- 24M: ₹16.43 | model=extra_trees | error band=±12.98%
- 36M: ₹8.65 | model=hist | error band=±16.13%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1344.800048828125
- Current P/L: ₹238.94
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1361.75 | model=historical_median | error band=±14.10%
- 6M: ₹1392.66 | model=historical_median | error band=±21.97%
- 9M: ₹1294.72 | model=extra_trees | error band=±25.66%
- 12M: ₹1348.84 | model=hist | error band=±26.03%
- 18M: ₹1410.54 | model=hist | error band=±33.73%
- 24M: ₹1526.10 | model=extra_trees | error band=±37.53%
- 36M: ₹2413.11 | model=historical_median | error band=±43.25%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 321.25
- Current P/L: ₹-1194.18
- First forecast horizon at/above purchase price: 12M

- 3M: ₹331.46 | model=historical_median | error band=±15.08%
- 6M: ₹352.83 | model=historical_median | error band=±17.62%
- 9M: ₹353.36 | model=historical_median | error band=±18.85%
- 12M: ₹373.03 | model=historical_median | error band=±19.07%
- 18M: ₹421.35 | model=historical_median | error band=±22.98%
- 24M: ₹428.82 | model=historical_median | error band=±48.57%
- 36M: ₹497.12 | model=historical_median | error band=±58.72%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 115.9499969482422
- Current P/L: ₹-2992.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹98.73 | model=extra_trees | error band=±5.97%
- 6M: ₹94.32 | model=hist | error band=±9.03%
- 9M: ₹85.50 | model=extra_trees | error band=±2.26%
- 12M: ₹85.58 | model=historical_median | error band=±2.65%
- 18M: ₹67.83 | model=hist | error band=±3.88%
- 24M: ₹63.53 | model=extra_trees | error band=±6.43%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 82.11000061035156
- Current P/L: ₹-1720.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹68.46 | model=hist | error band=±12.89%
- 6M: ₹68.32 | model=hist | error band=±30.77%
- 9M: ₹57.86 | model=hist | error band=±59.58%
- 12M: ₹65.16 | model=hist | error band=±74.04%
- 18M: ₹157.92 | model=historical_median | error band=±205.32%
- 24M: ₹212.64 | model=hist | error band=±57.14%
- 36M: ₹624.45 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 345.5
- Current P/L: ₹-6457.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹351.13 | model=historical_median | error band=±12.16%
- 6M: ₹354.19 | model=historical_median | error band=±17.04%
- 9M: ₹353.80 | model=historical_median | error band=±14.33%
- 12M: ₹351.70 | model=historical_median | error band=±17.45%
- 18M: ₹463.52 | model=historical_median | error band=±43.39%
- 24M: ₹566.77 | model=historical_median | error band=±79.04%
- 36M: ₹584.48 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 193.5399932861328
- Current P/L: ₹-8267.70
- First forecast horizon at/above purchase price: 24M

- 3M: ₹187.51 | model=extra_trees | error band=±9.56%
- 6M: ₹183.97 | model=extra_trees | error band=±21.50%
- 9M: ₹177.40 | model=extra_trees | error band=±27.80%
- 12M: ₹182.10 | model=extra_trees | error band=±24.70%
- 18M: ₹174.38 | model=hist | error band=±29.78%
- 24M: ₹252.07 | model=historical_median | error band=±45.45%
- 36M: ₹270.26 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 78.5
- Current P/L: ₹-11475.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹78.45 | model=historical_median | error band=±18.12%
- 6M: ₹83.62 | model=extra_trees | error band=±16.41%
- 9M: ₹74.14 | model=extra_trees | error band=±26.21%
- 12M: ₹77.30 | model=extra_trees | error band=±40.49%
- 18M: ₹111.74 | model=hist | error band=±49.29%
- 24M: ₹103.80 | model=historical_median | error band=±66.34%
- 36M: ₹157.60 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 33.72999954223633
- Current P/L: ₹-48171.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.17 | model=historical_median | error band=±12.25%
- 6M: ₹25.34 | model=extra_trees | error band=±15.55%
- 9M: ₹23.34 | model=hist | error band=±9.69%
- 12M: ₹23.23 | model=historical_median | error band=±4.71%
- 18M: ₹17.25 | model=hist | error band=±4.35%
- 24M: N/A — Insufficient history for target_24M: 2 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 174.4600067138672
- Current P/L: ₹-8268.04
- First forecast horizon at/above purchase price: 24M

- 3M: ₹173.70 | model=historical_median | error band=±20.56%
- 6M: ₹164.60 | model=extra_trees | error band=±16.19%
- 9M: ₹176.31 | model=historical_median | error band=±24.47%
- 12M: ₹177.91 | model=historical_median | error band=±24.59%
- 18M: ₹193.36 | model=historical_median | error band=±24.08%
- 24M: ₹292.27 | model=extra_trees | error band=±29.94%
- 36M: ₹238.96 | model=historical_median | error band=±38.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 56.58000183105469
- Current P/L: ₹-3660.22
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹54.17 | model=extra_trees | error band=±17.98%
- 6M: ₹54.79 | model=historical_median | error band=±29.42%
- 9M: ₹55.40 | model=historical_median | error band=±34.89%
- 12M: ₹56.81 | model=historical_median | error band=±42.65%
- 18M: ₹63.96 | model=historical_median | error band=±60.32%
- 24M: ₹73.58 | model=historical_median | error band=±86.22%
- 36M: ₹100.06 | model=historical_median | error band=±95.16%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.06999969482422
- Current P/L: ₹-49365.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.12 | model=historical_median | error band=±31.94%
- 6M: ₹17.49 | model=historical_median | error band=±27.30%
- 9M: ₹16.84 | model=historical_median | error band=±45.34%
- 12M: ₹18.14 | model=historical_median | error band=±61.50%
- 18M: ₹20.88 | model=historical_median | error band=±129.48%
- 24M: ₹28.76 | model=hist | error band=±99.85%
- 36M: ₹42.66 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 451.6499938964844
- Current P/L: ₹-28178.95
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹440.14 | model=extra_trees | error band=±14.96%
- 6M: ₹438.69 | model=historical_median | error band=±21.31%
- 9M: ₹439.08 | model=historical_median | error band=±32.40%
- 12M: ₹503.00 | model=historical_median | error band=±48.64%
- 18M: ₹574.71 | model=historical_median | error band=±68.18%
- 24M: ₹546.83 | model=historical_median | error band=±65.73%
- 36M: ₹829.09 | model=extra_trees | error band=±114.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.920000076293945
- Current P/L: ₹-7009.64
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.69 | model=historical_median | error band=±15.24%
- 6M: ₹4.80 | model=historical_median | error band=±21.60%
- 9M: ₹3.01 | model=hist | error band=±54.31%
- 12M: ₹3.02 | model=hist | error band=±49.47%
- 18M: ₹5.41 | model=historical_median | error band=±55.81%
- 24M: ₹5.61 | model=historical_median | error band=±65.43%
- 36M: ₹4.52 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
