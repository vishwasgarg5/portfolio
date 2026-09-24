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
- Current price: 32.349998474121094
- Current P/L: ₹510.00
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
- Current price: 22.489999771118164
- Current P/L: ₹-974.16
- First forecast horizon at/above purchase price: 12M

- 3M: ₹22.50 | model=historical_median | error band=±17.82%
- 6M: ₹22.09 | model=historical_median | error band=±14.99%
- 9M: ₹21.71 | model=historical_median | error band=±23.03%
- 12M: ₹26.13 | model=extra_trees | error band=±21.35%
- 18M: ₹16.96 | model=historical_median | error band=±21.70%
- 24M: ₹27.25 | model=extra_trees | error band=±13.36%
- 36M: ₹23.80 | model=hist | error band=±16.25%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1227.4000244140625
- Current P/L: ₹-1287.26
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1245.47 | model=historical_median | error band=±14.10%
- 6M: ₹1276.44 | model=historical_median | error band=±21.97%
- 9M: ₹1397.43 | model=hist | error band=±25.66%
- 12M: ₹1519.37 | model=hist | error band=±26.03%
- 18M: ₹1223.68 | model=hist | error band=±33.73%
- 24M: ₹1385.43 | model=extra_trees | error band=±33.80%
- 36M: ₹1501.31 | model=extra_trees | error band=±43.26%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 325.8999938964844
- Current P/L: ₹-1073.28
- First forecast horizon at/above purchase price: 12M

- 3M: ₹337.08 | model=historical_median | error band=±15.08%
- 6M: ₹358.98 | model=historical_median | error band=±17.62%
- 9M: ₹360.41 | model=historical_median | error band=±18.85%
- 12M: ₹383.98 | model=historical_median | error band=±19.03%
- 18M: ₹423.45 | model=historical_median | error band=±22.74%
- 24M: ₹429.96 | model=historical_median | error band=±39.75%
- 36M: ₹495.61 | model=historical_median | error band=±51.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 109.72000122070312
- Current P/L: ₹-5173.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹101.05 | model=historical_median | error band=±6.85%
- 6M: ₹98.66 | model=hist | error band=±5.08%
- 9M: ₹90.82 | model=extra_trees | error band=±2.20%
- 12M: ₹80.26 | model=historical_median | error band=±2.73%
- 18M: ₹66.93 | model=hist | error band=±3.81%
- 24M: ₹74.84 | model=hist | error band=±5.95%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 79.94999694824219
- Current P/L: ₹-2152.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹71.98 | model=hist | error band=±17.38%
- 6M: ₹58.81 | model=hist | error band=±27.15%
- 9M: ₹51.66 | model=hist | error band=±60.10%
- 12M: ₹86.85 | model=hist | error band=±77.06%
- 18M: ₹171.34 | model=historical_median | error band=±202.30%
- 24M: ₹600.81 | model=hist | error band=±43.25%
- 36M: ₹568.33 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 364.7000122070313
- Current P/L: ₹-5113.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹371.26 | model=historical_median | error band=±12.16%
- 6M: ₹377.78 | model=historical_median | error band=±10.78%
- 9M: ₹374.29 | model=historical_median | error band=±14.33%
- 12M: ₹380.32 | model=historical_median | error band=±18.83%
- 18M: ₹483.90 | model=historical_median | error band=±44.88%
- 24M: ₹620.76 | model=historical_median | error band=±76.59%
- 36M: ₹509.40 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 164.4499969482422
- Current P/L: ₹-17285.60
- First forecast horizon at/above purchase price: 36M

