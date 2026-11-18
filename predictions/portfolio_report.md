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
- 6M: ₹17.33 | model=historical_median | error band=±14.98%
- 9M: ₹16.91 | model=historical_median | error band=±23.03%
- 12M: ₹18.52 | model=extra_trees | error band=±21.75%
- 18M: ₹13.62 | model=historical_median | error band=±22.05%
- 24M: ₹17.39 | model=extra_trees | error band=±13.28%
- 36M: ₹22.42 | model=hist | error band=±16.32%

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
- 9M: ₹1356.86 | model=hist | error band=±19.02%
- 12M: ₹1472.95 | model=hist | error band=±26.03%
- 18M: ₹1493.40 | model=hist | error band=±33.73%
- 24M: ₹1519.74 | model=extra_trees | error band=±37.59%
- 36M: ₹2445.27 | model=historical_median | error band=±43.31%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 320.3999938964844
- Current P/L: ₹-1216.28
- First forecast horizon at/above purchase price: 12M

- 3M: ₹330.30 | model=historical_median | error band=±15.08%
- 6M: ₹345.68 | model=historical_median | error band=±23.64%
- 9M: ₹351.23 | model=historical_median | error band=±19.87%
- 12M: ₹371.55 | model=historical_median | error band=±19.07%
- 18M: ₹425.89 | model=historical_median | error band=±22.98%
- 24M: ₹428.43 | model=historical_median | error band=±47.31%
- 36M: ₹492.95 | model=historical_median | error band=±52.67%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 117.4000015258789
- Current P/L: ₹-2485.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹98.74 | model=extra_trees | error band=±5.99%
- 6M: ₹93.28 | model=hist | error band=±9.06%
- 9M: ₹84.04 | model=hist | error band=±2.25%
- 12M: ₹86.71 | model=historical_median | error band=±2.65%
- 18M: ₹65.67 | model=hist | error band=±3.88%
- 24M: ₹65.22 | model=extra_trees | error band=±6.23%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 82.6500015258789
- Current P/L: ₹-1612.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹66.64 | model=hist | error band=±12.89%
- 6M: ₹71.06 | model=hist | error band=±30.77%
- 9M: ₹58.91 | model=hist | error band=±59.58%
- 12M: ₹61.19 | model=hist | error band=±74.04%
- 18M: ₹155.57 | model=historical_median | error band=±205.32%
- 24M: ₹200.72 | model=hist | error band=±56.32%
- 36M: ₹621.82 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 344.5
- Current P/L: ₹-6527.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹350.09 | model=historical_median | error band=±12.16%
- 6M: ₹353.06 | model=historical_median | error band=±17.04%
- 9M: ₹352.65 | model=historical_median | error band=±14.33%
- 12M: ₹350.67 | model=historical_median | error band=±17.45%
- 18M: ₹461.32 | model=historical_median | error band=±43.39%
- 24M: ₹565.19 | model=historical_median | error band=±79.04%
- 36M: ₹585.78 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 189.88999938964844
- Current P/L: ₹-9399.20
- First forecast horizon at/above purchase price: 24M

- 3M: ₹185.38 | model=extra_trees | error band=±9.56%
- 6M: ₹174.99 | model=extra_trees | error band=±21.50%
- 9M: ₹167.78 | model=extra_trees | error band=±27.79%
- 12M: ₹164.46 | model=extra_trees | error band=±24.47%
- 18M: ₹181.87 | model=hist | error band=±29.78%
- 24M: ₹247.22 | model=historical_median | error band=±45.45%
- 36M: ₹264.84 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.0
- Current P/L: ₹-11025.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹79.95 | model=historical_median | error band=±18.12%
- 6M: ₹86.15 | model=extra_trees | error band=±16.41%
- 9M: ₹76.96 | model=extra_trees | error band=±26.21%
- 12M: ₹81.61 | model=extra_trees | error band=±40.49%
- 18M: ₹135.53 | model=hist | error band=±38.65%
- 24M: ₹131.36 | model=hist | error band=±66.34%
- 36M: ₹160.60 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 33.2400016784668
- Current P/L: ₹-49564.48
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹27.80 | model=historical_median | error band=±12.25%
- 6M: ₹25.31 | model=extra_trees | error band=±15.54%
- 9M: ₹22.60 | model=hist | error band=±9.69%
- 12M: ₹22.78 | model=historical_median | error band=±4.70%
- 18M: ₹16.93 | model=hist | error band=±4.31%
- 24M: N/A — Insufficient history for target_24M: 3 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 173.44000244140625
- Current P/L: ₹-8355.76
- First forecast horizon at/above purchase price: 24M

- 3M: ₹172.63 | model=historical_median | error band=±20.60%
- 6M: ₹169.44 | model=extra_trees | error band=±16.09%
- 9M: ₹178.60 | model=historical_median | error band=±24.31%
- 12M: ₹176.53 | model=historical_median | error band=±26.86%
- 18M: ₹186.96 | model=historical_median | error band=±23.39%
- 24M: ₹279.47 | model=extra_trees | error band=±36.34%
- 36M: ₹236.85 | model=historical_median | error band=±36.17%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 55.880001068115234
- Current P/L: ₹-3711.32
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹54.32 | model=extra_trees | error band=±17.98%
- 6M: ₹54.10 | model=historical_median | error band=±29.42%
- 9M: ₹54.70 | model=historical_median | error band=±34.89%
- 12M: ₹56.10 | model=historical_median | error band=±42.65%
- 18M: ₹63.19 | model=historical_median | error band=±60.32%
- 24M: ₹72.61 | model=historical_median | error band=±86.22%
- 36M: ₹98.83 | model=historical_median | error band=±95.15%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.940000534057617
- Current P/L: ₹-49657.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.00 | model=historical_median | error band=±31.94%
- 6M: ₹17.36 | model=historical_median | error band=±27.38%
- 9M: ₹16.72 | model=historical_median | error band=±45.34%
- 12M: ₹18.00 | model=historical_median | error band=±61.50%
- 18M: ₹20.93 | model=historical_median | error band=±129.75%
- 24M: ₹29.88 | model=hist | error band=±99.85%
- 36M: ₹42.41 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 449.3500061035156
- Current P/L: ₹-28319.25
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹430.75 | model=extra_trees | error band=±14.96%
- 6M: ₹436.35 | model=historical_median | error band=±21.31%
- 9M: ₹436.84 | model=historical_median | error band=±32.40%
- 12M: ₹500.34 | model=historical_median | error band=±48.64%
- 18M: ₹571.48 | model=historical_median | error band=±68.18%
- 24M: ₹543.24 | model=historical_median | error band=±65.73%
- 36M: ₹836.85 | model=extra_trees | error band=±114.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.900000095367432
- Current P/L: ₹-7029.22
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.73 | model=historical_median | error band=±15.24%
- 6M: ₹4.77 | model=historical_median | error band=±21.60%
- 9M: ₹2.80 | model=hist | error band=±54.31%
- 12M: ₹3.15 | model=hist | error band=±49.47%
- 18M: ₹5.38 | model=historical_median | error band=±55.81%
- 24M: ₹5.62 | model=historical_median | error band=±65.43%
- 36M: ₹4.52 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
