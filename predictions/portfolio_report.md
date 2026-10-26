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
- Current price: 26.6200008392334
- Current P/L: ₹-5220.00
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
- Current price: 15.859999656677246
- Current P/L: ₹-6954.42
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.83 | model=historical_median | error band=±17.82%
- 6M: ₹15.54 | model=historical_median | error band=±14.98%
- 9M: ₹15.23 | model=historical_median | error band=±23.03%
- 12M: ₹16.85 | model=extra_trees | error band=±21.80%
- 18M: ₹12.04 | model=historical_median | error band=±21.53%
- 24M: ₹14.08 | model=extra_trees | error band=±13.26%
- 36M: ₹4.61 | model=hist | error band=±16.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1201.800048828125
- Current P/L: ₹-1620.06
- First forecast horizon at/above purchase price: 18M

- 3M: ₹1217.45 | model=historical_median | error band=±14.10%
- 6M: ₹1245.37 | model=historical_median | error band=±21.97%
- 9M: ₹1318.20 | model=hist | error band=±25.66%
- 12M: ₹1306.91 | model=hist | error band=±26.03%
- 18M: ₹1453.25 | model=historical_median | error band=±33.73%
- 24M: ₹1403.19 | model=extra_trees | error band=±37.58%
- 36M: ₹2168.34 | model=historical_median | error band=±43.10%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 300.0
- Current P/L: ₹-1746.68
- First forecast horizon at/above purchase price: 18M

- 3M: ₹309.79 | model=historical_median | error band=±15.08%
- 6M: ₹324.51 | model=historical_median | error band=±23.64%
- 9M: ₹330.91 | model=historical_median | error band=±18.85%
- 12M: ₹348.40 | model=historical_median | error band=±19.03%
- 18M: ₹393.68 | model=historical_median | error band=±22.96%
- 24M: ₹397.10 | model=historical_median | error band=±48.41%
- 36M: ₹461.54 | model=historical_median | error band=±55.11%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 101.87000274658205
- Current P/L: ₹-7920.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹104.24 | model=extra_trees | error band=±5.99%
- 6M: ₹97.11 | model=hist | error band=±5.11%
- 9M: ₹82.68 | model=extra_trees | error band=±2.25%
- 12M: ₹75.06 | model=historical_median | error band=±2.73%
- 18M: ₹65.66 | model=hist | error band=±3.69%
- 24M: ₹52.16 | model=extra_trees | error band=±8.77%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 74.4000015258789
- Current P/L: ₹-3262.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹66.65 | model=hist | error band=±15.34%
- 6M: ₹63.62 | model=hist | error band=±30.79%
- 9M: ₹82.70 | model=hist | error band=±59.08%
- 12M: ₹84.53 | model=hist | error band=±74.88%
- 18M: ₹152.54 | model=historical_median | error band=±205.72%
- 24M: ₹507.85 | model=hist | error band=±103.89%
- 36M: ₹515.11 | model=hist | error band=±300.30%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 338.5
- Current P/L: ₹-6947.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹344.20 | model=historical_median | error band=±12.16%
- 6M: ₹347.43 | model=historical_median | error band=±17.04%
- 9M: ₹347.14 | model=historical_median | error band=±14.33%
- 12M: ₹345.81 | model=historical_median | error band=±17.45%
- 18M: ₹455.75 | model=historical_median | error band=±43.39%
- 24M: ₹553.88 | model=historical_median | error band=±79.04%
- 36M: ₹613.06 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 189.1999969482422
- Current P/L: ₹-9613.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹169.14 | model=extra_trees | error band=±9.56%
- 6M: ₹154.22 | model=extra_trees | error band=±21.50%
- 9M: ₹144.26 | model=extra_trees | error band=±27.68%
- 12M: ₹149.16 | model=extra_trees | error band=±24.71%
- 18M: ₹125.07 | model=hist | error band=±29.78%
- 24M: ₹245.93 | model=historical_median | error band=±45.45%
- 36M: ₹266.67 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 78.44999694824219
- Current P/L: ₹-11490.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹79.13 | model=historical_median | error band=±18.12%
- 6M: ₹73.83 | model=extra_trees | error band=±16.41%
- 9M: ₹65.36 | model=extra_trees | error band=±26.21%
- 12M: ₹62.96 | model=extra_trees | error band=±40.49%
- 18M: ₹62.69 | model=hist | error band=±38.65%
- 24M: ₹57.57 | model=hist | error band=±66.34%
- 36M: ₹158.43 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 29.940000534057617
- Current P/L: ₹-58943.08
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹24.70 | model=historical_median | error band=±12.31%
- 6M: ₹25.06 | model=hist | error band=±16.43%
- 9M: ₹21.24 | model=hist | error band=±9.69%
- 12M: ₹17.87 | model=historical_median | error band=±8.03%
- 18M: ₹16.50 | model=hist | error band=±5.29%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 160.58999633789062
- Current P/L: ₹-9460.86
- First forecast horizon at/above purchase price: 24M

- 3M: ₹159.62 | model=historical_median | error band=±20.77%
- 6M: ₹156.33 | model=extra_trees | error band=±20.87%
- 9M: ₹163.88 | model=historical_median | error band=±23.71%
- 12M: ₹165.33 | model=historical_median | error band=±16.80%
- 18M: ₹182.45 | model=historical_median | error band=±29.46%
- 24M: ₹299.61 | model=extra_trees | error band=±28.44%
- 36M: ₹219.56 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 49.0
- Current P/L: ₹-4213.56
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹47.43 | model=historical_median | error band=±17.98%
- 6M: ₹47.51 | model=historical_median | error band=±29.42%
- 9M: ₹48.06 | model=historical_median | error band=±34.89%
- 12M: ₹49.30 | model=historical_median | error band=±42.65%
- 18M: ₹55.29 | model=historical_median | error band=±60.32%
- 24M: ₹63.02 | model=historical_median | error band=±86.22%
- 36M: ₹86.33 | model=historical_median | error band=±96.91%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 16.540000915527344
- Current P/L: ₹-52807.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹15.65 | model=historical_median | error band=±31.94%
- 6M: ₹15.96 | model=historical_median | error band=±27.37%
- 9M: ₹15.36 | model=historical_median | error band=±45.34%
- 12M: ₹16.50 | model=historical_median | error band=±61.50%
- 18M: ₹18.96 | model=historical_median | error band=±129.56%
- 24M: ₹40.67 | model=hist | error band=±99.85%
- 36M: ₹38.80 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 438.6499938964844
- Current P/L: ₹-28971.95
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹411.00 | model=extra_trees | error band=±14.97%
- 6M: ₹426.43 | model=historical_median | error band=±21.30%
- 9M: ₹429.70 | model=historical_median | error band=±32.46%
- 12M: ₹491.52 | model=historical_median | error band=±48.65%
- 18M: ₹560.06 | model=historical_median | error band=±68.41%
- 24M: ₹536.14 | model=historical_median | error band=±65.73%
- 36M: ₹592.72 | model=extra_trees | error band=±103.03%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.789999961853027
- Current P/L: ₹-7136.91
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.62 | model=historical_median | error band=±15.24%
- 6M: ₹4.63 | model=historical_median | error band=±21.60%
- 9M: ₹2.97 | model=hist | error band=±54.31%
- 12M: ₹2.41 | model=extra_trees | error band=±49.47%
- 18M: ₹5.31 | model=historical_median | error band=±55.81%
- 24M: ₹5.42 | model=historical_median | error band=±65.43%
- 36M: ₹4.34 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
