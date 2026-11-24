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
- Current price: 23.299999237060547
- Current P/L: ₹-8540.00
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
- Current price: 17.729999542236328
- Current P/L: ₹-5267.68
- First forecast horizon at/above purchase price: 24M

- 3M: ₹17.68 | model=historical_median | error band=±20.21%
- 6M: ₹17.32 | model=historical_median | error band=±14.97%
- 9M: ₹16.94 | model=historical_median | error band=±23.03%
- 12M: ₹18.75 | model=extra_trees | error band=±21.71%
- 18M: ₹13.68 | model=historical_median | error band=±21.92%
- 24M: ₹24.12 | model=hist | error band=±13.52%
- 36M: ₹28.71 | model=hist | error band=±16.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1351.0
- Current P/L: ₹319.54
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1373.69 | model=historical_median | error band=±13.20%
- 6M: ₹1398.80 | model=historical_median | error band=±21.97%
- 9M: ₹1368.54 | model=hist | error band=±18.98%
- 12M: ₹1359.81 | model=hist | error band=±26.03%
- 18M: ₹1449.70 | model=hist | error band=±33.73%
- 24M: ₹1513.17 | model=extra_trees | error band=±37.53%
- 36M: ₹2421.80 | model=historical_median | error band=±43.26%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 315.45001220703125
- Current P/L: ₹-1344.98
- First forecast horizon at/above purchase price: 18M

- 3M: ₹322.81 | model=historical_median | error band=±15.08%
- 6M: ₹341.33 | model=historical_median | error band=±23.64%
- 9M: ₹345.68 | model=historical_median | error band=±19.87%
- 12M: ₹356.77 | model=historical_median | error band=±19.03%
- 18M: ₹421.68 | model=historical_median | error band=±28.07%
- 24M: ₹415.62 | model=historical_median | error band=±44.71%
- 36M: ₹492.19 | model=historical_median | error band=±53.83%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 132.1999969482422
- Current P/L: ₹2695.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹111.31 | model=extra_trees | error band=±5.99%
- 6M: ₹118.03 | model=hist | error band=±9.06%
- 9M: ₹95.38 | model=hist | error band=±2.27%
- 12M: ₹97.94 | model=historical_median | error band=±2.65%
- 18M: ₹74.35 | model=hist | error band=±3.88%
- 24M: ₹76.46 | model=extra_trees | error band=±6.32%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.80000305175781
- Current P/L: ₹-1982.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹66.19 | model=hist | error band=±12.89%
- 6M: ₹63.91 | model=hist | error band=±30.77%
- 9M: ₹54.88 | model=hist | error band=±59.58%
- 12M: ₹58.67 | model=hist | error band=±74.04%
- 18M: ₹147.32 | model=historical_median | error band=±205.32%
- 24M: ₹159.87 | model=hist | error band=±57.39%
- 36M: ₹639.94 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 328.0
- Current P/L: ₹-7682.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹328.08 | model=historical_median | error band=±13.46%
- 6M: ₹336.01 | model=historical_median | error band=±17.04%
- 9M: ₹330.64 | model=historical_median | error band=±14.33%
- 12M: ₹333.63 | model=historical_median | error band=±17.45%
- 18M: ₹440.02 | model=historical_median | error band=±43.39%
- 24M: ₹538.80 | model=historical_median | error band=±79.04%
- 36M: ₹648.85 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 187.2899932861328
- Current P/L: ₹-10205.20
- First forecast horizon at/above purchase price: 24M

- 3M: ₹182.23 | model=extra_trees | error band=±8.94%
- 6M: ₹172.23 | model=extra_trees | error band=±21.50%
- 9M: ₹165.15 | model=extra_trees | error band=±27.80%
- 12M: ₹160.03 | model=extra_trees | error band=±24.23%
- 18M: ₹191.52 | model=hist | error band=±29.78%
- 24M: ₹243.33 | model=historical_median | error band=±45.45%
- 36M: ₹260.76 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.33000183105469
- Current P/L: ₹-10626.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹81.26 | model=historical_median | error band=±18.12%
- 6M: ₹81.30 | model=extra_trees | error band=±16.41%
- 9M: ₹72.91 | model=extra_trees | error band=±26.21%
- 12M: ₹69.23 | model=extra_trees | error band=±40.49%
- 18M: ₹102.73 | model=hist | error band=±38.65%
- 24M: ₹122.06 | model=hist | error band=±66.34%
- 36M: ₹163.22 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 32.060001373291016
- Current P/L: ₹-52918.04
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹26.90 | model=historical_median | error band=±12.32%
- 6M: ₹24.79 | model=extra_trees | error band=±15.58%
- 9M: ₹21.59 | model=hist | error band=±9.69%
- 12M: ₹23.92 | model=extra_trees | error band=±4.71%
- 18M: ₹16.64 | model=hist | error band=±4.13%
- 24M: N/A — Insufficient history for target_24M: 7 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 173.85000610351562
- Current P/L: ₹-8320.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹173.09 | model=historical_median | error band=±20.74%
- 6M: ₹169.43 | model=extra_trees | error band=±16.01%
- 9M: ₹177.77 | model=historical_median | error band=±25.31%
- 12M: ₹177.28 | model=historical_median | error band=±23.09%
- 18M: ₹190.54 | model=historical_median | error band=±24.78%
- 24M: ₹333.76 | model=extra_trees | error band=±38.17%
- 36M: ₹241.44 | model=historical_median | error band=±50.50%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 54.959999084472656
- Current P/L: ₹-3778.48
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹53.82 | model=extra_trees | error band=±17.32%
- 6M: ₹53.20 | model=historical_median | error band=±29.42%
- 9M: ₹53.33 | model=historical_median | error band=±35.31%
- 12M: ₹55.15 | model=historical_median | error band=±42.65%
- 18M: ₹62.15 | model=historical_median | error band=±60.32%
- 24M: ₹70.08 | model=historical_median | error band=±86.22%
- 36M: ₹97.25 | model=historical_median | error band=±95.17%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.239999771118164
- Current P/L: ₹-51232.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹15.90 | model=historical_median | error band=±26.45%
- 6M: ₹16.70 | model=historical_median | error band=±27.32%
- 9M: ₹15.13 | model=historical_median | error band=±42.49%
- 12M: ₹17.31 | model=historical_median | error band=±61.50%
- 18M: ₹20.08 | model=historical_median | error band=±129.42%
- 24M: ₹34.84 | model=hist | error band=±99.85%
- 36M: ₹40.94 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 447.2000122070313
- Current P/L: ₹-28450.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹430.39 | model=extra_trees | error band=±10.53%
- 6M: ₹433.72 | model=historical_median | error band=±21.31%
- 9M: ₹433.04 | model=historical_median | error band=±32.40%
- 12M: ₹497.85 | model=historical_median | error band=±48.64%
- 18M: ₹567.74 | model=historical_median | error band=±68.18%
- 24M: ₹538.74 | model=historical_median | error band=±65.73%
- 36M: ₹582.47 | model=hist | error band=±114.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.78000020980835
- Current P/L: ₹-7146.70
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.55 | model=historical_median | error band=±15.24%
- 6M: ₹4.68 | model=historical_median | error band=±21.60%
- 9M: ₹2.84 | model=hist | error band=±54.31%
- 12M: ₹3.53 | model=extra_trees | error band=±49.47%
- 18M: ₹5.22 | model=historical_median | error band=±55.81%
- 24M: ₹5.56 | model=historical_median | error band=±65.43%
- 36M: ₹4.46 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
