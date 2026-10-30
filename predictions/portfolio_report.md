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
- 6M: ₹14.83 | model=historical_median | error band=±14.97%
- 9M: ₹14.52 | model=historical_median | error band=±23.03%
- 12M: ₹15.37 | model=extra_trees | error band=±21.99%
- 18M: ₹11.56 | model=historical_median | error band=±22.09%
- 24M: ₹12.34 | model=extra_trees | error band=±13.09%
- 36M: ₹3.38 | model=hist | error band=±16.15%

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
- 24M: ₹1427.07 | model=extra_trees | error band=±37.53%
- 36M: ₹2102.26 | model=historical_median | error band=±43.14%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 316.25
- Current P/L: ₹-1324.18
- First forecast horizon at/above purchase price: 18M

- 3M: ₹326.48 | model=historical_median | error band=±15.08%
- 6M: ₹341.86 | model=historical_median | error band=±23.64%
- 9M: ₹348.32 | model=historical_median | error band=±18.85%
- 12M: ₹365.69 | model=historical_median | error band=±19.03%
- 18M: ₹416.48 | model=historical_median | error band=±22.96%
- 24M: ₹418.33 | model=historical_median | error band=±48.51%
- 36M: ₹488.32 | model=historical_median | error band=±55.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 99.5
- Current P/L: ₹-8750.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹101.62 | model=extra_trees | error band=±5.99%
- 6M: ₹93.95 | model=hist | error band=±5.07%
- 9M: ₹81.54 | model=extra_trees | error band=±2.25%
- 12M: ₹73.50 | model=historical_median | error band=±2.73%
- 18M: ₹63.71 | model=hist | error band=±3.69%
- 24M: ₹49.43 | model=extra_trees | error band=±8.54%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 73.37000274658203
- Current P/L: ₹-3468.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹65.62 | model=hist | error band=±13.88%
- 6M: ₹69.28 | model=historical_median | error band=±30.76%
- 9M: ₹82.86 | model=hist | error band=±59.54%
- 12M: ₹67.90 | model=hist | error band=±74.35%
- 18M: ₹149.74 | model=historical_median | error band=±206.23%
- 24M: ₹297.36 | model=hist | error band=±174.22%
- 36M: ₹493.56 | model=hist | error band=±300.62%

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
- 36M: ₹595.91 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 198.30999755859372
- Current P/L: ₹-6789.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹179.49 | model=extra_trees | error band=±9.56%
- 6M: ₹166.33 | model=extra_trees | error band=±21.50%
- 9M: ₹159.18 | model=extra_trees | error band=±27.76%
- 12M: ₹179.76 | model=extra_trees | error band=±24.61%
- 18M: ₹128.52 | model=hist | error band=±29.78%
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
- 6M: ₹72.90 | model=extra_trees | error band=±16.41%
- 9M: ₹63.96 | model=extra_trees | error band=±26.21%
- 12M: ₹62.00 | model=extra_trees | error band=±40.49%
- 18M: ₹60.90 | model=hist | error band=±38.65%
- 24M: ₹87.72 | model=hist | error band=±66.34%
- 36M: ₹165.15 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 33.18000030517578
- Current P/L: ₹-49735.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹27.53 | model=historical_median | error band=±12.25%
- 6M: ₹22.92 | model=extra_trees | error band=±16.40%
- 9M: ₹23.30 | model=hist | error band=±9.69%
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
- 6M: ₹164.79 | model=extra_trees | error band=±20.87%
- 9M: ₹174.50 | model=historical_median | error band=±23.71%
- 12M: ₹176.01 | model=historical_median | error band=±16.74%
- 18M: ₹194.30 | model=historical_median | error band=±29.46%
- 24M: ₹278.92 | model=extra_trees | error band=±28.45%
- 36M: ₹234.48 | model=historical_median | error band=±26.67%

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
- 18M: ₹60.27 | model=historical_median | error band=±60.32%
- 24M: ₹67.89 | model=historical_median | error band=±86.22%
- 36M: ₹94.17 | model=historical_median | error band=±95.54%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.90999984741211
- Current P/L: ₹-49725.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹16.96 | model=historical_median | error band=±31.94%
- 6M: ₹17.29 | model=historical_median | error band=±27.28%
- 9M: ₹16.66 | model=historical_median | error band=±45.34%
- 12M: ₹17.96 | model=historical_median | error band=±61.50%
- 18M: ₹20.70 | model=historical_median | error band=±129.60%
- 24M: ₹37.84 | model=hist | error band=±99.85%
- 36M: ₹42.08 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 436.2000122070313
- Current P/L: ₹-29121.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹402.25 | model=extra_trees | error band=±14.96%
- 6M: ₹423.96 | model=historical_median | error band=±21.31%
- 9M: ₹426.90 | model=historical_median | error band=±32.43%
- 12M: ₹488.19 | model=historical_median | error band=±48.64%
- 18M: ₹556.29 | model=historical_median | error band=±68.18%
- 24M: ₹530.99 | model=historical_median | error band=±66.48%
- 36M: ₹558.46 | model=extra_trees | error band=±104.10%

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
- 9M: ₹3.00 | model=hist | error band=±54.31%
- 12M: ₹2.37 | model=extra_trees | error band=±49.47%
- 18M: ₹5.31 | model=historical_median | error band=±55.81%
- 24M: ₹5.38 | model=historical_median | error band=±65.43%
- 36M: ₹4.36 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
