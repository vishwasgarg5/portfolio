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
- Current price: 23.809999465942383
- Current P/L: ₹-8030.00
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
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.62 | model=historical_median | error band=±20.21%
- 6M: ₹17.27 | model=historical_median | error band=±14.97%
- 9M: ₹16.88 | model=historical_median | error band=±23.03%
- 12M: ₹18.56 | model=extra_trees | error band=±21.40%
- 18M: ₹13.67 | model=historical_median | error band=±21.80%
- 24M: ₹20.46 | model=extra_trees | error band=±13.25%
- 36M: ₹32.86 | model=hist | error band=±16.06%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1396.199951171875
- Current P/L: ₹907.14
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1419.36 | model=historical_median | error band=±13.20%
- 6M: ₹1445.58 | model=historical_median | error band=±21.97%
- 9M: ₹1455.99 | model=hist | error band=±19.02%
- 12M: ₹1432.59 | model=hist | error band=±26.03%
- 18M: ₹1513.55 | model=hist | error band=±33.73%
- 24M: ₹1533.99 | model=extra_trees | error band=±37.52%
- 36M: ₹2501.33 | model=historical_median | error band=±43.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 320.25
- Current P/L: ₹-1220.18
- First forecast horizon at/above purchase price: 12M

- 3M: ₹292.93 | model=hist | error band=±15.08%
- 6M: ₹345.27 | model=historical_median | error band=±23.64%
- 9M: ₹350.90 | model=historical_median | error band=±19.87%
- 12M: ₹368.56 | model=historical_median | error band=±19.03%
- 18M: ₹422.98 | model=historical_median | error band=±28.07%
- 24M: ₹421.84 | model=historical_median | error band=±49.52%
- 36M: ₹494.75 | model=historical_median | error band=±56.98%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 127.0
- Current P/L: ₹875.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹106.31 | model=extra_trees | error band=±5.99%
- 6M: ₹109.46 | model=hist | error band=±9.03%
- 9M: ₹87.71 | model=hist | error band=±2.26%
- 12M: ₹94.19 | model=historical_median | error band=±2.65%
- 18M: ₹71.14 | model=hist | error band=±3.88%
- 24M: ₹72.27 | model=extra_trees | error band=±6.91%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 82.30000305175781
- Current P/L: ₹-1682.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹68.48 | model=hist | error band=±12.89%
- 6M: ₹64.36 | model=hist | error band=±30.77%
- 9M: ₹52.00 | model=hist | error band=±59.58%
- 12M: ₹65.61 | model=hist | error band=±74.04%
- 18M: ₹149.37 | model=historical_median | error band=±205.32%
- 24M: ₹137.82 | model=hist | error band=±56.37%
- 36M: ₹645.68 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 323.5
- Current P/L: ₹-7997.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹323.42 | model=historical_median | error band=±13.46%
- 6M: ₹331.29 | model=historical_median | error band=±17.04%
- 9M: ₹326.04 | model=historical_median | error band=±14.33%
- 12M: ₹328.28 | model=historical_median | error band=±17.45%
- 18M: ₹433.98 | model=historical_median | error band=±43.39%
- 24M: ₹531.56 | model=historical_median | error band=±79.04%
- 36M: ₹671.37 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 196.5399932861328
- Current P/L: ₹-7337.70
- First forecast horizon at/above purchase price: 24M

- 3M: ₹200.35 | model=extra_trees | error band=±8.94%
- 6M: ₹198.21 | model=extra_trees | error band=±21.50%
- 9M: ₹183.83 | model=extra_trees | error band=±27.77%
- 12M: ₹185.53 | model=extra_trees | error band=±24.84%
- 18M: ₹211.64 | model=hist | error band=±29.78%
- 24M: ₹255.35 | model=historical_median | error band=±45.45%
- 36M: ₹273.41 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 78.79000091552734
- Current P/L: ₹-11388.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹78.72 | model=historical_median | error band=±18.12%
- 6M: ₹84.84 | model=extra_trees | error band=±16.41%
- 9M: ₹76.67 | model=extra_trees | error band=±26.21%
- 12M: ₹78.99 | model=extra_trees | error band=±40.49%
- 18M: ₹66.74 | model=hist | error band=±38.65%
- 24M: ₹106.00 | model=hist | error band=±66.34%
- 36M: ₹157.77 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 31.86000061035156
- Current P/L: ₹-53486.44
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹26.73 | model=historical_median | error band=±12.32%
- 6M: ₹25.20 | model=extra_trees | error band=±15.58%
- 9M: ₹18.03 | model=hist | error band=±9.69%
- 12M: ₹23.99 | model=extra_trees | error band=±4.70%
- 18M: ₹16.61 | model=hist | error band=±3.86%
- 24M: N/A — Insufficient history for target_24M: 9 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 171.25999450683594
- Current P/L: ₹-8543.24
- First forecast horizon at/above purchase price: 24M

- 3M: ₹170.55 | model=historical_median | error band=±20.75%
- 6M: ₹166.30 | model=extra_trees | error band=±16.02%
- 9M: ₹175.31 | model=historical_median | error band=±23.03%
- 12M: ₹174.42 | model=historical_median | error band=±22.99%
- 18M: ₹188.26 | model=historical_median | error band=±26.32%
- 24M: ₹329.48 | model=extra_trees | error band=±38.24%
- 36M: ₹241.81 | model=historical_median | error band=±41.54%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 55.040000915527344
- Current P/L: ₹-3772.64
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹53.92 | model=extra_trees | error band=±17.32%
- 6M: ₹53.27 | model=historical_median | error band=±29.42%
- 9M: ₹53.41 | model=historical_median | error band=±35.31%
- 12M: ₹55.22 | model=historical_median | error band=±42.65%
- 18M: ₹62.25 | model=historical_median | error band=±66.42%
- 24M: ₹71.49 | model=historical_median | error band=±86.22%
- 36M: ₹97.39 | model=historical_median | error band=±97.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.1200008392334
- Current P/L: ₹-51502.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹15.80 | model=historical_median | error band=±26.45%
- 6M: ₹16.62 | model=historical_median | error band=±27.32%
- 9M: ₹15.03 | model=historical_median | error band=±42.49%
- 12M: ₹27.12 | model=extra_trees | error band=±61.50%
- 18M: ₹19.96 | model=historical_median | error band=±129.57%
- 24M: ₹28.89 | model=hist | error band=±99.85%
- 36M: ₹40.62 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 454.2000122070313
- Current P/L: ₹-28023.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹444.18 | model=extra_trees | error band=±10.52%
- 6M: ₹440.32 | model=historical_median | error band=±21.31%
- 9M: ₹439.50 | model=historical_median | error band=±32.40%
- 12M: ₹505.37 | model=historical_median | error band=±48.64%
- 18M: ₹576.41 | model=historical_median | error band=±68.18%
- 24M: ₹547.16 | model=historical_median | error band=±65.73%
- 36M: ₹685.03 | model=hist | error band=±114.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.75
- Current P/L: ₹-7176.07
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.51 | model=historical_median | error band=±15.24%
- 6M: ₹4.63 | model=historical_median | error band=±21.60%
- 9M: ₹3.38 | model=extra_trees | error band=±54.31%
- 12M: ₹2.98 | model=hist | error band=±49.47%
- 18M: ₹5.18 | model=historical_median | error band=±55.81%
- 24M: ₹5.52 | model=historical_median | error band=±65.43%
- 36M: ₹4.44 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
