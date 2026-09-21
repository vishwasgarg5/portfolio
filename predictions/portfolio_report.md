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
- Current price: 30.68000030517578
- Current P/L: ₹-1160.00
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
- Current price: 23.170000076293945
- Current P/L: ₹-360.80
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.18 | model=historical_median | error band=±17.82%
- 6M: ₹22.77 | model=historical_median | error band=±14.97%
- 9M: ₹22.37 | model=historical_median | error band=±23.03%
- 12M: ₹26.21 | model=extra_trees | error band=±21.54%
- 18M: ₹17.38 | model=historical_median | error band=±21.61%
- 24M: ₹25.10 | model=extra_trees | error band=±13.21%
- 36M: ₹25.60 | model=hist | error band=±16.31%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1247.4000244140625
- Current P/L: ₹-1027.26
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1266.17 | model=historical_median | error band=±14.10%
- 6M: ₹1297.46 | model=historical_median | error band=±21.97%
- 9M: ₹1399.31 | model=hist | error band=±25.66%
- 12M: ₹1516.57 | model=hist | error band=±26.03%
- 18M: ₹1229.28 | model=hist | error band=±33.73%
- 24M: ₹1372.50 | model=extra_trees | error band=±33.80%
- 36M: ₹1543.17 | model=extra_trees | error band=±43.51%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 326.3999938964844
- Current P/L: ₹-1060.28
- First forecast horizon at/above purchase price: 12M

- 3M: ₹337.77 | model=historical_median | error band=±15.08%
- 6M: ₹359.54 | model=historical_median | error band=±17.62%
- 9M: ₹361.29 | model=historical_median | error band=±18.85%
- 12M: ₹384.63 | model=historical_median | error band=±19.03%
- 18M: ₹423.88 | model=historical_median | error band=±22.56%
- 24M: ₹430.13 | model=historical_median | error band=±39.92%
- 36M: ₹493.99 | model=historical_median | error band=±51.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 111.0
- Current P/L: ₹-4725.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.26 | model=historical_median | error band=±6.74%
- 6M: ₹94.31 | model=historical_median | error band=±5.21%
- 9M: ₹91.32 | model=extra_trees | error band=±2.21%
- 12M: ₹81.76 | model=historical_median | error band=±2.73%
- 18M: ₹67.16 | model=hist | error band=±3.71%
- 24M: ₹79.24 | model=hist | error band=±6.77%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.22000122070312
- Current P/L: ₹-2098.00
- First forecast horizon at/above purchase price: 12M

- 3M: ₹73.78 | model=hist | error band=±17.38%
- 6M: ₹61.99 | model=hist | error band=±27.15%
- 9M: ₹49.13 | model=hist | error band=±60.10%
- 12M: ₹91.45 | model=hist | error band=±77.06%
- 18M: ₹172.27 | model=historical_median | error band=±202.30%
- 24M: ₹643.95 | model=hist | error band=±42.14%
- 36M: ₹570.12 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 367.1499938964844
- Current P/L: ₹-4942.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹373.91 | model=historical_median | error band=±12.16%
- 6M: ₹380.35 | model=historical_median | error band=±10.78%
- 9M: ₹376.66 | model=historical_median | error band=±14.33%
- 12M: ₹382.55 | model=historical_median | error band=±18.83%
- 18M: ₹486.84 | model=historical_median | error band=±44.88%
- 24M: ₹624.93 | model=historical_median | error band=±76.59%
- 36M: ₹451.37 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 164.5500030517578
- Current P/L: ₹-17254.60
- First forecast horizon at/above purchase price: 36M

