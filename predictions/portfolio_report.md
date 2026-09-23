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
- Current price: 33.81999969482422
- Current P/L: ₹1980.00
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
- Current price: 23.200000762939453
- Current P/L: ₹-333.74
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.21 | model=historical_median | error band=±17.82%
- 6M: ₹22.77 | model=historical_median | error band=±14.97%
- 9M: ₹22.39 | model=historical_median | error band=±23.03%
- 12M: ₹26.89 | model=extra_trees | error band=±21.87%
- 18M: ₹17.45 | model=historical_median | error band=±21.84%
- 24M: ₹26.20 | model=extra_trees | error band=±13.56%
- 36M: ₹27.35 | model=hist | error band=±16.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1247.5
- Current P/L: ₹-1025.96
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1266.17 | model=historical_median | error band=±14.10%
- 6M: ₹1297.41 | model=historical_median | error band=±21.97%
- 9M: ₹1374.54 | model=hist | error band=±25.66%
- 12M: ₹1512.28 | model=hist | error band=±26.03%
- 18M: ₹1209.29 | model=hist | error band=±33.73%
- 24M: ₹1386.64 | model=extra_trees | error band=±33.79%
- 36M: ₹1500.76 | model=extra_trees | error band=±43.77%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 327.25
- Current P/L: ₹-1038.18
- First forecast horizon at/above purchase price: 12M

- 3M: ₹338.63 | model=historical_median | error band=±15.08%
- 6M: ₹360.46 | model=historical_median | error band=±17.62%
- 9M: ₹361.91 | model=historical_median | error band=±18.85%
- 12M: ₹386.81 | model=historical_median | error band=±19.03%
- 18M: ₹424.45 | model=historical_median | error band=±22.55%
- 24M: ₹429.32 | model=historical_median | error band=±39.71%
- 36M: ₹497.68 | model=historical_median | error band=±51.98%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 110.91999816894533
- Current P/L: ₹-4753.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.15 | model=historical_median | error band=±6.88%
- 6M: ₹99.85 | model=hist | error band=±5.01%
- 9M: ₹91.46 | model=extra_trees | error band=±2.20%
- 12M: ₹81.24 | model=historical_median | error band=±2.73%
- 18M: ₹67.41 | model=hist | error band=±3.87%
- 24M: ₹78.02 | model=hist | error band=±6.55%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.97000122070312
- Current P/L: ₹-1948.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹72.94 | model=hist | error band=±17.38%
- 6M: ₹76.02 | model=historical_median | error band=±27.15%
- 9M: ₹46.34 | model=hist | error band=±60.10%
- 12M: ₹87.24 | model=hist | error band=±77.06%
- 18M: ₹173.53 | model=historical_median | error band=±202.30%
- 24M: ₹609.98 | model=hist | error band=±40.75%
- 36M: ₹572.26 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 369.0
- Current P/L: ₹-4812.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹375.74 | model=historical_median | error band=±12.16%
- 6M: ₹382.27 | model=historical_median | error band=±10.78%
- 9M: ₹378.70 | model=historical_median | error band=±14.33%
- 12M: ₹384.79 | model=historical_median | error band=±18.83%
- 18M: ₹489.29 | model=historical_median | error band=±44.88%
- 24M: ₹627.84 | model=historical_median | error band=±76.59%
- 36M: ₹462.78 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 164.9600067138672
- Current P/L: ₹-17127.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹171.27 | model=extra_trees | error band=±9.56%
- 6M: ₹158.30 | model=extra_trees | error band=±21.50%
- 9M: ₹142.88 | model=extra_trees | error band=±27.83%
- 12M: ₹154.46 | model=extra_trees | error band=±21.79%
- 18M: ₹173.99 | model=hist | error band=±29.78%
- 24M: ₹216.49 | model=historical_median | error band=±41.29%
- 36M: ₹235.53 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 85.68000030517578
- Current P/L: ₹-9321.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹86.56 | model=historical_median | error band=±18.12%
- 6M: ₹68.35 | model=extra_trees | error band=±16.72%
- 9M: ₹61.04 | model=extra_trees | error band=±26.21%
- 12M: ₹57.03 | model=extra_trees | error band=±40.49%
- 18M: ₹61.71 | model=hist | error band=±38.65%
- 24M: ₹114.97 | model=historical_median | error band=±61.31%
- 36M: ₹173.94 | model=historical_median | error band=±88.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 41.400001525878906
- Current P/L: ₹-26373.76
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹41.69 | model=extra_trees | error band=±12.42%
- 6M: ₹28.08 | model=hist | error band=±16.51%
- 9M: ₹34.86 | model=hist | error band=±10.35%
- 12M: ₹32.26 | model=extra_trees | error band=±10.94%
- 18M: ₹21.12 | model=hist | error band=±4.81%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 189.33999633789065
- Current P/L: ₹-6988.36
- First forecast horizon at/above purchase price: 24M

- 3M: ₹190.93 | model=historical_median | error band=±20.10%
- 6M: ₹170.35 | model=extra_trees | error band=±20.87%
- 9M: ₹198.36 | model=historical_median | error band=±20.33%
- 12M: ₹196.34 | model=historical_median | error band=±16.76%
- 18M: ₹214.62 | model=historical_median | error band=±29.46%
- 24M: ₹332.17 | model=extra_trees | error band=±28.68%
- 36M: ₹257.64 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.16999816894531
- Current P/L: ₹-3179.15
- First forecast horizon at/above purchase price: 36M

- 3M: ₹61.24 | model=historical_median | error band=±17.98%
- 6M: ₹62.36 | model=historical_median | error band=±25.92%
- 9M: ₹62.09 | model=historical_median | error band=±34.89%
- 12M: ₹63.81 | model=historical_median | error band=±38.32%
- 18M: ₹70.98 | model=historical_median | error band=±69.37%
- 24M: ₹81.54 | model=historical_median | error band=±86.61%
- 36M: ₹110.89 | model=historical_median | error band=±122.99%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.040000915527344
- Current P/L: ₹-42682.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.44 | model=historical_median | error band=±32.27%
- 6M: ₹22.83 | model=extra_trees | error band=±25.64%
- 9M: ₹21.29 | model=extra_trees | error band=±47.41%
- 12M: ₹21.46 | model=historical_median | error band=±59.34%
- 18M: ₹16.55 | model=extra_trees | error band=±97.85%
- 24M: ₹37.39 | model=historical_median | error band=±104.21%
- 36M: ₹47.75 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 464.7999877929688
- Current P/L: ₹-27376.80
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹416.43 | model=hist | error band=±15.04%
- 6M: ₹451.69 | model=historical_median | error band=±21.55%
- 9M: ₹458.71 | model=historical_median | error band=±32.44%
- 12M: ₹530.78 | model=historical_median | error band=±48.53%
- 18M: ₹596.76 | model=historical_median | error band=±68.41%
- 24M: ₹573.37 | model=historical_median | error band=±48.40%
- 36M: ₹358.75 | model=extra_trees | error band=±115.01%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.199999809265137
- Current P/L: ₹-6735.52
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.94 | model=historical_median | error band=±20.59%
- 6M: ₹5.22 | model=historical_median | error band=±21.94%
- 9M: ₹2.17 | model=hist | error band=±48.03%
- 12M: ₹2.15 | model=extra_trees | error band=±53.68%
- 18M: ₹5.77 | model=historical_median | error band=±51.51%
- 24M: ₹6.20 | model=historical_median | error band=±60.41%
- 36M: ₹4.64 | model=historical_median | error band=±87.63%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