- 3M: ₹170.82 | model=extra_trees | error band=±9.56%
- 6M: ₹159.34 | model=extra_trees | error band=±21.50%
- 9M: ₹141.34 | model=extra_trees | error band=±27.65%
- 12M: ₹157.69 | model=extra_trees | error band=±21.79%
- 18M: ₹179.51 | model=hist | error band=±29.78%
- 24M: ₹215.85 | model=historical_median | error band=±41.29%
- 36M: ₹234.76 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 85.69999694824219
- Current P/L: ₹-9315.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹86.58 | model=historical_median | error band=±18.12%
- 6M: ₹71.03 | model=extra_trees | error band=±16.72%
- 9M: ₹61.72 | model=extra_trees | error band=±26.21%
- 12M: ₹58.43 | model=extra_trees | error band=±40.49%
- 18M: ₹68.13 | model=hist | error band=±38.65%
- 24M: ₹114.89 | model=historical_median | error band=±61.31%
- 36M: ₹173.94 | model=historical_median | error band=±88.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 42.52000045776367
- Current P/L: ₹-23190.72
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹43.90 | model=extra_trees | error band=±12.42%
- 6M: ₹30.59 | model=hist | error band=±16.43%
- 9M: ₹34.68 | model=hist | error band=±10.35%
- 12M: ₹31.16 | model=extra_trees | error band=±10.88%
- 18M: ₹21.37 | model=hist | error band=±5.29%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 186.6100006103516
- Current P/L: ₹-7223.14
- First forecast horizon at/above purchase price: 24M

- 3M: ₹188.19 | model=historical_median | error band=±20.10%
- 6M: ₹169.15 | model=extra_trees | error band=±20.87%
- 9M: ₹195.43 | model=historical_median | error band=±20.33%
- 12M: ₹193.48 | model=historical_median | error band=±16.76%
- 18M: ₹211.49 | model=historical_median | error band=±29.46%
- 24M: ₹333.21 | model=extra_trees | error band=±28.71%
- 36M: ₹254.26 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 62.13999938964844
- Current P/L: ₹-3254.34
- First forecast horizon at/above purchase price: 36M

- 3M: ₹60.23 | model=historical_median | error band=±17.98%
- 6M: ₹61.34 | model=historical_median | error band=±25.80%
- 9M: ₹61.08 | model=historical_median | error band=±34.89%
- 12M: ₹62.77 | model=historical_median | error band=±38.32%
- 18M: ₹69.83 | model=historical_median | error band=±66.42%
- 24M: ₹80.41 | model=historical_median | error band=±86.61%
- 36M: ₹109.10 | model=historical_median | error band=±115.54%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 20.65999984741211
- Current P/L: ₹-43537.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.08 | model=historical_median | error band=±32.27%
- 6M: ₹23.06 | model=extra_trees | error band=±25.32%
- 9M: ₹21.52 | model=extra_trees | error band=±47.41%
- 12M: ₹21.08 | model=historical_median | error band=±59.34%
- 18M: ₹19.79 | model=extra_trees | error band=±97.85%
- 24M: ₹24.01 | model=hist | error band=±104.21%
- 36M: ₹46.94 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 460.5
- Current P/L: ₹-27639.10
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹416.56 | model=hist | error band=±15.04%
- 6M: ₹447.51 | model=historical_median | error band=±21.55%
- 9M: ₹453.88 | model=historical_median | error band=±32.44%
- 12M: ₹525.57 | model=historical_median | error band=±48.52%
- 18M: ₹591.12 | model=historical_median | error band=±68.41%
- 24M: ₹567.55 | model=historical_median | error band=±46.47%
- 36M: ₹355.08 | model=extra_trees | error band=±115.01%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.110000133514404
- Current P/L: ₹-6823.63
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.85 | model=historical_median | error band=±20.49%
- 6M: ₹5.14 | model=historical_median | error band=±21.94%
- 9M: ₹2.02 | model=hist | error band=±48.03%
- 12M: ₹2.05 | model=extra_trees | error band=±53.68%
- 18M: ₹5.67 | model=historical_median | error band=±51.51%
- 24M: ₹6.09 | model=historical_median | error band=±62.85%
- 36M: ₹4.56 | model=historical_median | error band=±88.08%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
