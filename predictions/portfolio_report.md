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
- Current price: 26.809999465942383
- Current P/L: ₹-5030.00
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
- Current price: 17.200000762939453
- Current P/L: ₹-5745.74
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.16 | model=historical_median | error band=±17.82%
- 6M: ₹16.81 | model=historical_median | error band=±14.98%
- 9M: ₹16.46 | model=historical_median | error band=±23.03%
- 12M: ₹17.62 | model=extra_trees | error band=±21.34%
- 18M: ₹13.13 | model=historical_median | error band=±21.85%
- 24M: ₹14.06 | model=extra_trees | error band=±13.20%
- 36M: ₹4.76 | model=hist | error band=±16.27%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1320.0
- Current P/L: ₹-83.46
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1336.89 | model=historical_median | error band=±14.10%
- 6M: ₹1367.42 | model=historical_median | error band=±21.97%
- 9M: ₹1470.50 | model=hist | error band=±25.66%
- 12M: ₹1920.58 | model=hist | error band=±26.03%
- 18M: ₹1595.57 | model=historical_median | error band=±33.73%
- 24M: ₹1744.91 | model=extra_trees | error band=±37.59%
- 36M: ₹2375.61 | model=historical_median | error band=±43.63%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.45001220703125
- Current P/L: ₹-1136.98
- First forecast horizon at/above purchase price: 12M

- 3M: ₹334.25 | model=historical_median | error band=±16.15%
- 6M: ₹344.76 | model=historical_median | error band=±23.03%
- 9M: ₹355.96 | model=historical_median | error band=±18.92%
- 12M: ₹367.95 | model=historical_median | error band=±19.54%
- 18M: ₹424.24 | model=historical_median | error band=±23.83%
- 24M: ₹414.88 | model=historical_median | error band=±49.09%
- 36M: ₹508.16 | model=historical_median | error band=±57.92%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 111.45999908447266
- Current P/L: ₹-4564.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹95.84 | model=extra_trees | error band=±5.99%
- 6M: ₹100.59 | model=hist | error band=±5.12%
- 9M: ₹83.73 | model=extra_trees | error band=±2.28%
- 12M: ₹82.26 | model=historical_median | error band=±2.65%
- 18M: ₹62.98 | model=hist | error band=±3.88%
- 24M: ₹57.54 | model=extra_trees | error band=±7.46%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.43000030517578
- Current P/L: ₹-2056.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹70.32 | model=hist | error band=±12.89%
- 6M: ₹71.28 | model=hist | error band=±30.77%
- 9M: ₹65.84 | model=hist | error band=±59.58%
- 12M: ₹57.27 | model=hist | error band=±74.00%
- 18M: ₹163.05 | model=historical_median | error band=±206.28%
- 24M: ₹194.59 | model=hist | error band=±56.97%
- 36M: ₹640.85 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 352.5
- Current P/L: ₹-5967.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹358.21 | model=historical_median | error band=±12.16%
- 6M: ₹361.61 | model=historical_median | error band=±17.04%
- 9M: ₹361.29 | model=historical_median | error band=±14.33%
- 12M: ₹359.45 | model=historical_median | error band=±17.45%
- 18M: ₹472.92 | model=historical_median | error band=±43.39%
- 24M: ₹577.70 | model=historical_median | error band=±79.04%
- 36M: ₹574.74 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 198.0
- Current P/L: ₹-6885.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹190.38 | model=extra_trees | error band=±9.56%
- 6M: ₹181.05 | model=extra_trees | error band=±21.50%
- 9M: ₹174.68 | model=extra_trees | error band=±27.82%
- 12M: ₹186.36 | model=extra_trees | error band=±25.05%
- 18M: ₹183.86 | model=hist | error band=±29.78%
- 24M: ₹257.98 | model=historical_median | error band=±45.45%
- 36M: ₹277.00 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.5
- Current P/L: ₹-10875.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹80.48 | model=historical_median | error band=±18.12%
- 6M: ₹82.80 | model=extra_trees | error band=±16.41%
- 9M: ₹75.10 | model=extra_trees | error band=±26.21%
- 12M: ₹78.33 | model=extra_trees | error band=±40.49%
- 18M: ₹143.50 | model=hist | error band=±49.29%
- 24M: ₹148.51 | model=hist | error band=±66.34%
- 36M: ₹161.80 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 34.209999084472656
- Current P/L: ₹-46807.74
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.48 | model=historical_median | error band=±12.25%
- 6M: ₹24.74 | model=extra_trees | error band=±16.47%
- 9M: ₹22.28 | model=hist | error band=±9.69%
- 12M: ₹23.16 | model=historical_median | error band=±5.02%
- 18M: ₹17.34 | model=hist | error band=±4.47%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 172.50999450683594
- Current P/L: ₹-8435.74
- First forecast horizon at/above purchase price: 24M

- 3M: ₹171.60 | model=historical_median | error band=±20.77%
- 6M: ₹163.46 | model=extra_trees | error band=±20.87%
- 9M: ₹175.78 | model=historical_median | error band=±23.71%
- 12M: ₹177.66 | model=historical_median | error band=±16.77%
- 18M: ₹196.10 | model=historical_median | error band=±29.46%
- 24M: ₹271.74 | model=extra_trees | error band=±28.41%
- 36M: ₹236.97 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 57.150001525878906
- Current P/L: ₹-3618.61
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹50.97 | model=extra_trees | error band=±17.98%
- 6M: ₹55.38 | model=historical_median | error band=±29.42%
- 9M: ₹56.01 | model=historical_median | error band=±34.89%
- 12M: ₹57.40 | model=historical_median | error band=±42.65%
- 18M: ₹64.53 | model=historical_median | error band=±60.32%
- 24M: ₹73.27 | model=historical_median | error band=±86.22%
- 36M: ₹100.95 | model=historical_median | error band=±96.49%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.43000030517578
- Current P/L: ₹-48555.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.46 | model=historical_median | error band=±31.94%
- 6M: ₹17.80 | model=historical_median | error band=±27.45%
- 9M: ₹17.17 | model=historical_median | error band=±45.34%
- 12M: ₹18.50 | model=historical_median | error band=±61.50%
- 18M: ₹21.26 | model=historical_median | error band=±126.54%
- 24M: ₹20.56 | model=hist | error band=±99.85%
- 36M: ₹43.43 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 457.0
- Current P/L: ₹-27852.60
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹425.68 | model=extra_trees | error band=±14.99%
- 6M: ₹443.91 | model=historical_median | error band=±21.31%
- 9M: ₹446.47 | model=historical_median | error band=±32.40%
- 12M: ₹509.57 | model=historical_median | error band=±48.64%
- 18M: ₹582.55 | model=historical_median | error band=±68.18%
- 24M: ₹555.01 | model=historical_median | error band=±65.73%
- 36M: ₹784.48 | model=extra_trees | error band=±104.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.079999923706055
- Current P/L: ₹-6853.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.88 | model=historical_median | error band=±15.24%
- 6M: ₹4.96 | model=historical_median | error band=±21.60%
- 9M: ₹3.19 | model=hist | error band=±54.31%
- 12M: ₹3.37 | model=extra_trees | error band=±49.47%
- 18M: ₹5.60 | model=historical_median | error band=±55.81%
- 24M: ₹5.72 | model=historical_median | error band=±65.43%
- 36M: ₹4.63 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
