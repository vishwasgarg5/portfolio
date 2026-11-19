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
- Current price: 24.170000076293945
- Current P/L: ₹-7670.00
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
- Current price: 17.68000030517578
- Current P/L: ₹-5312.78
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.63 | model=historical_median | error band=±17.82%
- 6M: ₹17.27 | model=historical_median | error band=±15.03%
- 9M: ₹16.91 | model=historical_median | error band=±23.03%
- 12M: ₹18.49 | model=extra_trees | error band=±21.35%
- 18M: ₹13.61 | model=historical_median | error band=±22.00%
- 24M: ₹17.25 | model=extra_trees | error band=±13.30%
- 36M: ₹22.33 | model=hist | error band=±16.32%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1363.0
- Current P/L: ₹475.54
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1379.84 | model=historical_median | error band=±14.10%
- 6M: ₹1411.33 | model=historical_median | error band=±21.97%
- 9M: ₹1368.24 | model=hist | error band=±19.02%
- 12M: ₹1472.95 | model=hist | error band=±26.03%
- 18M: ₹1493.40 | model=hist | error band=±33.73%
- 24M: ₹1526.89 | model=extra_trees | error band=±37.59%
- 36M: ₹2445.32 | model=historical_median | error band=±43.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 320.3999938964844
- Current P/L: ₹-1216.28
- First forecast horizon at/above purchase price: 12M

- 3M: ₹329.93 | model=historical_median | error band=±15.08%
- 6M: ₹346.25 | model=historical_median | error band=±23.64%
- 9M: ₹351.23 | model=historical_median | error band=±19.87%
- 12M: ₹371.83 | model=historical_median | error band=±19.03%
- 18M: ₹426.44 | model=historical_median | error band=±22.98%
- 24M: ₹429.44 | model=historical_median | error band=±47.91%
- 36M: ₹490.09 | model=historical_median | error band=±52.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 119.8000030517578
- Current P/L: ₹-1645.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹99.25 | model=extra_trees | error band=±5.99%
- 6M: ₹92.82 | model=hist | error band=±9.04%
- 9M: ₹86.14 | model=hist | error band=±2.27%
- 12M: ₹88.48 | model=historical_median | error band=±2.65%
- 18M: ₹67.68 | model=hist | error band=±3.88%
- 24M: ₹67.27 | model=extra_trees | error band=±6.23%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 81.0999984741211
- Current P/L: ₹-1922.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹67.88 | model=hist | error band=±12.89%
- 6M: ₹67.71 | model=hist | error band=±30.77%
- 9M: ₹58.35 | model=hist | error band=±59.58%
- 12M: ₹61.97 | model=hist | error band=±74.04%
- 18M: ₹149.33 | model=historical_median | error band=±205.32%
- 24M: ₹203.83 | model=hist | error band=±56.46%
- 36M: ₹613.02 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 338.0
- Current P/L: ₹-6982.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹343.47 | model=historical_median | error band=±12.16%
- 6M: ₹346.37 | model=historical_median | error band=±17.04%
- 9M: ₹340.89 | model=historical_median | error band=±14.33%
- 12M: ₹344.04 | model=historical_median | error band=±17.45%
- 18M: ₹452.46 | model=historical_median | error band=±43.39%
- 24M: ₹554.81 | model=historical_median | error band=±79.04%
- 36M: ₹617.96 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 185.13999938964844
- Current P/L: ₹-10871.70
- First forecast horizon at/above purchase price: 24M

- 3M: ₹178.48 | model=extra_trees | error band=±9.56%
- 6M: ₹168.84 | model=extra_trees | error band=±21.50%
- 9M: ₹161.98 | model=extra_trees | error band=±27.68%
- 12M: ₹157.44 | model=extra_trees | error band=±24.65%
- 18M: ₹177.20 | model=hist | error band=±29.78%
- 24M: ₹240.85 | model=historical_median | error band=±45.45%
- 36M: ₹258.21 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 78.4000015258789
- Current P/L: ₹-11505.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹78.34 | model=historical_median | error band=±18.12%
- 6M: ₹81.93 | model=extra_trees | error band=±16.41%
- 9M: ₹73.14 | model=extra_trees | error band=±26.21%
- 12M: ₹70.35 | model=extra_trees | error band=±40.49%
- 18M: ₹87.52 | model=hist | error band=±38.65%
- 24M: ₹119.81 | model=hist | error band=±66.34%
- 36M: ₹157.37 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 32.58000183105469
- Current P/L: ₹-51440.19
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹27.24 | model=historical_median | error band=±12.25%
- 6M: ₹24.82 | model=extra_trees | error band=±15.52%
- 9M: ₹23.89 | model=hist | error band=±9.69%
- 12M: ₹24.21 | model=extra_trees | error band=±4.67%
- 18M: ₹16.64 | model=hist | error band=±4.29%
- 24M: N/A — Insufficient history for target_24M: 4 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 175.19000244140625
- Current P/L: ₹-8205.26
- First forecast horizon at/above purchase price: 24M

- 3M: ₹174.38 | model=historical_median | error band=±20.74%
- 6M: ₹168.32 | model=extra_trees | error band=±16.01%
- 9M: ₹179.27 | model=historical_median | error band=±23.94%
- 12M: ₹179.11 | model=historical_median | error band=±26.38%
- 18M: ₹192.44 | model=historical_median | error band=±23.72%
- 24M: ₹319.10 | model=extra_trees | error band=±33.77%
- 36M: ₹239.37 | model=historical_median | error band=±40.29%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 54.63999938964844
- Current P/L: ₹-3801.84
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹53.34 | model=extra_trees | error band=±17.98%
- 6M: ₹52.90 | model=historical_median | error band=±29.42%
- 9M: ₹53.03 | model=historical_median | error band=±35.31%
- 12M: ₹54.85 | model=historical_median | error band=±42.65%
- 18M: ₹61.79 | model=historical_median | error band=±66.42%
- 24M: ₹69.72 | model=historical_median | error band=±86.22%
- 36M: ₹96.64 | model=historical_median | error band=±95.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.760000228881836
- Current P/L: ₹-50062.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹16.83 | model=historical_median | error band=±31.94%
- 6M: ₹17.19 | model=historical_median | error band=±27.30%
- 9M: ₹15.57 | model=historical_median | error band=±42.49%
- 12M: ₹17.88 | model=historical_median | error band=±61.50%
- 18M: ₹20.47 | model=historical_median | error band=±129.61%
- 24M: ₹33.91 | model=hist | error band=±99.85%
- 36M: ₹41.93 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 444.3500061035156
- Current P/L: ₹-28624.25
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹423.77 | model=extra_trees | error band=±14.96%
- 6M: ₹431.39 | model=historical_median | error band=±21.31%
- 9M: ₹431.01 | model=historical_median | error band=±32.40%
- 12M: ₹494.77 | model=historical_median | error band=±48.64%
- 18M: ₹564.82 | model=historical_median | error band=±68.18%
- 24M: ₹536.41 | model=historical_median | error band=±65.73%
- 36M: ₹777.73 | model=extra_trees | error band=±114.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.860000133514404
- Current P/L: ₹-7068.38
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.67 | model=historical_median | error band=±15.24%
- 6M: ₹4.74 | model=historical_median | error band=±21.60%
- 9M: ₹3.27 | model=extra_trees | error band=±54.31%
- 12M: ₹3.11 | model=hist | error band=±49.47%
- 18M: ₹5.34 | model=historical_median | error band=±55.81%
- 24M: ₹5.57 | model=historical_median | error band=±65.43%
- 36M: ₹4.51 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
