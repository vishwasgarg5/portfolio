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
- Current price: 26.34000015258789
- Current P/L: ₹-5500.00
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
- Current price: 17.420000076293945
- Current P/L: ₹-5547.30
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.38 | model=historical_median | error band=±17.82%
- 6M: ₹17.02 | model=historical_median | error band=±14.98%
- 9M: ₹16.66 | model=historical_median | error band=±23.03%
- 12M: ₹18.13 | model=extra_trees | error band=±21.87%
- 18M: ₹13.35 | model=historical_median | error band=±22.00%
- 24M: ₹16.24 | model=extra_trees | error band=±13.23%
- 36M: ₹9.19 | model=hist | error band=±16.15%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1339.699951171875
- Current P/L: ₹172.64
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1356.65 | model=historical_median | error band=±14.10%
- 6M: ₹1387.38 | model=historical_median | error band=±21.97%
- 9M: ₹1330.34 | model=extra_trees | error band=±25.66%
- 12M: ₹1463.32 | model=hist | error band=±26.03%
- 18M: ₹1451.67 | model=hist | error band=±33.73%
- 24M: ₹1565.47 | model=extra_trees | error band=±37.59%
- 36M: ₹2406.95 | model=historical_median | error band=±43.19%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 319.1000061035156
- Current P/L: ₹-1250.08
- First forecast horizon at/above purchase price: 18M

- 3M: ₹328.97 | model=historical_median | error band=±15.08%
- 6M: ₹344.92 | model=historical_median | error band=±23.68%
- 9M: ₹351.13 | model=historical_median | error band=±18.92%
- 12M: ₹364.79 | model=historical_median | error band=±19.05%
- 18M: ₹421.77 | model=historical_median | error band=±28.07%
- 24M: ₹425.92 | model=historical_median | error band=±47.96%
- 36M: ₹490.69 | model=historical_median | error band=±65.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 118.3000030517578
- Current P/L: ₹-2170.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹99.12 | model=extra_trees | error band=±5.99%
- 6M: ₹96.14 | model=hist | error band=±9.04%
- 9M: ₹86.16 | model=extra_trees | error band=±2.22%
- 12M: ₹87.22 | model=historical_median | error band=±2.65%
- 18M: ₹67.09 | model=hist | error band=±3.88%
- 24M: ₹64.28 | model=extra_trees | error band=±6.77%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 83.30000305175781
- Current P/L: ₹-1482.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹66.49 | model=hist | error band=±12.89%
- 6M: ₹70.13 | model=hist | error band=±30.77%
- 9M: ₹57.89 | model=hist | error band=±59.58%
- 12M: ₹62.72 | model=hist | error band=±74.04%
- 18M: ₹160.31 | model=historical_median | error band=±205.32%
- 24M: ₹117.87 | model=hist | error band=±56.90%
- 36M: ₹667.74 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 348.0
- Current P/L: ₹-6282.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹353.65 | model=historical_median | error band=±12.16%
- 6M: ₹356.75 | model=historical_median | error band=±17.04%
- 9M: ₹356.51 | model=historical_median | error band=±14.33%
- 12M: ₹354.54 | model=historical_median | error band=±17.45%
- 18M: ₹466.88 | model=historical_median | error band=±43.39%
- 24M: ₹570.87 | model=historical_median | error band=±79.04%
- 36M: ₹629.96 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 194.6000061035156
- Current P/L: ₹-7939.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹187.89 | model=extra_trees | error band=±9.56%
- 6M: ₹181.38 | model=extra_trees | error band=±21.50%
- 9M: ₹178.12 | model=extra_trees | error band=±27.74%
- 12M: ₹183.81 | model=extra_trees | error band=±24.50%
- 18M: ₹185.00 | model=hist | error band=±29.78%
- 24M: ₹253.45 | model=historical_median | error band=±45.45%
- 36M: ₹271.91 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.0
- Current P/L: ₹-11025.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹79.95 | model=historical_median | error band=±18.12%
- 6M: ₹82.52 | model=extra_trees | error band=±16.41%
- 9M: ₹75.46 | model=extra_trees | error band=±26.21%
- 12M: ₹77.15 | model=extra_trees | error band=±40.49%
- 18M: ₹108.65 | model=hist | error band=±38.65%
- 24M: ₹125.26 | model=hist | error band=±66.34%
- 36M: ₹160.70 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 34.650001525878906
- Current P/L: ₹-45557.26
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.92 | model=historical_median | error band=±12.25%
- 6M: ₹25.69 | model=extra_trees | error band=±15.49%
- 9M: ₹24.90 | model=hist | error band=±9.69%
- 12M: ₹23.92 | model=historical_median | error band=±4.67%
- 18M: ₹17.56 | model=hist | error band=±4.47%
- 24M: N/A — Insufficient history for target_24M: 1 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 176.05999755859375
- Current P/L: ₹-8130.44
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.62 | model=historical_median | error band=±20.68%
- 6M: ₹164.93 | model=extra_trees | error band=±16.30%
- 9M: ₹179.71 | model=historical_median | error band=±22.69%
- 12M: ₹179.66 | model=historical_median | error band=±24.44%
- 18M: ₹192.82 | model=historical_median | error band=±26.43%
- 24M: ₹296.80 | model=extra_trees | error band=±31.73%
- 36M: ₹245.04 | model=historical_median | error band=±38.57%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 57.40999984741211
- Current P/L: ₹-3599.63
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹54.09 | model=extra_trees | error band=±17.98%
- 6M: ₹55.60 | model=historical_median | error band=±29.42%
- 9M: ₹56.24 | model=historical_median | error band=±34.89%
- 12M: ₹57.64 | model=historical_median | error band=±42.65%
- 18M: ₹64.90 | model=historical_median | error band=±60.32%
- 24M: ₹73.29 | model=historical_median | error band=±86.22%
- 36M: ₹101.52 | model=historical_median | error band=±95.01%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.549999237060547
- Current P/L: ₹-48285.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.58 | model=historical_median | error band=±31.94%
- 6M: ₹17.97 | model=historical_median | error band=±27.33%
- 9M: ₹17.27 | model=historical_median | error band=±45.34%
- 12M: ₹18.62 | model=historical_median | error band=±61.50%
- 18M: ₹21.57 | model=historical_median | error band=±129.56%
- 24M: ₹25.97 | model=hist | error band=±99.85%
- 36M: ₹43.79 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 457.7000122070313
- Current P/L: ₹-27809.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹451.46 | model=extra_trees | error band=±14.96%
- 6M: ₹444.58 | model=historical_median | error band=±21.31%
- 9M: ₹445.96 | model=historical_median | error band=±32.40%
- 12M: ₹509.83 | model=historical_median | error band=±48.64%
- 18M: ₹582.63 | model=historical_median | error band=±68.18%
- 24M: ₹554.85 | model=historical_median | error band=±65.73%
- 36M: ₹558.95 | model=hist | error band=±114.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.989999771118164
- Current P/L: ₹-6941.11
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.74 | model=historical_median | error band=±15.24%
- 6M: ₹4.87 | model=historical_median | error band=±21.60%
- 9M: ₹2.93 | model=hist | error band=±54.31%
- 12M: ₹3.15 | model=hist | error band=±49.47%
- 18M: ₹5.49 | model=historical_median | error band=±55.81%
- 24M: ₹5.68 | model=historical_median | error band=±65.43%
- 36M: ₹4.56 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
