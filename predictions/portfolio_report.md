# Portfolio forecast report

Models retrain from the latest market history on every scheduled run.
The selected model is chosen using chronological holdout error, with a zero-return baseline included.
Forecast calibration uses completed real forecast errors for the same stock/horizon when available, then walk-forward errors.
Error bands are empirical historical-error bands, not guarantees.
Forecast horizons marked unavailable have insufficient labelled historical data and are not treated as failed forecasts.
The first forecast horizon is a model checkpoint, not a guaranteed date.
Averaging scenarios are mathematical cost-basis calculations. The profit-signal table is a model-generated scenario, not a guarantee or personalized financial advice.

## Vedanta Iron & Steel (VISL.NS)
- Quantity: 1000.0
- Purchase price: 31.84
- Current price: 30.90999984741211
- Current P/L: ₹-930.00
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
- Current price: 22.71999931335449
- Current P/L: ₹-766.70
- First forecast horizon at/above purchase price: 12M

- 3M: ₹22.80 | model=zero_baseline | error band=±16.19%
- 6M: ₹22.27 | model=zero_baseline | error band=±18.82%
- 9M: ₹22.19 | model=zero_baseline | error band=±15.31%
- 12M: ₹25.50 | model=extra_trees | error band=±21.45%
- 18M: ₹22.72 | model=zero_baseline | error band=±16.38%
- 24M: ₹23.86 | model=zero_baseline | error band=±20.74%
- 36M: ₹25.37 | model=hist | error band=±44.75%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1226.4000244140625
- Current P/L: ₹-1300.26
- First forecast horizon at/above purchase price: 36M

- 3M: ₹1208.26 | model=zero_baseline | error band=±10.42%
- 6M: ₹1188.67 | model=zero_baseline | error band=±13.67%
- 9M: ₹1213.64 | model=zero_baseline | error band=±17.68%
- 12M: ₹1225.89 | model=zero_baseline | error band=±18.10%
- 18M: ₹1242.56 | model=zero_baseline | error band=±12.10%
- 24M: ₹1297.91 | model=zero_baseline | error band=±21.11%
- 36M: ₹1350.84 | model=zero_baseline | error band=±28.57%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.6499938964844
- Current P/L: ₹-1131.78
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹321.82 | model=zero_baseline | error band=±13.53%
- 6M: ₹325.09 | model=zero_baseline | error band=±11.97%
- 9M: ₹329.00 | model=zero_baseline | error band=±16.88%
- 12M: ₹319.26 | model=zero_baseline | error band=±17.87%
- 18M: ₹318.06 | model=zero_baseline | error band=±14.16%
- 24M: ₹320.59 | model=zero_baseline | error band=±35.91%
- 36M: ₹357.60 | model=extra_trees | error band=±52.13%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 114.31999969482422
- Current P/L: ₹-3563.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹111.81 | model=zero_baseline | error band=±9.07%
- 6M: ₹98.65 | model=extra_trees | error band=±4.99%
- 9M: ₹92.57 | model=extra_trees | error band=±2.86%
- 12M: ₹82.67 | model=extra_trees | error band=±2.45%
- 18M: ₹67.26 | model=hist | error band=±3.87%
- 24M: ₹83.07 | model=hist | error band=±6.64%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 81.5
- Current P/L: ₹-1842.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹77.64 | model=zero_baseline | error band=±12.70%
- 6M: ₹74.48 | model=zero_baseline | error band=±23.89%
- 9M: ₹73.01 | model=zero_baseline | error band=±28.54%
- 12M: ₹71.91 | model=zero_baseline | error band=±30.53%
- 18M: ₹69.27 | model=zero_baseline | error band=±40.31%
- 24M: ₹73.66 | model=zero_baseline | error band=±39.39%
- 36M: ₹82.64 | model=zero_baseline | error band=±171.42%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 374.7999877929688
- Current P/L: ₹-4406.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹373.72 | model=zero_baseline | error band=±11.28%
- 6M: ₹377.55 | model=zero_baseline | error band=±11.36%
- 9M: ₹367.86 | model=zero_baseline | error band=±10.91%
- 12M: ₹369.40 | model=zero_baseline | error band=±19.06%
- 18M: ₹378.89 | model=zero_baseline | error band=±49.36%
- 24M: ₹420.15 | model=zero_baseline | error band=±75.35%
- 36M: ₹431.02 | model=zero_baseline | error band=±92.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 166.8300018310547
- Current P/L: ₹-16547.80
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹171.91 | model=extra_trees | error band=±11.63%
- 6M: ₹158.77 | model=zero_baseline | error band=±27.13%
- 9M: ₹162.60 | model=zero_baseline | error band=±22.37%
- 12M: ₹169.52 | model=zero_baseline | error band=±21.62%
- 18M: ₹176.36 | model=hist | error band=±38.98%
- 24M: ₹190.10 | model=zero_baseline | error band=±33.38%
- 36M: ₹174.47 | model=zero_baseline | error band=±23.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.11000061035156
- Current P/L: ₹-9192.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹84.65 | model=zero_baseline | error band=±17.82%
- 6M: ₹68.18 | model=extra_trees | error band=±22.49%
- 9M: ₹78.76 | model=zero_baseline | error band=±25.11%
- 12M: ₹81.06 | model=zero_baseline | error band=±33.11%
- 18M: ₹86.01 | model=zero_baseline | error band=±39.50%
- 24M: ₹89.23 | model=zero_baseline | error band=±35.62%
- 36M: ₹80.05 | model=zero_baseline | error band=±32.74%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.38999938964844
- Current P/L: ₹-40612.18
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹36.92 | model=zero_baseline | error band=±36.52%
- 6M: ₹36.76 | model=zero_baseline | error band=±21.98%
- 9M: ₹31.52 | model=hist | error band=±15.20%
- 12M: ₹35.07 | model=zero_baseline | error band=±14.88%
- 18M: ₹20.43 | model=hist | error band=±4.22%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 194.25
- Current P/L: ₹-6566.10
- First forecast horizon at/above purchase price: 18M

