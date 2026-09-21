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
- Current price: 30.88999938964844
- Current P/L: ₹-950.00
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
- Current price: 23.239999771118164
- Current P/L: ₹-297.66
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.11 | model=historical_median | error band=±16.19%
- 6M: ₹21.99 | model=historical_median | error band=±18.82%
- 9M: ₹21.59 | model=historical_median | error band=±15.31%
- 12M: ₹25.88 | model=extra_trees | error band=±21.45%
- 18M: ₹16.99 | model=historical_median | error band=±16.38%
- 24M: ₹26.29 | model=extra_trees | error band=±21.17%
- 36M: ₹26.41 | model=hist | error band=±44.75%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1246.0
- Current P/L: ₹-1045.46
- First forecast horizon at/above purchase price: 6M

- 3M: ₹1289.91 | model=historical_median | error band=±10.42%
- 6M: ₹1340.27 | model=historical_median | error band=±13.67%
- 9M: ₹1478.20 | model=hist | error band=±17.68%
- 12M: ₹1599.89 | model=hist | error band=±18.10%
- 18M: ₹1435.43 | model=hist | error band=±12.10%
- 24M: ₹1530.38 | model=extra_trees | error band=±21.11%
- 36M: ₹1799.62 | model=extra_trees | error band=±28.57%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 327.5
- Current P/L: ₹-1031.68
- First forecast horizon at/above purchase price: 9M

- 3M: ₹343.13 | model=historical_median | error band=±13.53%
- 6M: ₹362.47 | model=historical_median | error band=±11.97%
- 9M: ₹376.91 | model=historical_median | error band=±16.85%
- 12M: ₹391.71 | model=historical_median | error band=±17.87%
- 18M: ₹433.61 | model=historical_median | error band=±13.38%
- 24M: ₹439.09 | model=historical_median | error band=±35.41%
- 36M: ₹495.35 | model=historical_median | error band=±51.33%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 111.45999908447266
- Current P/L: ₹-4564.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹100.05 | model=historical_median | error band=±9.28%
- 6M: ₹94.09 | model=historical_median | error band=±5.36%
- 9M: ₹91.53 | model=extra_trees | error band=±2.86%
- 12M: ₹82.10 | model=historical_median | error band=±2.47%
- 18M: ₹67.85 | model=hist | error band=±3.86%
- 24M: ₹79.88 | model=hist | error band=±6.76%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.55000305175781
- Current P/L: ₹-2032.00
- First forecast horizon at/above purchase price: 12M

- 3M: ₹74.74 | model=hist | error band=±12.70%
- 6M: ₹64.18 | model=hist | error band=±23.89%
- 9M: ₹53.13 | model=hist | error band=±28.54%
- 12M: ₹92.39 | model=hist | error band=±30.53%
- 18M: ₹172.97 | model=historical_median | error band=±40.31%
- 24M: ₹663.09 | model=hist | error band=±39.12%
- 36M: ₹584.95 | model=hist | error band=±171.45%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 367.1000061035156
- Current P/L: ₹-4945.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹378.39 | model=historical_median | error band=±11.28%
- 6M: ₹386.76 | model=historical_median | error band=±11.36%
- 9M: ₹380.96 | model=historical_median | error band=±10.91%
- 12M: ₹388.09 | model=historical_median | error band=±19.06%
- 18M: ₹522.82 | model=historical_median | error band=±49.60%
- 24M: ₹698.90 | model=historical_median | error band=±75.34%
- 36M: ₹561.14 | model=extra_trees | error band=±92.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 165.1699981689453
- Current P/L: ₹-17062.40
- First forecast horizon at/above purchase price: 24M

- 3M: ₹173.85 | model=extra_trees | error band=±11.59%
- 6M: ₹158.62 | model=extra_trees | error band=±27.13%
- 9M: ₹153.11 | model=extra_trees | error band=±22.35%
- 12M: ₹169.59 | model=extra_trees | error band=±21.63%
- 18M: ₹181.08 | model=hist | error band=±39.00%
- 24M: ₹244.94 | model=historical_median | error band=±33.38%
- 36M: ₹266.42 | model=historical_median | error band=±23.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 88.0
- Current P/L: ₹-8625.00
- First forecast horizon at/above purchase price: 24M

