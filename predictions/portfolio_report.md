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
- Current price: 32.310001373291016
- Current P/L: ₹470.00
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
- Current price: 22.440000534057617
- Current P/L: ₹-1019.26
- First forecast horizon at/above purchase price: 12M

- 3M: ₹22.44 | model=historical_median | error band=±17.82%
- 6M: ₹22.03 | model=historical_median | error band=±14.97%
- 9M: ₹21.66 | model=historical_median | error band=±23.03%
- 12M: ₹26.12 | model=extra_trees | error band=±21.33%
- 18M: ₹16.85 | model=historical_median | error band=±21.44%
- 24M: ₹28.91 | model=hist | error band=±13.27%
- 36M: ₹17.83 | model=hist | error band=±16.73%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1219.699951171875
- Current P/L: ₹-1387.36
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1237.36 | model=historical_median | error band=±14.10%
- 6M: ₹1268.37 | model=historical_median | error band=±21.97%
- 9M: ₹1419.68 | model=hist | error band=±25.66%
- 12M: ₹1477.51 | model=hist | error band=±26.03%
- 18M: ₹1212.36 | model=hist | error band=±33.73%
- 24M: ₹1385.55 | model=extra_trees | error band=±33.83%
- 36M: ₹1501.68 | model=extra_trees | error band=±43.27%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 325.6000061035156
- Current P/L: ₹-1081.08
- First forecast horizon at/above purchase price: 12M

- 3M: ₹336.71 | model=historical_median | error band=±15.08%
- 6M: ₹358.31 | model=historical_median | error band=±17.62%
- 9M: ₹360.08 | model=historical_median | error band=±18.85%
- 12M: ₹383.11 | model=historical_median | error band=±19.03%
- 18M: ₹422.24 | model=historical_median | error band=±22.74%
- 24M: ₹429.84 | model=historical_median | error band=±39.81%
- 36M: ₹495.82 | model=historical_median | error band=±51.53%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 114.4800033569336
- Current P/L: ₹-3507.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹105.43 | model=historical_median | error band=±6.87%
- 6M: ₹100.47 | model=hist | error band=±5.18%
- 9M: ₹91.85 | model=extra_trees | error band=±2.20%
- 12M: ₹83.74 | model=historical_median | error band=±2.73%
- 18M: ₹66.83 | model=hist | error band=±3.88%
- 24M: ₹76.02 | model=hist | error band=±5.92%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 79.88999938964844
- Current P/L: ₹-2164.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹70.31 | model=hist | error band=±17.38%
- 6M: ₹68.86 | model=hist | error band=±27.15%
- 9M: ₹51.76 | model=hist | error band=±60.10%
- 12M: ₹87.43 | model=hist | error band=±77.06%
- 18M: ₹170.87 | model=historical_median | error band=±202.30%
- 24M: ₹605.51 | model=hist | error band=±41.34%
- 36M: ₹555.95 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 366.6499938964844
- Current P/L: ₹-4977.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹373.14 | model=historical_median | error band=±12.16%
- 6M: ₹379.77 | model=historical_median | error band=±10.78%
- 9M: ₹376.42 | model=historical_median | error band=±14.33%
- 12M: ₹382.36 | model=historical_median | error band=±18.83%
- 18M: ₹486.65 | model=historical_median | error band=±44.88%
- 24M: ₹623.84 | model=historical_median | error band=±76.59%
- 36M: ₹498.36 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 164.25999450683594
- Current P/L: ₹-17344.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹172.63 | model=extra_trees | error band=±9.56%
- 6M: ₹161.11 | model=extra_trees | error band=±21.50%
- 9M: ₹146.31 | model=extra_trees | error band=±27.76%
- 12M: ₹161.88 | model=extra_trees | error band=±21.79%
- 18M: ₹175.90 | model=hist | error band=±29.78%
- 24M: ₹215.61 | model=historical_median | error band=±41.29%
- 36M: ₹234.49 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 84.5999984741211
- Current P/L: ₹-9645.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹85.46 | model=historical_median | error band=±18.12%
- 6M: ₹70.86 | model=extra_trees | error band=±16.72%
- 9M: ₹62.10 | model=extra_trees | error band=±26.21%
- 12M: ₹58.62 | model=extra_trees | error band=±40.49%
- 18M: ₹68.80 | model=hist | error band=±38.65%
- 24M: ₹113.41 | model=historical_median | error band=±61.31%
- 36M: ₹171.67 | model=historical_median | error band=±88.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 39.02999877929688
- Current P/L: ₹-33109.30
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹40.45 | model=extra_trees | error band=±12.42%
- 6M: ₹27.77 | model=hist | error band=±16.51%
- 9M: ₹34.19 | model=hist | error band=±10.35%
- 12M: ₹28.22 | model=extra_trees | error band=±10.96%
- 18M: ₹20.15 | model=hist | error band=±5.20%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 186.2899932861328
- Current P/L: ₹-7250.66
- First forecast horizon at/above purchase price: 24M

