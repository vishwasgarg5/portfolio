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
- Current price: 26.559999465942383
- Current P/L: ₹-5280.00
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
- Current price: 15.609999656677246
- Current P/L: ₹-7179.92
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.58 | model=historical_median | error band=±17.82%
- 6M: ₹15.29 | model=historical_median | error band=±15.00%
- 9M: ₹14.97 | model=historical_median | error band=±23.03%
- 12M: ₹16.69 | model=extra_trees | error band=±21.86%
- 18M: ₹11.89 | model=historical_median | error band=±21.83%
- 24M: ₹13.59 | model=extra_trees | error band=±13.11%
- 36M: ₹4.05 | model=hist | error band=±16.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1158.0
- Current P/L: ₹-2189.46
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1172.90 | model=historical_median | error band=±14.10%
- 6M: ₹1199.95 | model=historical_median | error band=±21.97%
- 9M: ₹1408.09 | model=hist | error band=±25.66%
- 12M: ₹1478.45 | model=hist | error band=±26.03%
- 18M: ₹1400.28 | model=historical_median | error band=±33.73%
- 24M: ₹1502.72 | model=extra_trees | error band=±37.59%
- 36M: ₹2088.87 | model=historical_median | error band=±43.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 303.75
- Current P/L: ₹-1649.18
- First forecast horizon at/above purchase price: 18M

- 3M: ₹313.59 | model=historical_median | error band=±15.08%
- 6M: ₹328.46 | model=historical_median | error band=±23.64%
- 9M: ₹334.98 | model=historical_median | error band=±18.85%
- 12M: ₹352.77 | model=historical_median | error band=±19.03%
- 18M: ₹399.91 | model=historical_median | error band=±22.96%
- 24M: ₹403.89 | model=historical_median | error band=±48.50%
- 36M: ₹467.71 | model=historical_median | error band=±54.61%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 100.58999633789062
- Current P/L: ₹-8368.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹104.27 | model=hist | error band=±5.99%
- 6M: ₹94.13 | model=hist | error band=±4.96%
- 9M: ₹81.46 | model=extra_trees | error band=±2.27%
- 12M: ₹74.15 | model=historical_median | error band=±2.73%
- 18M: ₹64.46 | model=hist | error band=±3.90%
- 24M: ₹50.80 | model=extra_trees | error band=±8.89%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 74.62999725341797
- Current P/L: ₹-3216.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹64.06 | model=hist | error band=±14.12%
- 6M: ₹70.49 | model=historical_median | error band=±30.97%
- 9M: ₹71.10 | model=hist | error band=±59.43%
- 12M: ₹83.87 | model=hist | error band=±74.31%
- 18M: ₹152.37 | model=historical_median | error band=±207.09%
- 24M: ₹352.21 | model=hist | error band=±83.85%
- 36M: ₹530.13 | model=hist | error band=±267.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 335.0
- Current P/L: ₹-7192.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹340.53 | model=historical_median | error band=±12.16%
- 6M: ₹343.78 | model=historical_median | error band=±17.04%
- 9M: ₹343.51 | model=historical_median | error band=±14.33%
- 12M: ₹342.03 | model=historical_median | error band=±17.45%
- 18M: ₹453.99 | model=historical_median | error band=±43.39%
- 24M: ₹548.20 | model=historical_median | error band=±79.04%
- 36M: ₹598.53 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 184.5
- Current P/L: ₹-11070.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹166.02 | model=extra_trees | error band=±9.56%
- 6M: ₹150.03 | model=extra_trees | error band=±21.50%
- 9M: ₹137.78 | model=extra_trees | error band=±27.75%
- 12M: ₹165.34 | model=extra_trees | error band=±24.41%
- 18M: ₹127.77 | model=hist | error band=±29.78%
- 24M: ₹239.83 | model=historical_median | error band=±45.45%
- 36M: ₹260.01 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 77.30000305175781
- Current P/L: ₹-11835.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹77.94 | model=historical_median | error band=±18.12%
- 6M: ₹68.12 | model=extra_trees | error band=±16.41%
- 9M: ₹57.49 | model=extra_trees | error band=±26.21%
- 12M: ₹54.75 | model=extra_trees | error band=±40.49%
- 18M: ₹62.62 | model=hist | error band=±38.65%
- 24M: ₹102.64 | model=historical_median | error band=±66.34%
- 36M: ₹156.03 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.65999984741211
- Current P/L: ₹-39844.84
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹30.27 | model=historical_median | error band=±12.25%
- 6M: ₹21.04 | model=hist | error band=±16.39%
- 9M: ₹22.85 | model=hist | error band=±9.69%
- 12M: ₹21.97 | model=historical_median | error band=±7.24%
- 18M: ₹19.12 | model=hist | error band=±4.36%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 162.41000366210938
- Current P/L: ₹-9304.34
- First forecast horizon at/above purchase price: 24M

- 3M: ₹161.43 | model=historical_median | error band=±20.77%
- 6M: ₹157.90 | model=extra_trees | error band=±20.87%
- 9M: ₹165.71 | model=historical_median | error band=±23.71%
- 12M: ₹166.94 | model=historical_median | error band=±16.76%
- 18M: ₹184.41 | model=historical_median | error band=±29.46%
- 24M: ₹275.60 | model=extra_trees | error band=±28.52%
- 36M: ₹220.75 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 50.93999862670898
- Current P/L: ₹-4071.94
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹49.30 | model=historical_median | error band=±17.98%
- 6M: ₹49.41 | model=historical_median | error band=±29.42%
- 9M: ₹49.95 | model=historical_median | error band=±34.89%
- 12M: ₹51.21 | model=historical_median | error band=±42.65%
- 18M: ₹57.49 | model=historical_median | error band=±66.42%
- 24M: ₹64.83 | model=historical_median | error band=±86.22%
- 36M: ₹89.78 | model=historical_median | error band=±95.67%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.389999389648438
- Current P/L: ₹-50895.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹16.47 | model=historical_median | error band=±31.94%
- 6M: ₹16.77 | model=historical_median | error band=±27.40%
- 9M: ₹16.18 | model=historical_median | error band=±45.34%
- 12M: ₹17.42 | model=historical_median | error band=±61.50%
- 18M: ₹19.83 | model=historical_median | error band=±129.71%
- 24M: ₹44.94 | model=hist | error band=±99.85%
- 36M: ₹40.87 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 442.7000122070313
- Current P/L: ₹-28724.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹392.47 | model=hist | error band=±14.99%
- 6M: ₹430.33 | model=historical_median | error band=±21.31%
- 9M: ₹433.31 | model=historical_median | error band=±32.43%
- 12M: ₹496.03 | model=historical_median | error band=±48.65%
- 18M: ₹564.67 | model=historical_median | error band=±68.41%
- 24M: ₹539.73 | model=historical_median | error band=±66.34%
- 36M: ₹546.99 | model=extra_trees | error band=±106.60%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.829999923706055
- Current P/L: ₹-7097.75
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.65 | model=historical_median | error band=±15.24%
- 6M: ₹4.70 | model=historical_median | error band=±21.60%
- 9M: ₹2.93 | model=hist | error band=±54.31%
- 12M: ₹2.15 | model=extra_trees | error band=±49.47%
- 18M: ₹5.35 | model=historical_median | error band=±55.81%
- 24M: ₹5.44 | model=historical_median | error band=±65.43%
- 36M: ₹4.38 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
