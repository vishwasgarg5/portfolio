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
- Current price: 25.290000915527344
- Current P/L: ₹-6550.00
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
- Current price: 15.43000030517578
- Current P/L: ₹-7342.28
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.40 | model=historical_median | error band=±17.82%
- 6M: ₹15.10 | model=historical_median | error band=±14.98%
- 9M: ₹14.79 | model=historical_median | error band=±23.03%
- 12M: ₹16.30 | model=extra_trees | error band=±21.88%
- 18M: ₹11.80 | model=historical_median | error band=±21.90%
- 24M: ₹13.01 | model=extra_trees | error band=±13.05%
- 36M: ₹3.83 | model=hist | error band=±16.27%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1167.4000244140625
- Current P/L: ₹-2067.26
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1182.42 | model=historical_median | error band=±14.10%
- 6M: ₹1209.57 | model=historical_median | error band=±21.97%
- 9M: ₹1366.19 | model=hist | error band=±25.66%
- 12M: ₹1347.70 | model=hist | error band=±26.03%
- 18M: ₹1411.52 | model=historical_median | error band=±33.73%
- 24M: ₹1401.42 | model=extra_trees | error band=±37.53%
- 36M: ₹2106.41 | model=historical_median | error band=±43.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 310.5
- Current P/L: ₹-1473.68
- First forecast horizon at/above purchase price: 18M

- 3M: ₹320.56 | model=historical_median | error band=±15.08%
- 6M: ₹335.61 | model=historical_median | error band=±23.64%
- 9M: ₹342.21 | model=historical_median | error band=±18.85%
- 12M: ₹359.75 | model=historical_median | error band=±19.03%
- 18M: ₹408.90 | model=historical_median | error band=±22.96%
- 24M: ₹413.28 | model=historical_median | error band=±48.53%
- 36M: ₹480.15 | model=historical_median | error band=±54.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 101.1999969482422
- Current P/L: ₹-8155.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.52 | model=extra_trees | error band=±5.99%
- 6M: ₹94.69 | model=hist | error band=±5.05%
- 9M: ₹82.81 | model=extra_trees | error band=±2.25%
- 12M: ₹74.68 | model=historical_median | error band=±2.73%
- 18M: ₹65.00 | model=hist | error band=±3.80%
- 24M: ₹50.15 | model=extra_trees | error band=±8.99%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 75.70999908447266
- Current P/L: ₹-3000.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹64.14 | model=hist | error band=±13.94%
- 6M: ₹71.52 | model=historical_median | error band=±30.70%
- 9M: ₹78.26 | model=hist | error band=±59.43%
- 12M: ₹83.73 | model=hist | error band=±74.42%
- 18M: ₹154.58 | model=historical_median | error band=±206.23%
- 24M: ₹401.22 | model=hist | error band=±111.64%
- 36M: ₹511.91 | model=hist | error band=±258.95%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 344.54998779296875
- Current P/L: ₹-6524.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹350.24 | model=historical_median | error band=±12.16%
- 6M: ₹353.58 | model=historical_median | error band=±17.04%
- 9M: ₹353.29 | model=historical_median | error band=±14.33%
- 12M: ₹351.78 | model=historical_median | error band=±17.45%
- 18M: ₹465.41 | model=historical_median | error band=±43.39%
- 24M: ₹564.06 | model=historical_median | error band=±79.04%
- 36M: ₹601.50 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 190.1000061035156
- Current P/L: ₹-9334.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.43 | model=extra_trees | error band=±9.56%
- 6M: ₹156.66 | model=extra_trees | error band=±21.50%
- 9M: ₹146.46 | model=extra_trees | error band=±27.54%
- 12M: ₹169.72 | model=extra_trees | error band=±24.76%
- 18M: ₹124.98 | model=hist | error band=±29.78%
- 24M: ₹247.30 | model=historical_median | error band=±45.45%
- 36M: ₹267.39 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.83999633789062
- Current P/L: ₹-10473.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹82.51 | model=historical_median | error band=±18.12%
- 6M: ₹74.01 | model=extra_trees | error band=±16.41%
- 9M: ₹63.83 | model=extra_trees | error band=±26.21%
- 12M: ₹62.39 | model=extra_trees | error band=±40.49%
- 18M: ₹98.19 | model=historical_median | error band=±38.65%
- 24M: ₹108.56 | model=historical_median | error band=±66.34%
- 36M: ₹165.19 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 35.15999984741211
- Current P/L: ₹-44107.84
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.11 | model=historical_median | error band=±12.31%
- 6M: ₹23.04 | model=extra_trees | error band=±16.43%
- 9M: ₹22.25 | model=hist | error band=±9.69%
- 12M: ₹21.11 | model=historical_median | error band=±6.29%
- 18M: ₹17.93 | model=hist | error band=±4.12%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 163.00999450683594
- Current P/L: ₹-9252.74
- First forecast horizon at/above purchase price: 24M

- 3M: ₹162.03 | model=historical_median | error band=±20.77%
- 6M: ₹157.83 | model=extra_trees | error band=±20.87%
- 9M: ₹166.32 | model=historical_median | error band=±23.71%
- 12M: ₹167.69 | model=historical_median | error band=±16.76%
- 18M: ₹185.16 | model=historical_median | error band=±29.46%
- 24M: ₹278.33 | model=extra_trees | error band=±28.46%
- 36M: ₹223.69 | model=historical_median | error band=±26.32%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 52.400001525878906
- Current P/L: ₹-3965.36
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹50.72 | model=historical_median | error band=±17.98%
- 6M: ₹50.87 | model=historical_median | error band=±29.42%
- 9M: ₹51.39 | model=historical_median | error band=±34.89%
- 12M: ₹52.68 | model=historical_median | error band=±42.65%
- 18M: ₹59.15 | model=historical_median | error band=±66.42%
- 24M: ₹67.19 | model=historical_median | error band=±86.22%
- 36M: ₹92.39 | model=historical_median | error band=±95.30%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.979999542236328
- Current P/L: ₹-47317.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.97 | model=historical_median | error band=±31.94%
- 6M: ₹18.34 | model=historical_median | error band=±27.37%
- 9M: ₹17.66 | model=historical_median | error band=±45.34%
- 12M: ₹18.99 | model=historical_median | error band=±61.50%
- 18M: ₹21.83 | model=historical_median | error band=±129.53%
- 24M: ₹10.64 | model=hist | error band=±99.85%
- 36M: ₹44.57 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 444.0499877929688
- Current P/L: ₹-28642.55
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹404.82 | model=extra_trees | error band=±14.99%
- 6M: ₹431.64 | model=historical_median | error band=±21.31%
- 9M: ₹434.61 | model=historical_median | error band=±32.43%
- 12M: ₹497.52 | model=historical_median | error band=±48.64%
- 18M: ₹566.39 | model=historical_median | error band=±68.18%
- 24M: ₹541.37 | model=historical_median | error band=±67.70%
- 36M: ₹542.06 | model=extra_trees | error band=±103.74%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.949999809265137
- Current P/L: ₹-6980.27
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.71 | model=historical_median | error band=±15.24%
- 6M: ₹4.80 | model=historical_median | error band=±21.60%
- 9M: ₹2.99 | model=hist | error band=±54.31%
- 12M: ₹2.33 | model=extra_trees | error band=±49.47%
- 18M: ₹5.48 | model=historical_median | error band=±55.81%
- 24M: ₹5.56 | model=historical_median | error band=±65.43%
- 36M: ₹4.49 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
