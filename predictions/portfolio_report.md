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
- Current price: 30.6200008392334
- Current P/L: ₹-1220.00
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
- Current price: 23.15999984741211
- Current P/L: ₹-369.82
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.17 | model=historical_median | error band=±17.82%
- 6M: ₹22.76 | model=historical_median | error band=±14.97%
- 9M: ₹22.36 | model=historical_median | error band=±23.03%
- 12M: ₹26.25 | model=extra_trees | error band=±21.54%
- 18M: ₹17.37 | model=historical_median | error band=±21.61%
- 24M: ₹25.03 | model=extra_trees | error band=±13.21%
- 36M: ₹25.74 | model=hist | error band=±16.31%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1246.5999755859375
- Current P/L: ₹-1037.66
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1265.35 | model=historical_median | error band=±14.10%
- 6M: ₹1296.63 | model=historical_median | error band=±21.97%
- 9M: ₹1403.05 | model=hist | error band=±25.66%
- 12M: ₹1508.74 | model=hist | error band=±26.03%
- 18M: ₹1245.19 | model=hist | error band=±33.73%
- 24M: ₹1373.93 | model=extra_trees | error band=±33.80%
- 36M: ₹1541.87 | model=extra_trees | error band=±43.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 326.5
- Current P/L: ₹-1057.68
- First forecast horizon at/above purchase price: 12M

- 3M: ₹337.80 | model=historical_median | error band=±15.08%
- 6M: ₹359.65 | model=historical_median | error band=±17.62%
- 9M: ₹361.40 | model=historical_median | error band=±18.85%
- 12M: ₹384.82 | model=historical_median | error band=±19.03%
- 18M: ₹423.14 | model=historical_median | error band=±22.56%
- 24M: ₹428.58 | model=historical_median | error band=±38.89%
- 36M: ₹494.30 | model=historical_median | error band=±52.10%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 111.0999984741211
- Current P/L: ₹-4690.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.35 | model=historical_median | error band=±6.77%
- 6M: ₹94.40 | model=historical_median | error band=±5.25%
- 9M: ₹91.42 | model=extra_trees | error band=±2.21%
- 12M: ₹81.84 | model=historical_median | error band=±2.73%
- 18M: ₹67.56 | model=hist | error band=±3.86%
- 24M: ₹79.26 | model=hist | error band=±6.76%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.20999908447266
- Current P/L: ₹-2100.00
- First forecast horizon at/above purchase price: 12M

- 3M: ₹73.78 | model=hist | error band=±17.38%
- 6M: ₹62.44 | model=hist | error band=±27.15%
- 9M: ₹48.18 | model=hist | error band=±60.10%
- 12M: ₹91.18 | model=hist | error band=±77.06%
- 18M: ₹172.24 | model=historical_median | error band=±202.30%
- 24M: ₹644.22 | model=hist | error band=±40.69%
- 36M: ₹575.01 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 366.8500061035156
- Current P/L: ₹-4963.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹373.60 | model=historical_median | error band=±12.16%
- 6M: ₹380.04 | model=historical_median | error band=±10.78%
- 9M: ₹376.35 | model=historical_median | error band=±14.33%
- 12M: ₹382.24 | model=historical_median | error band=±18.83%
- 18M: ₹486.44 | model=historical_median | error band=±44.88%
- 24M: ₹624.42 | model=historical_median | error band=±76.59%
- 36M: ₹456.24 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 165.1999969482422
- Current P/L: ₹-17053.10
- First forecast horizon at/above purchase price: 36M

