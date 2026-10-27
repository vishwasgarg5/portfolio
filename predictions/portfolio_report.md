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
- Current price: 27.950000762939453
- Current P/L: ₹-3890.00
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
- Current price: 15.899999618530272
- Current P/L: ₹-6918.34
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.87 | model=historical_median | error band=±17.82%
- 6M: ₹15.58 | model=historical_median | error band=±14.98%
- 9M: ₹15.27 | model=historical_median | error band=±23.03%
- 12M: ₹17.07 | model=extra_trees | error band=±21.58%
- 18M: ₹12.12 | model=historical_median | error band=±21.94%
- 24M: ₹13.84 | model=extra_trees | error band=±13.01%
- 36M: ₹4.01 | model=hist | error band=±16.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1196.199951171875
- Current P/L: ₹-1692.86
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1211.64 | model=historical_median | error band=±14.10%
- 6M: ₹1239.53 | model=historical_median | error band=±21.97%
- 9M: ₹1367.74 | model=hist | error band=±25.66%
- 12M: ₹1347.23 | model=hist | error band=±26.03%
- 18M: ₹1446.48 | model=historical_median | error band=±33.73%
- 24M: ₹1370.16 | model=extra_trees | error band=±37.59%
- 36M: ₹2159.01 | model=historical_median | error band=±43.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 301.79998779296875
- Current P/L: ₹-1699.88
- First forecast horizon at/above purchase price: 18M

- 3M: ₹311.57 | model=historical_median | error band=±15.08%
- 6M: ₹326.36 | model=historical_median | error band=±23.64%
- 9M: ₹332.89 | model=historical_median | error band=±18.85%
- 12M: ₹350.68 | model=historical_median | error band=±19.03%
- 18M: ₹396.98 | model=historical_median | error band=±22.96%
- 24M: ₹400.24 | model=historical_median | error band=±48.50%
- 36M: ₹464.22 | model=historical_median | error band=±54.69%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 99.6999969482422
- Current P/L: ₹-8680.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹102.90 | model=extra_trees | error band=±5.97%
- 6M: ₹95.75 | model=hist | error band=±5.31%
- 9M: ₹80.97 | model=extra_trees | error band=±2.26%
- 12M: ₹73.46 | model=historical_median | error band=±2.73%
- 18M: ₹64.33 | model=hist | error band=±3.82%
- 24M: ₹50.97 | model=extra_trees | error band=±8.77%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 74.55999755859375
- Current P/L: ₹-3230.00
- First forecast horizon at/above purchase price: 9M

- 3M: ₹65.61 | model=hist | error band=±14.14%
- 6M: ₹70.45 | model=historical_median | error band=±30.97%
- 9M: ₹91.19 | model=hist | error band=±59.47%
- 12M: ₹92.90 | model=hist | error band=±74.34%
- 18M: ₹152.29 | model=historical_median | error band=±208.39%
- 24M: ₹362.83 | model=hist | error band=±40.16%
- 36M: ₹539.71 | model=hist | error band=±300.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 339.1000061035156
- Current P/L: ₹-6905.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹344.76 | model=historical_median | error band=±12.16%
- 6M: ₹347.99 | model=historical_median | error band=±17.04%
- 9M: ₹347.75 | model=historical_median | error band=±14.33%
- 12M: ₹346.25 | model=historical_median | error band=±17.45%
- 18M: ₹458.05 | model=historical_median | error band=±43.39%
- 24M: ₹554.89 | model=historical_median | error band=±79.04%
- 36M: ₹610.78 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 187.0
- Current P/L: ₹-10295.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹166.10 | model=extra_trees | error band=±9.56%
- 6M: ₹152.02 | model=extra_trees | error band=±21.50%
- 9M: ₹139.53 | model=extra_trees | error band=±27.74%
- 12M: ₹146.71 | model=extra_trees | error band=±24.73%
- 18M: ₹128.81 | model=hist | error band=±29.78%
- 24M: ₹243.27 | model=historical_median | error band=±45.45%
- 36M: ₹263.57 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 77.6500015258789
- Current P/L: ₹-11730.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹78.30 | model=historical_median | error band=±18.12%
- 6M: ₹70.33 | model=extra_trees | error band=±16.41%
- 9M: ₹60.46 | model=extra_trees | error band=±26.21%
- 12M: ₹57.96 | model=extra_trees | error band=±40.49%
- 18M: ₹55.31 | model=hist | error band=±38.65%
- 24M: ₹103.12 | model=historical_median | error band=±66.34%
- 36M: ₹156.81 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 34.79999923706055
- Current P/L: ₹-45130.96
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.71 | model=historical_median | error band=±12.25%
- 6M: ₹22.20 | model=hist | error band=±16.52%
- 9M: ₹22.15 | model=hist | error band=±9.69%
- 12M: ₹20.77 | model=historical_median | error band=±7.95%
- 18M: ₹17.85 | model=hist | error band=±4.35%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 157.97000122070312
- Current P/L: ₹-9686.18
- First forecast horizon at/above purchase price: 24M

- 3M: ₹157.01 | model=historical_median | error band=±20.77%
- 6M: ₹154.01 | model=extra_trees | error band=±20.87%
- 9M: ₹161.20 | model=historical_median | error band=±23.71%
- 12M: ₹162.50 | model=historical_median | error band=±16.76%
- 18M: ₹179.42 | model=historical_median | error band=±29.46%
- 24M: ₹289.71 | model=extra_trees | error band=±28.68%
- 36M: ₹215.94 | model=historical_median | error band=±26.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 50.75
- Current P/L: ₹-4085.81
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹49.12 | model=historical_median | error band=±17.98%
- 6M: ₹49.20 | model=historical_median | error band=±29.42%
- 9M: ₹49.77 | model=historical_median | error band=±34.89%
- 12M: ₹51.04 | model=historical_median | error band=±42.65%
- 18M: ₹57.27 | model=historical_median | error band=±66.42%
- 24M: ₹65.10 | model=historical_median | error band=±86.22%
- 36M: ₹89.42 | model=historical_median | error band=±96.17%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 16.979999542236328
- Current P/L: ₹-51817.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹16.08 | model=historical_median | error band=±31.94%
- 6M: ₹16.37 | model=historical_median | error band=±27.32%
- 9M: ₹15.75 | model=historical_median | error band=±45.34%
- 12M: ₹16.97 | model=historical_median | error band=±61.50%
- 18M: ₹19.33 | model=historical_median | error band=±129.47%
- 24M: ₹44.33 | model=hist | error band=±99.85%
- 36M: ₹39.82 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 449.2000122070313
- Current P/L: ₹-28328.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹410.27 | model=extra_trees | error band=±14.99%
- 6M: ₹436.64 | model=historical_median | error band=±21.30%
- 9M: ₹439.70 | model=historical_median | error band=±32.47%
- 12M: ₹503.32 | model=historical_median | error band=±48.65%
- 18M: ₹573.06 | model=historical_median | error band=±68.41%
- 24M: ₹548.49 | model=historical_median | error band=±66.06%
- 36M: ₹594.85 | model=extra_trees | error band=±101.24%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.880000114440918
- Current P/L: ₹-7048.80
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.71 | model=historical_median | error band=±15.24%
- 6M: ₹4.73 | model=historical_median | error band=±21.60%
- 9M: ₹2.70 | model=hist | error band=±54.31%
- 12M: ₹2.56 | model=extra_trees | error band=±49.47%
- 18M: ₹5.41 | model=historical_median | error band=±55.81%
- 24M: ₹5.53 | model=historical_median | error band=±65.43%
- 36M: ₹4.42 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
