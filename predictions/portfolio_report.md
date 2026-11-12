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
- Current price: 26.46999931335449
- Current P/L: ₹-5370.00
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
- Current price: 17.690000534057617
- Current P/L: ₹-5303.76
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.65 | model=historical_median | error band=±17.82%
- 6M: ₹17.30 | model=historical_median | error band=±14.98%
- 9M: ₹16.92 | model=historical_median | error band=±23.03%
- 12M: ₹18.31 | model=extra_trees | error band=±21.49%
- 18M: ₹13.56 | model=historical_median | error band=±21.49%
- 24M: ₹15.15 | model=extra_trees | error band=±13.26%
- 36M: ₹8.96 | model=hist | error band=±16.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1339.699951171875
- Current P/L: ₹172.64
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1356.65 | model=historical_median | error band=±14.10%
- 6M: ₹1387.46 | model=historical_median | error band=±21.97%
- 9M: ₹1359.45 | model=hist | error band=±25.66%
- 12M: ₹1433.23 | model=hist | error band=±26.03%
- 18M: ₹1778.41 | model=hist | error band=±33.73%
- 24M: ₹1552.73 | model=extra_trees | error band=±37.78%
- 36M: ₹2410.85 | model=historical_median | error band=±43.08%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.0
- Current P/L: ₹-1148.68
- First forecast horizon at/above purchase price: 12M

- 3M: ₹332.72 | model=historical_median | error band=±15.11%
- 6M: ₹347.00 | model=historical_median | error band=±23.69%
- 9M: ₹355.45 | model=historical_median | error band=±18.92%
- 12M: ₹374.64 | model=historical_median | error band=±19.08%
- 18M: ₹426.98 | model=historical_median | error band=±23.13%
- 24M: ₹427.12 | model=historical_median | error band=±46.74%
- 36M: ₹495.09 | model=historical_median | error band=±59.01%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 119.8499984741211
- Current P/L: ₹-1627.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹92.32 | model=hist | error band=±5.99%
- 6M: ₹95.87 | model=hist | error band=±9.03%
- 9M: ₹86.42 | model=extra_trees | error band=±2.25%
- 12M: ₹88.46 | model=historical_median | error band=±2.65%
- 18M: ₹66.85 | model=hist | error band=±3.88%
- 24M: ₹64.69 | model=extra_trees | error band=±6.84%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 85.29000091552734
- Current P/L: ₹-1084.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹68.59 | model=hist | error band=±12.89%
- 6M: ₹68.06 | model=hist | error band=±30.77%
- 9M: ₹59.43 | model=hist | error band=±59.58%
- 12M: ₹59.66 | model=hist | error band=±74.04%
- 18M: ₹164.14 | model=historical_median | error band=±205.32%
- 24M: ₹144.25 | model=hist | error band=±56.96%
- 36M: ₹693.46 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 357.0
- Current P/L: ₹-5652.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹362.80 | model=historical_median | error band=±12.16%
- 6M: ₹366.09 | model=historical_median | error band=±17.04%
- 9M: ₹365.89 | model=historical_median | error band=±14.33%
- 12M: ₹363.71 | model=historical_median | error band=±17.45%
- 18M: ₹479.85 | model=historical_median | error band=±43.39%
- 24M: ₹585.57 | model=historical_median | error band=±79.04%
- 36M: ₹571.62 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 196.1999969482422
- Current P/L: ₹-7443.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹190.46 | model=extra_trees | error band=±9.56%
- 6M: ₹185.49 | model=extra_trees | error band=±21.50%
- 9M: ₹181.51 | model=extra_trees | error band=±27.67%
- 12M: ₹186.47 | model=extra_trees | error band=±24.68%
- 18M: ₹191.64 | model=hist | error band=±29.78%
- 24M: ₹255.63 | model=historical_median | error band=±45.45%
- 36M: ₹274.32 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.0
- Current P/L: ₹-11025.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹79.95 | model=historical_median | error band=±18.12%
- 6M: ₹82.36 | model=extra_trees | error band=±16.41%
- 9M: ₹75.86 | model=extra_trees | error band=±26.21%
- 12M: ₹76.91 | model=extra_trees | error band=±40.49%
- 18M: ₹141.50 | model=hist | error band=±38.65%
- 24M: ₹108.12 | model=hist | error band=±66.34%
- 36M: ₹160.70 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 35.7400016784668
- Current P/L: ₹-42459.48
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.81 | model=historical_median | error band=±12.25%
- 6M: ₹26.04 | model=extra_trees | error band=±15.52%
- 9M: ₹24.26 | model=hist | error band=±9.69%
- 12M: ₹24.61 | model=historical_median | error band=±4.70%
- 18M: ₹18.25 | model=hist | error band=±4.55%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 176.2100067138672
- Current P/L: ₹-8117.54
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.35 | model=historical_median | error band=±20.77%
- 6M: ₹163.55 | model=extra_trees | error band=±20.87%
- 9M: ₹179.45 | model=historical_median | error band=±23.71%
- 12M: ₹179.64 | model=historical_median | error band=±23.36%
- 18M: ₹193.63 | model=historical_median | error band=±26.28%
- 24M: ₹281.76 | model=extra_trees | error band=±28.22%
- 36M: ₹240.81 | model=historical_median | error band=±37.19%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 58.52999877929688
- Current P/L: ₹-3517.87
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹52.84 | model=extra_trees | error band=±17.98%
- 6M: ₹56.69 | model=historical_median | error band=±29.42%
- 9M: ₹57.36 | model=historical_median | error band=±34.89%
- 12M: ₹58.77 | model=historical_median | error band=±42.65%
- 18M: ₹66.14 | model=historical_median | error band=±66.42%
- 24M: ₹75.40 | model=historical_median | error band=±86.22%
- 36M: ₹103.49 | model=historical_median | error band=±96.74%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 19.280000686645508
- Current P/L: ₹-46642.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹18.27 | model=historical_median | error band=±31.94%
- 6M: ₹18.66 | model=historical_median | error band=±27.25%
- 9M: ₹17.94 | model=historical_median | error band=±45.34%
- 12M: ₹19.39 | model=historical_median | error band=±61.50%
- 18M: ₹22.25 | model=historical_median | error band=±129.56%
- 24M: ₹19.26 | model=hist | error band=±99.85%
- 36M: ₹45.56 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 470.9500122070313
- Current P/L: ₹-27001.65
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹469.47 | model=extra_trees | error band=±14.96%
- 6M: ₹457.45 | model=historical_median | error band=±21.31%
- 9M: ₹459.41 | model=historical_median | error band=±32.40%
- 12M: ₹524.80 | model=historical_median | error band=±48.64%
- 18M: ₹599.50 | model=historical_median | error band=±68.18%
- 24M: ₹570.91 | model=historical_median | error band=±65.73%
- 36M: ₹833.19 | model=hist | error band=±114.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.070000171661377
- Current P/L: ₹-6862.79
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.87 | model=historical_median | error band=±15.24%
- 6M: ₹4.93 | model=historical_median | error band=±21.60%
- 9M: ₹2.88 | model=hist | error band=±54.31%
- 12M: ₹2.77 | model=hist | error band=±49.47%
- 18M: ₹5.59 | model=historical_median | error band=±55.81%
- 24M: ₹5.77 | model=historical_median | error band=±65.43%
- 36M: ₹4.63 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
