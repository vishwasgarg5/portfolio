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
- Current price: 25.5
- Current P/L: ₹-6340.00
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
- Current price: 15.149999618530272
- Current P/L: ₹-7594.84
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.12 | model=historical_median | error band=±17.82%
- 6M: ₹14.90 | model=historical_median | error band=±14.98%
- 9M: ₹14.52 | model=historical_median | error band=±23.03%
- 12M: ₹15.32 | model=extra_trees | error band=±21.57%
- 18M: ₹11.56 | model=historical_median | error band=±21.99%
- 24M: ₹12.27 | model=extra_trees | error band=±13.12%
- 36M: ₹3.65 | model=hist | error band=±16.17%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1164.9000244140625
- Current P/L: ₹-2099.76
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1179.84 | model=historical_median | error band=±14.10%
- 6M: ₹1206.98 | model=historical_median | error band=±21.97%
- 9M: ₹1383.95 | model=hist | error band=±25.66%
- 12M: ₹1387.83 | model=hist | error band=±26.03%
- 18M: ₹1408.50 | model=historical_median | error band=±33.73%
- 24M: ₹1427.36 | model=extra_trees | error band=±37.63%
- 36M: ₹2101.73 | model=historical_median | error band=±43.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 316.25
- Current P/L: ₹-1324.18
- First forecast horizon at/above purchase price: 18M

- 3M: ₹326.56 | model=historical_median | error band=±15.08%
- 6M: ₹341.84 | model=historical_median | error band=±23.64%
- 9M: ₹348.32 | model=historical_median | error band=±18.85%
- 12M: ₹366.84 | model=historical_median | error band=±19.03%
- 18M: ₹417.30 | model=historical_median | error band=±22.96%
- 24M: ₹418.39 | model=historical_median | error band=±48.43%
- 36M: ₹487.87 | model=historical_median | error band=±54.03%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 99.5
- Current P/L: ₹-8750.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹101.60 | model=extra_trees | error band=±5.99%
- 6M: ₹93.75 | model=hist | error band=±5.38%
- 9M: ₹81.53 | model=extra_trees | error band=±2.26%
- 12M: ₹73.50 | model=historical_median | error band=±2.73%
- 18M: ₹63.71 | model=hist | error band=±3.83%
- 24M: ₹49.43 | model=extra_trees | error band=±8.52%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 73.37000274658203
- Current P/L: ₹-3468.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹65.69 | model=hist | error band=±15.02%
- 6M: ₹62.56 | model=hist | error band=±30.77%
- 9M: ₹72.83 | model=hist | error band=±59.54%
- 12M: ₹84.16 | model=hist | error band=±74.35%
- 18M: ₹149.74 | model=historical_median | error band=±206.23%
- 24M: ₹276.15 | model=hist | error band=±55.47%
- 36M: ₹555.35 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 345.04998779296875
- Current P/L: ₹-6489.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹350.68 | model=historical_median | error band=±12.16%
- 6M: ₹354.09 | model=historical_median | error band=±17.04%
- 9M: ₹353.79 | model=historical_median | error band=±14.33%
- 12M: ₹352.27 | model=historical_median | error band=±17.45%
- 18M: ₹466.09 | model=historical_median | error band=±43.39%
- 24M: ₹564.87 | model=historical_median | error band=±79.04%
- 36M: ₹596.76 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 198.30999755859372
- Current P/L: ₹-6789.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹179.31 | model=extra_trees | error band=±9.56%
- 6M: ₹165.96 | model=extra_trees | error band=±21.50%
- 9M: ₹158.86 | model=extra_trees | error band=±27.74%
- 12M: ₹179.52 | model=extra_trees | error band=±24.66%
- 18M: ₹129.27 | model=hist | error band=±29.78%
- 24M: ₹257.98 | model=historical_median | error band=±45.45%
- 36M: ₹278.41 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.86000061035156
- Current P/L: ₹-10467.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹82.53 | model=historical_median | error band=±18.12%
- 6M: ₹72.88 | model=extra_trees | error band=±16.41%
- 9M: ₹63.98 | model=extra_trees | error band=±26.21%
- 12M: ₹62.00 | model=extra_trees | error band=±40.49%
- 18M: ₹60.97 | model=hist | error band=±38.65%
- 24M: ₹86.44 | model=hist | error band=±66.34%
- 36M: ₹165.15 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 33.18000030517578
- Current P/L: ₹-49735.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹27.53 | model=historical_median | error band=±12.32%
- 6M: ₹22.89 | model=extra_trees | error band=±16.44%
- 9M: ₹23.29 | model=hist | error band=±9.69%
- 12M: ₹19.95 | model=historical_median | error band=±5.75%
- 18M: ₹17.75 | model=hist | error band=±3.76%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 171.10000610351562
- Current P/L: ₹-8557.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹170.07 | model=historical_median | error band=±20.77%
- 6M: ₹165.21 | model=extra_trees | error band=±20.87%
- 9M: ₹174.44 | model=historical_median | error band=±23.72%
- 12M: ₹176.01 | model=historical_median | error band=±16.77%
- 18M: ₹194.43 | model=historical_median | error band=±29.46%
- 24M: ₹278.56 | model=extra_trees | error band=±28.46%
- 36M: ₹234.16 | model=historical_median | error band=±26.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 53.38999938964844
- Current P/L: ₹-3893.09
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹51.67 | model=historical_median | error band=±17.98%
- 6M: ₹51.75 | model=historical_median | error band=±29.42%
- 9M: ₹52.36 | model=historical_median | error band=±34.89%
- 12M: ₹53.64 | model=historical_median | error band=±42.65%
- 18M: ₹60.27 | model=historical_median | error band=±66.42%
- 24M: ₹67.91 | model=historical_median | error band=±86.22%
- 36M: ₹94.17 | model=historical_median | error band=±98.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.90999984741211
- Current P/L: ₹-49725.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹16.96 | model=historical_median | error band=±31.94%
- 6M: ₹17.30 | model=historical_median | error band=±27.30%
- 9M: ₹16.67 | model=historical_median | error band=±45.34%
- 12M: ₹17.97 | model=historical_median | error band=±61.50%
- 18M: ₹20.56 | model=historical_median | error band=±129.41%
- 24M: ₹38.22 | model=hist | error band=±99.85%
- 36M: ₹42.04 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 436.2000122070313
- Current P/L: ₹-29121.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹403.28 | model=extra_trees | error band=±14.96%
- 6M: ₹423.96 | model=historical_median | error band=±21.31%
- 9M: ₹426.90 | model=historical_median | error band=±32.40%
- 12M: ₹488.19 | model=historical_median | error band=±48.64%
- 18M: ₹556.29 | model=historical_median | error band=±68.18%
- 24M: ₹530.99 | model=historical_median | error band=±65.73%
- 36M: ₹561.76 | model=extra_trees | error band=±104.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.800000190734863
- Current P/L: ₹-7127.12
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.63 | model=historical_median | error band=±15.24%
- 6M: ₹4.66 | model=historical_median | error band=±21.60%
- 9M: ₹2.88 | model=hist | error band=±54.31%
- 12M: ₹2.37 | model=extra_trees | error band=±49.47%
- 18M: ₹5.31 | model=historical_median | error band=±55.81%
- 24M: ₹5.38 | model=historical_median | error band=±65.43%
- 36M: ₹4.36 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