- 3M: ₹172.50 | model=extra_trees | error band=±9.56%
- 6M: ₹160.22 | model=extra_trees | error band=±21.50%
- 9M: ₹142.92 | model=extra_trees | error band=±27.74%
- 12M: ₹159.44 | model=extra_trees | error band=±21.79%
- 18M: ₹180.51 | model=hist | error band=±29.78%
- 24M: ₹216.78 | model=historical_median | error band=±41.29%
- 36M: ₹236.16 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.20999908447266
- Current P/L: ₹-9162.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹87.10 | model=historical_median | error band=±18.12%
- 6M: ₹69.52 | model=extra_trees | error band=±16.72%
- 9M: ₹60.60 | model=extra_trees | error band=±26.21%
- 12M: ₹59.06 | model=extra_trees | error band=±40.49%
- 18M: ₹68.50 | model=hist | error band=±38.65%
- 24M: ₹115.93 | model=historical_median | error band=±61.31%
- 36M: ₹175.11 | model=historical_median | error band=±88.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 37.02000045776367
- Current P/L: ₹-38821.72
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.76 | model=historical_median | error band=±12.42%
- 6M: ₹26.14 | model=hist | error band=±16.46%
- 9M: ₹31.84 | model=hist | error band=±10.35%
- 12M: ₹33.95 | model=hist | error band=±16.00%
- 18M: ₹19.49 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 193.2700042724609
- Current P/L: ₹-6650.38
- First forecast horizon at/above purchase price: 24M

- 3M: ₹194.90 | model=historical_median | error band=±20.10%
- 6M: ₹172.90 | model=extra_trees | error band=±20.87%
- 9M: ₹202.58 | model=historical_median | error band=±20.33%
- 12M: ₹200.52 | model=historical_median | error band=±16.81%
- 18M: ₹218.95 | model=historical_median | error band=±29.46%
- 24M: ₹335.00 | model=extra_trees | error band=±28.45%
- 36M: ₹238.42 | model=hist | error band=±26.73%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.400001525878906
- Current P/L: ₹-3162.36
- First forecast horizon at/above purchase price: 36M

- 3M: ₹61.46 | model=historical_median | error band=±17.98%
- 6M: ₹62.60 | model=historical_median | error band=±25.60%
- 9M: ₹62.33 | model=historical_median | error band=±34.89%
- 12M: ₹64.04 | model=historical_median | error band=±38.32%
- 18M: ₹71.24 | model=historical_median | error band=±69.37%
- 24M: ₹81.78 | model=historical_median | error band=±86.61%
- 36M: ₹111.18 | model=historical_median | error band=±120.16%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.020000457763672
- Current P/L: ₹-42727.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.42 | model=historical_median | error band=±32.27%
- 6M: ₹21.82 | model=extra_trees | error band=±25.32%
- 9M: ₹20.18 | model=extra_trees | error band=±47.41%
- 12M: ₹21.40 | model=historical_median | error band=±59.35%
- 18M: ₹14.29 | model=extra_trees | error band=±97.85%
- 24M: ₹37.28 | model=historical_median | error band=±104.21%
- 36M: ₹47.68 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 470.9500122070313
- Current P/L: ₹-27001.65
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹427.62 | model=hist | error band=±14.96%
- 6M: ₹457.99 | model=historical_median | error band=±21.57%
- 9M: ₹464.85 | model=historical_median | error band=±32.40%
- 12M: ₹538.81 | model=historical_median | error band=±48.64%
- 18M: ₹605.15 | model=historical_median | error band=±68.18%
- 24M: ₹581.62 | model=historical_median | error band=±46.50%
- 36M: ₹368.88 | model=extra_trees | error band=±115.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.099999904632568
- Current P/L: ₹-6833.42
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.84 | model=historical_median | error band=±20.83%
- 6M: ₹5.11 | model=historical_median | error band=±21.88%
- 9M: ₹2.49 | model=extra_trees | error band=±48.03%
- 12M: ₹2.08 | model=extra_trees | error band=±53.68%
- 18M: ₹5.66 | model=historical_median | error band=±51.51%
- 24M: ₹6.08 | model=historical_median | error band=±62.18%
- 36M: ₹4.55 | model=historical_median | error band=±87.80%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
