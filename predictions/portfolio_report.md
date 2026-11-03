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
- Current price: 26.0
- Current P/L: ₹-5840.00
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
- Current price: 15.380000114440918
- Current P/L: ₹-7387.38
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.35 | model=historical_median | error band=±17.82%
- 6M: ₹15.08 | model=historical_median | error band=±14.98%
- 9M: ₹14.74 | model=historical_median | error band=±19.95%
- 12M: ₹15.23 | model=extra_trees | error band=±21.40%
- 18M: ₹11.71 | model=historical_median | error band=±21.50%
- 24M: ₹12.46 | model=extra_trees | error band=±13.26%
- 36M: ₹4.13 | model=hist | error band=±16.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1307.9000244140625
- Current P/L: ₹-240.76
- First forecast horizon at/above purchase price: 6M

- 3M: ₹1324.68 | model=historical_median | error band=±14.10%
- 6M: ₹1354.99 | model=historical_median | error band=±21.97%
- 9M: ₹1566.62 | model=hist | error band=±25.66%
- 12M: ₹2183.29 | model=hist | error band=±26.03%
- 18M: ₹1581.17 | model=historical_median | error band=±33.73%
- 24M: ₹2081.51 | model=extra_trees | error band=±37.53%
- 36M: ₹2358.11 | model=historical_median | error band=±43.22%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 321.54998779296875
- Current P/L: ₹-1186.38
- First forecast horizon at/above purchase price: 12M

- 3M: ₹331.93 | model=historical_median | error band=±15.08%
- 6M: ₹347.48 | model=historical_median | error band=±23.64%
- 9M: ₹354.10 | model=historical_median | error band=±18.85%
- 12M: ₹373.12 | model=historical_median | error band=±19.03%
- 18M: ₹424.96 | model=historical_median | error band=±22.96%
- 24M: ₹426.14 | model=historical_median | error band=±48.50%
- 36M: ₹496.73 | model=historical_median | error band=±54.65%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 102.3000030517578
- Current P/L: ₹-7770.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.19 | model=extra_trees | error band=±5.99%
- 6M: ₹94.65 | model=hist | error band=±4.95%
- 9M: ₹82.26 | model=extra_trees | error band=±2.25%
- 12M: ₹75.62 | model=historical_median | error band=±2.73%
- 18M: ₹63.33 | model=hist | error band=±3.83%
- 24M: ₹50.13 | model=extra_trees | error band=±7.69%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 75.9000015258789
- Current P/L: ₹-2962.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹61.55 | model=hist | error band=±12.86%
- 6M: ₹60.47 | model=hist | error band=±30.77%
- 9M: ₹69.14 | model=hist | error band=±59.58%
- 12M: ₹57.33 | model=hist | error band=±74.35%
- 18M: ₹154.88 | model=historical_median | error band=±206.23%
- 24M: ₹211.41 | model=hist | error band=±33.09%
- 36M: ₹583.93 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 356.54998779296875
- Current P/L: ₹-5684.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹362.36 | model=historical_median | error band=±12.16%
- 6M: ₹365.83 | model=historical_median | error band=±17.04%
- 9M: ₹365.56 | model=historical_median | error band=±14.33%
- 12M: ₹363.88 | model=historical_median | error band=±17.45%
- 18M: ₹479.65 | model=historical_median | error band=±43.39%
- 24M: ₹583.97 | model=historical_median | error band=±79.04%
- 36M: ₹559.44 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 198.0
- Current P/L: ₹-6885.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹179.64 | model=extra_trees | error band=±9.56%
- 6M: ₹168.85 | model=extra_trees | error band=±21.50%
- 9M: ₹161.67 | model=extra_trees | error band=±27.73%
- 12M: ₹178.88 | model=extra_trees | error band=±24.73%
- 18M: ₹137.22 | model=hist | error band=±29.78%
- 24M: ₹257.88 | model=historical_median | error band=±45.45%
- 36M: ₹277.70 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.93000030517578
- Current P/L: ₹-10446.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹82.58 | model=historical_median | error band=±18.12%
- 6M: ₹74.16 | model=extra_trees | error band=±16.41%
- 9M: ₹62.84 | model=extra_trees | error band=±26.21%
- 12M: ₹64.78 | model=extra_trees | error band=±40.49%
- 18M: ₹82.68 | model=hist | error band=±38.65%
- 24M: ₹108.52 | model=historical_median | error band=±66.34%
- 36M: ₹164.94 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 34.59000015258789
- Current P/L: ₹-45727.78
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.73 | model=historical_median | error band=±12.25%
- 6M: ₹21.65 | model=hist | error band=±16.48%
- 9M: ₹23.08 | model=hist | error band=±9.69%
- 12M: ₹20.93 | model=historical_median | error band=±5.69%
- 18M: ₹17.59 | model=hist | error band=±4.06%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 175.4600067138672
- Current P/L: ₹-8182.04
- First forecast horizon at/above purchase price: 24M

- 3M: ₹174.44 | model=historical_median | error band=±20.77%
- 6M: ₹163.38 | model=extra_trees | error band=±20.87%
- 9M: ₹178.92 | model=historical_median | error band=±23.71%
- 12M: ₹180.66 | model=historical_median | error band=±16.76%
- 18M: ₹199.39 | model=historical_median | error band=±29.46%
- 24M: ₹293.62 | model=extra_trees | error band=±28.50%
- 36M: ₹240.47 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 55.7599983215332
- Current P/L: ₹-3720.08
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹49.41 | model=extra_trees | error band=±17.98%
- 6M: ₹54.04 | model=historical_median | error band=±29.42%
- 9M: ₹54.68 | model=historical_median | error band=±34.89%
- 12M: ₹56.02 | model=historical_median | error band=±42.65%
- 18M: ₹62.96 | model=historical_median | error band=±60.32%
- 24M: ₹70.93 | model=historical_median | error band=±86.22%
- 36M: ₹98.38 | model=historical_median | error band=±95.86%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.280000686645508
- Current P/L: ₹-48892.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.32 | model=historical_median | error band=±31.94%
- 6M: ₹17.67 | model=historical_median | error band=±27.32%
- 9M: ₹17.01 | model=historical_median | error band=±45.34%
- 12M: ₹18.31 | model=historical_median | error band=±61.50%
- 18M: ₹20.86 | model=historical_median | error band=±129.57%
- 24M: ₹34.13 | model=hist | error band=±99.85%
- 36M: ₹43.01 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 447.5
- Current P/L: ₹-28432.10
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹399.67 | model=extra_trees | error band=±14.99%
- 6M: ₹434.89 | model=historical_median | error band=±21.31%
- 9M: ₹437.93 | model=historical_median | error band=±32.40%
- 12M: ₹499.68 | model=historical_median | error band=±48.64%
- 18M: ₹570.65 | model=historical_median | error band=±68.18%
- 24M: ₹543.95 | model=historical_median | error band=±65.73%
- 36M: ₹623.59 | model=extra_trees | error band=±104.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.78000020980835
- Current P/L: ₹-7146.70
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.61 | model=historical_median | error band=±15.24%
- 6M: ₹4.65 | model=historical_median | error band=±21.60%
- 9M: ₹2.81 | model=hist | error band=±54.31%
- 12M: ₹2.66 | model=extra_trees | error band=±49.47%
- 18M: ₹5.28 | model=historical_median | error band=±55.81%
- 24M: ₹5.32 | model=historical_median | error band=±65.43%
- 36M: ₹4.35 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