- 3M: ₹89.94 | model=historical_median | error band=±17.82%
- 6M: ₹68.49 | model=extra_trees | error band=±22.49%
- 9M: ₹62.46 | model=extra_trees | error band=±25.11%
- 12M: ₹65.77 | model=extra_trees | error band=±33.11%
- 18M: ₹80.03 | model=hist | error band=±39.50%
- 24M: ₹134.72 | model=historical_median | error band=±35.62%
- 36M: ₹185.75 | model=historical_median | error band=±32.74%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.95000076293945
- Current P/L: ₹-39020.66
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹30.13 | model=historical_median | error band=±36.52%
- 6M: ₹26.12 | model=hist | error band=±21.98%
- 9M: ₹31.22 | model=hist | error band=±15.20%
- 12M: ₹32.69 | model=hist | error band=±16.01%
- 18M: ₹19.44 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 193.8500061035156
- Current P/L: ₹-6600.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹196.45 | model=historical_median | error band=±19.99%
- 6M: ₹176.95 | model=extra_trees | error band=±10.78%
- 9M: ₹201.07 | model=historical_median | error band=±21.67%
- 12M: ₹205.44 | model=historical_median | error band=±27.73%
- 18M: ₹215.24 | model=historical_median | error band=±34.79%
- 24M: ₹329.08 | model=extra_trees | error band=±27.89%
- 36M: ₹238.68 | model=hist | error band=±26.84%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.400001525878906
- Current P/L: ₹-3162.36
- First forecast horizon at/above purchase price: 36M

- 3M: ₹62.19 | model=historical_median | error band=±14.56%
- 6M: ₹63.89 | model=historical_median | error band=±23.13%
- 9M: ₹64.20 | model=historical_median | error band=±27.54%
- 12M: ₹66.15 | model=historical_median | error band=±29.46%
- 18M: ₹71.37 | model=historical_median | error band=±43.53%
- 24M: ₹82.11 | model=historical_median | error band=±41.51%
- 36M: ₹111.18 | model=historical_median | error band=±125.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.09000015258789
- Current P/L: ₹-42570.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.60 | model=historical_median | error band=±31.10%
- 6M: ₹22.60 | model=extra_trees | error band=±22.87%
- 9M: ₹20.40 | model=extra_trees | error band=±48.34%
- 12M: ₹22.65 | model=historical_median | error band=±72.69%
- 18M: ₹13.16 | model=extra_trees | error band=±143.81%
- 24M: ₹35.17 | model=historical_median | error band=±97.27%
- 36M: ₹50.56 | model=historical_median | error band=±64.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 471.9500122070313
- Current P/L: ₹-26940.65
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹414.42 | model=hist | error band=±14.05%
- 6M: ₹468.45 | model=historical_median | error band=±19.53%
- 9M: ₹478.56 | model=historical_median | error band=±30.16%
- 12M: ₹567.11 | model=historical_median | error band=±25.79%
- 18M: ₹618.13 | model=historical_median | error band=±36.59%
- 24M: ₹685.18 | model=historical_median | error band=±39.81%
- 36M: ₹428.40 | model=extra_trees | error band=±19.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.099999904632568
- Current P/L: ₹-6833.42
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.77 | model=historical_median | error band=±25.53%
- 6M: ₹4.74 | model=historical_median | error band=±29.85%
- 9M: ₹2.49 | model=extra_trees | error band=±47.90%
- 12M: ₹2.08 | model=extra_trees | error band=±53.23%
- 18M: ₹5.66 | model=historical_median | error band=±69.76%
- 24M: ₹6.08 | model=historical_median | error band=±67.98%
- 36M: ₹4.55 | model=historical_median | error band=±87.27%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
