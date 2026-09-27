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
- Current price: 32.779998779296875
- Current P/L: ₹940.00
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
- Current price: 22.5
- Current P/L: ₹-965.14
- First forecast horizon at/above purchase price: 12M

- 3M: ₹22.50 | model=historical_median | error band=±17.82%
- 6M: ₹22.10 | model=historical_median | error band=±14.98%
- 9M: ₹21.72 | model=historical_median | error band=±19.95%
- 12M: ₹25.80 | model=extra_trees | error band=±21.61%
- 18M: ₹16.86 | model=historical_median | error band=±21.79%
- 24M: ₹28.52 | model=hist | error band=±13.06%
- 36M: ₹16.96 | model=hist | error band=±16.44%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1226.0
- Current P/L: ₹-1305.46
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1243.75 | model=historical_median | error band=±14.10%
- 6M: ₹1274.92 | model=historical_median | error band=±21.97%
- 9M: ₹1424.61 | model=hist | error band=±25.66%
- 12M: ₹1573.92 | model=hist | error band=±26.03%
- 18M: ₹1271.30 | model=hist | error band=±33.73%
- 24M: ₹1377.36 | model=extra_trees | error band=±33.78%
- 36M: ₹1503.21 | model=extra_trees | error band=±43.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 326.6000061035156
- Current P/L: ₹-1055.08
- First forecast horizon at/above purchase price: 12M

- 3M: ₹337.75 | model=historical_median | error band=±15.08%
- 6M: ₹359.31 | model=historical_median | error band=±17.62%
- 9M: ₹361.18 | model=historical_median | error band=±18.85%
- 12M: ₹383.75 | model=historical_median | error band=±19.03%
- 18M: ₹423.71 | model=historical_median | error band=±22.38%
- 24M: ₹428.85 | model=historical_median | error band=±39.35%
- 36M: ₹497.36 | model=historical_median | error band=±51.50%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 113.22000122070312
- Current P/L: ₹-3948.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹104.27 | model=historical_median | error band=±6.88%
- 6M: ₹100.33 | model=hist | error band=±5.08%
- 9M: ₹91.64 | model=extra_trees | error band=±2.20%
- 12M: ₹82.82 | model=historical_median | error band=±2.73%
- 18M: ₹66.44 | model=hist | error band=±3.90%
- 24M: ₹75.11 | model=hist | error band=±5.94%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 79.94999694824219
- Current P/L: ₹-2152.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹71.47 | model=hist | error band=±17.38%
- 6M: ₹63.57 | model=hist | error band=±27.15%
- 9M: ₹54.28 | model=hist | error band=±60.10%
- 12M: ₹87.45 | model=hist | error band=±77.06%
- 18M: ₹171.00 | model=historical_median | error band=±202.30%
- 24M: ₹602.51 | model=hist | error band=±43.69%
- 36M: ₹552.18 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 367.5
- Current P/L: ₹-4917.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹374.00 | model=historical_median | error band=±12.16%
- 6M: ₹380.65 | model=historical_median | error band=±10.78%
- 9M: ₹377.29 | model=historical_median | error band=±14.33%
- 12M: ₹383.24 | model=historical_median | error band=±18.83%
- 18M: ₹487.77 | model=historical_median | error band=±44.88%
- 24M: ₹625.29 | model=historical_median | error band=±76.59%
- 36M: ₹503.17 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 164.02000427246094
- Current P/L: ₹-17418.90
- First forecast horizon at/above purchase price: 36M

- 3M: ₹172.81 | model=extra_trees | error band=±9.56%
- 6M: ₹161.21 | model=extra_trees | error band=±21.50%
- 9M: ₹147.80 | model=extra_trees | error band=±27.88%
- 12M: ₹161.50 | model=extra_trees | error band=±21.79%
- 18M: ₹179.23 | model=hist | error band=±29.78%
- 24M: ₹215.29 | model=historical_median | error band=±41.29%
- 36M: ₹234.14 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 88.91999816894531
- Current P/L: ₹-8349.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹89.83 | model=historical_median | error band=±18.12%
- 6M: ₹71.01 | model=extra_trees | error band=±16.72%
- 9M: ₹61.49 | model=extra_trees | error band=±26.21%
- 12M: ₹59.55 | model=extra_trees | error band=±40.49%
- 18M: ₹58.33 | model=hist | error band=±49.29%
- 24M: ₹119.20 | model=historical_median | error band=±61.31%
- 36M: ₹180.43 | model=historical_median | error band=±88.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 38.47999954223633
- Current P/L: ₹-34672.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹39.19 | model=extra_trees | error band=±12.42%
- 6M: ₹25.82 | model=hist | error band=±16.55%
- 9M: ₹33.61 | model=hist | error band=±10.35%
- 12M: ₹27.95 | model=extra_trees | error band=±10.94%
- 18M: ₹20.14 | model=hist | error band=±5.17%
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
- 6M: ₹170.55 | model=extra_trees | error band=±20.87%
- 9M: ₹195.43 | model=historical_median | error band=±20.33%
- 12M: ₹193.51 | model=historical_median | error band=±16.76%
- 18M: ₹211.56 | model=historical_median | error band=±29.46%
- 24M: ₹336.40 | model=extra_trees | error band=±28.74%
- 36M: ₹254.27 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 61.7599983215332
- Current P/L: ₹-3282.08
- First forecast horizon at/above purchase price: 36M

- 3M: ₹59.86 | model=historical_median | error band=±17.98%
- 6M: ₹60.96 | model=historical_median | error band=±25.55%
- 9M: ₹60.70 | model=historical_median | error band=±34.89%
- 12M: ₹62.39 | model=historical_median | error band=±38.32%
- 18M: ₹69.43 | model=historical_median | error band=±69.37%
- 24M: ₹79.78 | model=historical_median | error band=±86.61%
- 36M: ₹108.44 | model=historical_median | error band=±115.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 20.56999969482422
- Current P/L: ₹-43740.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.00 | model=historical_median | error band=±32.27%
- 6M: ₹22.93 | model=extra_trees | error band=±25.59%
- 9M: ₹20.91 | model=extra_trees | error band=±47.41%
- 12M: ₹21.01 | model=historical_median | error band=±59.35%
- 18M: ₹18.34 | model=extra_trees | error band=±97.85%
- 24M: ₹15.46 | model=hist | error band=±104.21%
- 36M: ₹46.69 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 458.7000122070313
- Current P/L: ₹-27748.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹427.44 | model=hist | error band=±14.96%
- 6M: ₹445.48 | model=historical_median | error band=±21.57%
- 9M: ₹451.98 | model=historical_median | error band=±32.46%
- 12M: ₹523.46 | model=historical_median | error band=±48.65%
- 18M: ₹588.69 | model=historical_median | error band=±68.41%
- 24M: ₹564.81 | model=historical_median | error band=±46.60%
- 36M: ₹359.46 | model=extra_trees | error band=±114.94%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.119999885559082
- Current P/L: ₹-6813.84
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.87 | model=historical_median | error band=±20.51%
- 6M: ₹5.14 | model=historical_median | error band=±22.33%
- 9M: ₹2.23 | model=hist | error band=±48.03%
- 12M: ₹2.06 | model=extra_trees | error band=±53.68%
- 18M: ₹5.69 | model=historical_median | error band=±51.51%
- 24M: ₹6.03 | model=historical_median | error band=±59.44%
- 36M: ₹4.57 | model=historical_median | error band=±88.26%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
