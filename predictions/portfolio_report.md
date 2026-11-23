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
- Current price: 23.8799991607666
- Current P/L: ₹-7960.00
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
- Current price: 17.90999984741211
- Current P/L: ₹-5105.32
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.86 | model=historical_median | error band=±17.82%
- 6M: ₹17.49 | model=historical_median | error band=±14.97%
- 9M: ₹17.12 | model=historical_median | error band=±23.03%
- 12M: ₹18.66 | model=extra_trees | error band=±21.72%
- 18M: ₹13.83 | model=historical_median | error band=±21.77%
- 24M: ₹21.26 | model=hist | error band=±13.48%
- 36M: ₹29.38 | model=hist | error band=±16.40%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1377.5
- Current P/L: ₹664.04
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1394.49 | model=historical_median | error band=±14.10%
- 6M: ₹1426.24 | model=historical_median | error band=±21.97%
- 9M: ₹1328.61 | model=hist | error band=±18.98%
- 12M: ₹1393.90 | model=hist | error band=±26.03%
- 18M: ₹1628.82 | model=hist | error band=±33.73%
- 24M: ₹1484.56 | model=extra_trees | error band=±37.68%
- 36M: ₹2469.30 | model=historical_median | error band=±43.26%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 321.5
- Current P/L: ₹-1187.68
- First forecast horizon at/above purchase price: 18M

- 3M: ₹330.98 | model=historical_median | error band=±15.08%
- 6M: ₹347.73 | model=historical_median | error band=±23.64%
- 9M: ₹352.33 | model=historical_median | error band=±19.87%
- 12M: ₹364.44 | model=historical_median | error band=±19.03%
- 18M: ₹428.64 | model=historical_median | error band=±28.07%
- 24M: ₹424.05 | model=historical_median | error band=±42.84%
- 36M: ₹501.32 | model=historical_median | error band=±52.77%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 131.6999969482422
- Current P/L: ₹2520.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹108.59 | model=extra_trees | error band=±5.99%
- 6M: ₹100.21 | model=hist | error band=±9.07%
- 9M: ₹91.20 | model=hist | error band=±2.28%
- 12M: ₹97.45 | model=historical_median | error band=±2.65%
- 18M: ₹73.68 | model=hist | error band=±3.88%
- 24M: ₹75.15 | model=extra_trees | error band=±5.80%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 83.73999786376953
- Current P/L: ₹-1394.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹67.11 | model=hist | error band=±12.89%
- 6M: ₹64.93 | model=hist | error band=±30.77%
- 9M: ₹54.07 | model=hist | error band=±59.58%
- 12M: ₹61.98 | model=hist | error band=±74.04%
- 18M: ₹153.44 | model=historical_median | error band=±205.32%
- 24M: ₹154.43 | model=hist | error band=±57.10%
- 36M: ₹656.87 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 339.70001220703125
- Current P/L: ₹-6863.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹345.11 | model=historical_median | error band=±12.16%
- 6M: ₹347.99 | model=historical_median | error band=±17.04%
- 9M: ₹342.46 | model=historical_median | error band=±14.33%
- 12M: ₹345.65 | model=historical_median | error band=±17.45%
- 18M: ₹455.71 | model=historical_median | error band=±43.39%
- 24M: ₹558.02 | model=historical_median | error band=±79.04%
- 36M: ₹595.82 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 185.6999969482422
- Current P/L: ₹-10698.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹179.42 | model=extra_trees | error band=±9.56%
- 6M: ₹171.43 | model=extra_trees | error band=±21.50%
- 9M: ₹164.60 | model=extra_trees | error band=±27.80%
- 12M: ₹155.35 | model=extra_trees | error band=±24.53%
- 18M: ₹200.42 | model=hist | error band=±29.78%
- 24M: ₹241.26 | model=historical_median | error band=±45.45%
- 36M: ₹258.61 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 76.83000183105469
- Current P/L: ₹-11976.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹76.77 | model=historical_median | error band=±18.12%
- 6M: ₹82.24 | model=extra_trees | error band=±16.41%
- 9M: ₹72.08 | model=extra_trees | error band=±26.21%
- 12M: ₹72.77 | model=extra_trees | error band=±40.49%
- 18M: ₹68.98 | model=hist | error band=±38.65%
- 24M: ₹108.04 | model=hist | error band=±66.34%
- 36M: ₹154.20 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 32.59000015258789
- Current P/L: ₹-51411.78
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹27.32 | model=historical_median | error band=±12.25%
- 6M: ₹24.30 | model=extra_trees | error band=±15.58%
- 9M: ₹21.51 | model=hist | error band=±9.69%
- 12M: ₹21.40 | model=historical_median | error band=±4.67%
- 18M: ₹16.22 | model=hist | error band=±4.04%
- 24M: N/A — Insufficient history for target_24M: 6 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 175.85000610351562
- Current P/L: ₹-8148.50
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.06 | model=historical_median | error band=±20.72%
- 6M: ₹168.51 | model=extra_trees | error band=±16.01%
- 9M: ₹179.83 | model=historical_median | error band=±23.61%
- 12M: ₹178.73 | model=historical_median | error band=±23.06%
- 18M: ₹192.99 | model=historical_median | error band=±26.32%
- 24M: ₹331.08 | model=extra_trees | error band=±33.37%
- 36M: ₹246.89 | model=historical_median | error band=±41.66%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 55.77999877929688
- Current P/L: ₹-3718.62
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹53.72 | model=extra_trees | error band=±17.98%
- 6M: ₹53.99 | model=historical_median | error band=±29.42%
- 9M: ₹54.13 | model=historical_median | error band=±35.31%
- 12M: ₹55.98 | model=historical_median | error band=±42.65%
- 18M: ₹63.08 | model=historical_median | error band=±66.42%
- 24M: ₹71.18 | model=historical_median | error band=±86.22%
- 36M: ₹98.69 | model=historical_median | error band=±95.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 17.65999984741211
- Current P/L: ₹-50287.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹16.73 | model=historical_median | error band=±31.94%
- 6M: ₹17.11 | model=historical_median | error band=±27.32%
- 9M: ₹15.49 | model=historical_median | error band=±42.49%
- 12M: ₹17.73 | model=historical_median | error band=±61.50%
- 18M: ₹20.59 | model=historical_median | error band=±129.43%
- 24M: ₹31.14 | model=hist | error band=±99.85%
- 36M: ₹41.82 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 448.0499877929688
- Current P/L: ₹-28398.55
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹436.21 | model=extra_trees | error band=±10.50%
- 6M: ₹434.76 | model=historical_median | error band=±21.31%
- 9M: ₹434.19 | model=historical_median | error band=±32.40%
- 12M: ₹498.88 | model=historical_median | error band=±48.64%
- 18M: ₹569.17 | model=historical_median | error band=±68.18%
- 24M: ₹540.32 | model=historical_median | error band=±65.73%
- 36M: ₹636.48 | model=hist | error band=±114.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.849999904632568
- Current P/L: ₹-7078.17
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.62 | model=historical_median | error band=±15.24%
- 6M: ₹4.74 | model=historical_median | error band=±21.60%
- 9M: ₹3.29 | model=extra_trees | error band=±54.31%
- 12M: ₹2.96 | model=hist | error band=±49.47%
- 18M: ₹5.31 | model=historical_median | error band=±55.81%
- 24M: ₹5.62 | model=historical_median | error band=±65.43%
- 36M: ₹4.52 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
