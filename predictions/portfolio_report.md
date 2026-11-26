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
- Current price: 23.190000534057617
- Current P/L: ₹-8650.00
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
- Current price: 17.709999084472656
- Current P/L: ₹-5285.72
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.65 | model=historical_median | error band=±20.21%
- 6M: ₹17.29 | model=historical_median | error band=±14.96%
- 9M: ₹16.91 | model=historical_median | error band=±23.03%
- 12M: ₹18.59 | model=extra_trees | error band=±21.35%
- 18M: ₹13.68 | model=historical_median | error band=±22.07%
- 24M: ₹20.72 | model=extra_trees | error band=±13.22%
- 36M: ₹32.20 | model=hist | error band=±16.10%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1373.9000244140625
- Current P/L: ₹617.24
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1396.83 | model=historical_median | error band=±13.20%
- 6M: ₹1422.50 | model=historical_median | error band=±21.97%
- 9M: ₹1355.89 | model=hist | error band=±19.06%
- 12M: ₹1390.16 | model=hist | error band=±26.03%
- 18M: ₹1489.86 | model=hist | error band=±33.73%
- 24M: ₹1512.33 | model=extra_trees | error band=±37.51%
- 36M: ₹2461.08 | model=historical_median | error band=±43.22%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 318.0
- Current P/L: ₹-1278.68
- First forecast horizon at/above purchase price: 18M

- 3M: ₹332.11 | model=historical_median | error band=±15.08%
- 6M: ₹348.00 | model=historical_median | error band=±23.41%
- 9M: ₹348.43 | model=historical_median | error band=±19.87%
- 12M: ₹366.04 | model=historical_median | error band=±19.03%
- 18M: ₹419.91 | model=historical_median | error band=±28.07%
- 24M: ₹418.86 | model=historical_median | error band=±49.52%
- 36M: ₹492.01 | model=historical_median | error band=±57.24%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 124.75
- Current P/L: ₹87.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹103.68 | model=extra_trees | error band=±5.99%
- 6M: ₹95.89 | model=hist | error band=±9.06%
- 9M: ₹83.58 | model=hist | error band=±2.28%
- 12M: ₹92.52 | model=historical_median | error band=±2.65%
- 18M: ₹72.10 | model=hist | error band=±3.88%
- 24M: ₹72.18 | model=extra_trees | error band=±6.56%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 81.05000305175781
- Current P/L: ₹-1932.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹67.35 | model=hist | error band=±12.89%
- 6M: ₹63.83 | model=hist | error band=±30.77%
- 9M: ₹54.96 | model=hist | error band=±59.58%
- 12M: ₹62.32 | model=hist | error band=±74.04%
- 18M: ₹147.44 | model=historical_median | error band=±205.32%
- 24M: ₹150.95 | model=hist | error band=±57.21%
- 36M: ₹648.19 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 323.0
- Current P/L: ₹-8032.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹323.00 | model=historical_median | error band=±13.46%
- 6M: ₹330.78 | model=historical_median | error band=±17.04%
- 9M: ₹325.54 | model=historical_median | error band=±14.33%
- 12M: ₹328.16 | model=historical_median | error band=±17.45%
- 18M: ₹434.09 | model=historical_median | error band=±43.39%
- 24M: ₹530.72 | model=historical_median | error band=±79.04%
- 36M: ₹696.22 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 189.0500030517578
- Current P/L: ₹-9659.60
- First forecast horizon at/above purchase price: 24M

- 3M: ₹187.08 | model=extra_trees | error band=±8.94%
- 6M: ₹184.01 | model=extra_trees | error band=±21.50%
- 9M: ₹171.63 | model=extra_trees | error band=±27.81%
- 12M: ₹165.67 | model=extra_trees | error band=±24.65%
- 18M: ₹209.61 | model=hist | error band=±29.78%
- 24M: ₹245.74 | model=historical_median | error band=±45.45%
- 36M: ₹262.99 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 78.4800033569336
- Current P/L: ₹-11481.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹78.42 | model=historical_median | error band=±18.12%
- 6M: ₹84.57 | model=extra_trees | error band=±16.41%
- 9M: ₹77.27 | model=extra_trees | error band=±26.21%
- 12M: ₹76.09 | model=extra_trees | error band=±40.49%
- 18M: ₹87.67 | model=hist | error band=±38.65%
- 24M: ₹114.86 | model=hist | error band=±66.34%
- 36M: ₹157.32 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 31.729999542236328
- Current P/L: ₹-53855.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹26.63 | model=historical_median | error band=±12.32%
- 6M: ₹24.92 | model=extra_trees | error band=±15.55%
- 9M: ₹18.32 | model=hist | error band=±9.69%
- 12M: ₹24.08 | model=extra_trees | error band=±4.67%
- 18M: ₹16.45 | model=hist | error band=±4.00%
- 24M: N/A — Insufficient history for target_24M: 8 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 170.16000366210938
- Current P/L: ₹-8637.84
- First forecast horizon at/above purchase price: 24M

- 3M: ₹169.42 | model=historical_median | error band=±20.75%
- 6M: ₹167.19 | model=extra_trees | error band=±16.02%
- 9M: ₹174.01 | model=historical_median | error band=±23.31%
- 12M: ₹172.96 | model=historical_median | error band=±22.72%
- 18M: ₹185.35 | model=historical_median | error band=±23.20%
- 24M: ₹327.50 | model=extra_trees | error band=±36.28%
- 36M: ₹238.32 | model=historical_median | error band=±41.69%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 55.45000076293945
- Current P/L: ₹-3742.71
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹54.12 | model=extra_trees | error band=±17.32%
- 6M: ₹53.67 | model=historical_median | error band=±29.42%
- 9M: ₹53.81 | model=historical_median | error band=±35.31%
- 12M: ₹55.64 | model=historical_median | error band=±42.65%
- 18M: ₹62.71 | model=historical_median | error band=±66.42%
- 24M: ₹72.28 | model=historical_median | error band=±86.22%
- 36M: ₹98.12 | model=historical_median | error band=±95.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.1299991607666
- Current P/L: ₹-51480.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹15.80 | model=historical_median | error band=±26.45%
- 6M: ₹16.63 | model=historical_median | error band=±27.36%
- 9M: ₹15.04 | model=historical_median | error band=±42.49%
- 12M: ₹17.25 | model=historical_median | error band=±61.50%
- 18M: ₹19.99 | model=historical_median | error band=±129.65%
- 24M: ₹35.71 | model=hist | error band=±99.85%
- 36M: ₹40.65 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 441.8500061035156
- Current P/L: ₹-28776.75
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹425.38 | model=extra_trees | error band=±10.53%
- 6M: ₹428.35 | model=historical_median | error band=±21.31%
- 9M: ₹427.86 | model=historical_median | error band=±32.40%
- 12M: ₹491.81 | model=historical_median | error band=±48.64%
- 18M: ₹560.84 | model=historical_median | error band=±68.18%
- 24M: ₹532.29 | model=historical_median | error band=±65.73%
- 36M: ₹616.93 | model=hist | error band=±114.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.769999980926514
- Current P/L: ₹-7156.49
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.59 | model=historical_median | error band=±15.24%
- 6M: ₹4.67 | model=historical_median | error band=±21.60%
- 9M: ₹2.54 | model=hist | error band=±54.31%
- 12M: ₹3.51 | model=extra_trees | error band=±49.47%
- 18M: ₹5.21 | model=historical_median | error band=±55.81%
- 24M: ₹5.55 | model=historical_median | error band=±65.43%
- 36M: ₹4.45 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