- 3M: ₹187.87 | model=historical_median | error band=±20.10%
- 6M: ₹169.84 | model=extra_trees | error band=±20.87%
- 9M: ₹195.09 | model=historical_median | error band=±20.33%
- 12M: ₹193.17 | model=historical_median | error band=±16.81%
- 18M: ₹211.19 | model=historical_median | error band=±29.46%
- 24M: ₹335.72 | model=extra_trees | error band=±28.44%
- 36M: ₹253.33 | model=historical_median | error band=±26.25%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 61.58000183105469
- Current P/L: ₹-3295.22
- First forecast horizon at/above purchase price: 36M

- 3M: ₹59.69 | model=historical_median | error band=±17.98%
- 6M: ₹60.78 | model=historical_median | error band=±25.49%
- 9M: ₹60.52 | model=historical_median | error band=±34.89%
- 12M: ₹62.21 | model=historical_median | error band=±38.32%
- 18M: ₹69.23 | model=historical_median | error band=±69.37%
- 24M: ₹79.64 | model=historical_median | error band=±86.61%
- 36M: ₹108.12 | model=historical_median | error band=±117.64%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 20.43000030517578
- Current P/L: ₹-44055.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹19.86 | model=historical_median | error band=±32.27%
- 6M: ₹23.04 | model=extra_trees | error band=±25.39%
- 9M: ₹21.56 | model=extra_trees | error band=±47.43%
- 12M: ₹20.85 | model=historical_median | error band=±59.34%
- 18M: ₹19.79 | model=extra_trees | error band=±97.85%
- 24M: ₹12.56 | model=hist | error band=±104.21%
- 36M: ₹46.35 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 459.0
- Current P/L: ₹-27730.60
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹422.12 | model=hist | error band=±15.04%
- 6M: ₹445.47 | model=historical_median | error band=±21.55%
- 9M: ₹452.20 | model=historical_median | error band=±32.44%
- 12M: ₹523.80 | model=historical_median | error band=±48.52%
- 18M: ₹589.08 | model=historical_median | error band=±68.41%
- 24M: ₹565.18 | model=historical_median | error band=±46.47%
- 36M: ₹357.93 | model=extra_trees | error band=±114.91%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.130000114440918
- Current P/L: ₹-6804.05
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.88 | model=historical_median | error band=±20.52%
- 6M: ₹5.16 | model=historical_median | error band=±22.10%
- 9M: ₹2.05 | model=hist | error band=±48.03%
- 12M: ₹2.15 | model=extra_trees | error band=±53.68%
- 18M: ₹5.70 | model=historical_median | error band=±51.51%
- 24M: ₹6.04 | model=historical_median | error band=±60.82%
- 36M: ₹4.58 | model=historical_median | error band=±88.91%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