- 3M: ₹195.26 | model=zero_baseline | error band=±19.99%
- 6M: ₹189.20 | model=zero_baseline | error band=±10.81%
- 9M: ₹189.58 | model=zero_baseline | error band=±21.67%
- 12M: ₹193.59 | model=zero_baseline | error band=±27.73%
- 18M: ₹280.03 | model=extra_trees | error band=±34.79%
- 24M: ₹325.93 | model=extra_trees | error band=±27.49%
- 36M: ₹364.99 | model=extra_trees | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.95000076293945
- Current P/L: ₹-3122.21
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹60.28 | model=zero_baseline | error band=±14.56%
- 6M: ₹60.58 | model=zero_baseline | error band=±20.65%
- 9M: ₹57.18 | model=zero_baseline | error band=±27.54%
- 12M: ₹56.65 | model=zero_baseline | error band=±29.46%
- 18M: ₹54.49 | model=zero_baseline | error band=±43.53%
- 24M: ₹56.98 | model=zero_baseline | error band=±41.34%
- 36M: ₹106.62 | model=extra_trees | error band=±114.03%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.1299991607666
- Current P/L: ₹-42480.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹20.43 | model=zero_baseline | error band=±31.10%
- 6M: ₹23.04 | model=extra_trees | error band=±22.94%
- 9M: ₹20.82 | model=extra_trees | error band=±48.34%
- 12M: ₹21.22 | model=zero_baseline | error band=±72.61%
- 18M: ₹15.05 | model=extra_trees | error band=±143.81%
- 24M: ₹14.27 | model=hist | error band=±98.06%
- 36M: ₹7.19 | model=extra_trees | error band=±63.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 476.75
- Current P/L: ₹-26647.85
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹449.67 | model=zero_baseline | error band=±14.05%
- 6M: ₹446.27 | model=zero_baseline | error band=±19.53%
- 9M: ₹430.09 | model=zero_baseline | error band=±30.16%
- 12M: ₹432.66 | model=zero_baseline | error band=±25.79%
- 18M: ₹417.05 | model=zero_baseline | error band=±36.59%
- 24M: ₹508.60 | model=zero_baseline | error band=±39.81%
- 36M: ₹466.08 | model=zero_baseline | error band=±19.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.230000019073486
- Current P/L: ₹-6706.15
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹5.04 | model=zero_baseline | error band=±25.24%
- 6M: ₹4.60 | model=zero_baseline | error band=±29.82%
- 9M: ₹4.45 | model=zero_baseline | error band=±47.90%
- 12M: ₹4.45 | model=zero_baseline | error band=±53.23%
- 18M: ₹4.45 | model=zero_baseline | error band=±69.76%
- 24M: ₹4.50 | model=zero_baseline | error band=±67.98%
- 36M: ₹4.45 | model=zero_baseline | error band=±87.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