- 3M: ₹171.85 | model=extra_trees | error band=±9.56%
- 6M: ₹158.69 | model=extra_trees | error band=±21.50%
- 9M: ₹143.05 | model=extra_trees | error band=±27.94%
- 12M: ₹159.84 | model=extra_trees | error band=±21.79%
- 18M: ₹179.40 | model=hist | error band=±29.78%
- 24M: ₹215.93 | model=historical_median | error band=±41.29%
- 36M: ₹235.23 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.88999938964844
- Current P/L: ₹-8958.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹87.82 | model=historical_median | error band=±18.12%
- 6M: ₹68.77 | model=extra_trees | error band=±16.72%
- 9M: ₹60.66 | model=extra_trees | error band=±26.21%
- 12M: ₹59.59 | model=extra_trees | error band=±40.49%
- 18M: ₹63.93 | model=hist | error band=±49.29%
- 24M: ₹116.70 | model=historical_median | error band=±61.31%
- 36M: ₹176.44 | model=historical_median | error band=±88.25%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 37.0
- Current P/L: ₹-38878.56
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.74 | model=historical_median | error band=±12.42%
- 6M: ₹26.22 | model=hist | error band=±16.46%
- 9M: ₹31.86 | model=hist | error band=±10.35%
- 12M: ₹34.05 | model=hist | error band=±16.01%
- 18M: ₹19.50 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 193.5
- Current P/L: ₹-6630.60
- First forecast horizon at/above purchase price: 24M

- 3M: ₹195.10 | model=historical_median | error band=±20.10%
- 6M: ₹173.01 | model=extra_trees | error band=±20.87%
- 9M: ₹202.83 | model=historical_median | error band=±20.33%
- 12M: ₹200.72 | model=historical_median | error band=±16.79%
- 18M: ₹219.29 | model=historical_median | error band=±29.46%
- 24M: ₹337.26 | model=extra_trees | error band=±28.54%
- 36M: ₹237.85 | model=hist | error band=±26.22%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.34999847412109
- Current P/L: ₹-3166.01
- First forecast horizon at/above purchase price: 36M

- 3M: ₹61.41 | model=historical_median | error band=±17.98%
- 6M: ₹62.55 | model=historical_median | error band=±25.80%
- 9M: ₹62.28 | model=historical_median | error band=±34.89%
- 12M: ₹63.99 | model=historical_median | error band=±38.32%
- 18M: ₹71.19 | model=historical_median | error band=±66.42%
- 24M: ₹81.95 | model=historical_median | error band=±86.61%
- 36M: ₹111.09 | model=historical_median | error band=±116.68%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.0
- Current P/L: ₹-42772.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.40 | model=historical_median | error band=±32.27%
- 6M: ₹21.78 | model=extra_trees | error band=±25.32%
- 9M: ₹20.14 | model=extra_trees | error band=±47.41%
- 12M: ₹21.38 | model=historical_median | error band=±59.35%
- 18M: ₹14.57 | model=extra_trees | error band=±97.85%
- 24M: ₹37.25 | model=historical_median | error band=±104.21%
- 36M: ₹47.63 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 470.7000122070313
- Current P/L: ₹-27016.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹426.17 | model=hist | error band=±14.96%
- 6M: ₹457.75 | model=historical_median | error band=±21.57%
- 9M: ₹464.60 | model=historical_median | error band=±32.40%
- 12M: ₹538.53 | model=historical_median | error band=±48.64%
- 18M: ₹604.83 | model=historical_median | error band=±68.18%
- 24M: ₹581.31 | model=historical_median | error band=±46.50%
- 36M: ₹368.33 | model=extra_trees | error band=±115.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.090000152587891
- Current P/L: ₹-6843.21
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.83 | model=historical_median | error band=±20.83%
- 6M: ₹5.10 | model=historical_median | error band=±21.88%
- 9M: ₹2.49 | model=extra_trees | error band=±48.03%
- 12M: ₹2.09 | model=extra_trees | error band=±53.68%
- 18M: ₹5.65 | model=historical_median | error band=±51.51%
- 24M: ₹6.07 | model=historical_median | error band=±62.18%
- 36M: ₹4.55 | model=historical_median | error band=±87.80%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
