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
- Current price: 27.100000381469727
- Current P/L: ₹-4740.00
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
- Current price: 15.729999542236328
- Current P/L: ₹-7071.68
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹15.70 | model=historical_median | error band=±17.82%
- 6M: ₹15.44 | model=historical_median | error band=±14.97%
- 9M: ₹15.07 | model=historical_median | error band=±23.03%
- 12M: ₹16.02 | model=extra_trees | error band=±21.45%
- 18M: ₹11.99 | model=historical_median | error band=±22.08%
- 24M: ₹12.73 | model=extra_trees | error band=±13.61%
- 36M: ₹4.53 | model=hist | error band=±16.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1311.0
- Current P/L: ₹-200.46
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1327.79 | model=historical_median | error band=±14.10%
- 6M: ₹1358.19 | model=historical_median | error band=±21.97%
- 9M: ₹1597.49 | model=hist | error band=±25.66%
- 12M: ₹2149.19 | model=hist | error band=±26.03%
- 18M: ₹1584.83 | model=historical_median | error band=±33.73%
- 24M: ₹1997.86 | model=extra_trees | error band=±37.52%
- 36M: ₹2360.85 | model=historical_median | error band=±43.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 321.95001220703125
- Current P/L: ₹-1175.98
- First forecast horizon at/above purchase price: 12M

- 3M: ₹332.32 | model=historical_median | error band=±15.08%
- 6M: ₹347.81 | model=historical_median | error band=±23.64%
- 9M: ₹354.47 | model=historical_median | error band=±18.85%
- 12M: ₹372.43 | model=historical_median | error band=±19.03%
- 18M: ₹425.55 | model=historical_median | error band=±22.96%
- 24M: ₹427.63 | model=historical_median | error band=±48.38%
- 36M: ₹498.08 | model=historical_median | error band=±54.14%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 106.0
- Current P/L: ₹-6475.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹99.49 | model=extra_trees | error band=±5.99%
- 6M: ₹97.00 | model=hist | error band=±5.18%
- 9M: ₹81.69 | model=extra_trees | error band=±2.26%
- 12M: ₹78.30 | model=historical_median | error band=±2.73%
- 18M: ₹63.05 | model=hist | error band=±3.89%
- 24M: ₹51.18 | model=extra_trees | error band=±7.74%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 77.83999633789062
- Current P/L: ₹-2574.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹65.39 | model=hist | error band=±12.89%
- 6M: ₹64.30 | model=hist | error band=±30.77%
- 9M: ₹72.39 | model=hist | error band=±59.58%
- 12M: ₹55.38 | model=hist | error band=±74.53%
- 18M: ₹158.32 | model=historical_median | error band=±206.28%
- 24M: ₹200.24 | model=hist | error band=±36.49%
- 36M: ₹617.97 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 360.0
- Current P/L: ₹-5442.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹365.85 | model=historical_median | error band=±12.16%
- 6M: ₹369.31 | model=historical_median | error band=±17.04%
- 9M: ₹369.08 | model=historical_median | error band=±14.33%
- 12M: ₹367.25 | model=historical_median | error band=±17.45%
- 18M: ₹483.88 | model=historical_median | error band=±43.39%
- 24M: ₹589.66 | model=historical_median | error band=±79.04%
- 36M: ₹524.84 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 194.5500030517578
- Current P/L: ₹-7954.60
- First forecast horizon at/above purchase price: 24M

- 3M: ₹174.67 | model=extra_trees | error band=±9.56%
- 6M: ₹162.91 | model=extra_trees | error band=±21.50%
- 9M: ₹154.59 | model=extra_trees | error band=±27.77%
- 12M: ₹171.49 | model=extra_trees | error band=±24.94%
- 18M: ₹135.42 | model=hist | error band=±29.78%
- 24M: ₹253.48 | model=historical_median | error band=±45.45%
- 36M: ₹272.58 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 81.8499984741211
- Current P/L: ₹-10470.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹82.50 | model=historical_median | error band=±18.12%
- 6M: ₹72.53 | model=extra_trees | error band=±16.41%
- 9M: ₹61.75 | model=extra_trees | error band=±26.21%
- 12M: ₹61.96 | model=extra_trees | error band=±40.49%
- 18M: ₹67.85 | model=hist | error band=±38.65%
- 24M: ₹108.36 | model=historical_median | error band=±66.34%
- 36M: ₹164.65 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 35.040000915527344
- Current P/L: ₹-44448.88
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.13 | model=historical_median | error band=±12.25%
- 6M: ₹22.20 | model=hist | error band=±16.40%
- 9M: ₹21.54 | model=hist | error band=±9.69%
- 12M: ₹21.33 | model=historical_median | error band=±5.58%
- 18M: ₹17.88 | model=hist | error band=±4.14%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 176.74000549316406
- Current P/L: ₹-8071.96
- First forecast horizon at/above purchase price: 24M

- 3M: ₹175.76 | model=historical_median | error band=±20.77%
- 6M: ₹162.27 | model=extra_trees | error band=±20.87%
- 9M: ₹180.31 | model=historical_median | error band=±23.70%
- 12M: ₹182.00 | model=historical_median | error band=±16.75%
- 18M: ₹200.79 | model=historical_median | error band=±29.46%
- 24M: ₹293.55 | model=extra_trees | error band=±28.64%
- 36M: ₹241.18 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 56.04999923706055
- Current P/L: ₹-3698.91
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹49.66 | model=extra_trees | error band=±17.98%
- 6M: ₹54.32 | model=historical_median | error band=±29.42%
- 9M: ₹54.95 | model=historical_median | error band=±34.89%
- 12M: ₹56.30 | model=historical_median | error band=±42.65%
- 18M: ₹63.29 | model=historical_median | error band=±66.42%
- 24M: ₹71.47 | model=historical_median | error band=±86.22%
- 36M: ₹98.92 | model=historical_median | error band=±96.69%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.43000030517578
- Current P/L: ₹-48555.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.46 | model=historical_median | error band=±31.94%
- 6M: ₹17.82 | model=historical_median | error band=±27.30%
- 9M: ₹17.15 | model=historical_median | error band=±45.34%
- 12M: ₹18.50 | model=historical_median | error band=±61.50%
- 18M: ₹21.29 | model=historical_median | error band=±129.77%
- 24M: ₹13.27 | model=hist | error band=±99.85%
- 36M: ₹43.33 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 450.0
- Current P/L: ₹-28279.60
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹399.58 | model=extra_trees | error band=±14.99%
- 6M: ₹437.21 | model=historical_median | error band=±21.31%
- 9M: ₹440.08 | model=historical_median | error band=±32.40%
- 12M: ₹502.47 | model=historical_median | error band=±48.64%
- 18M: ₹573.73 | model=historical_median | error band=±68.18%
- 24M: ₹546.75 | model=historical_median | error band=±65.73%
- 36M: ₹777.12 | model=hist | error band=±104.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 4.940000057220459
- Current P/L: ₹-6990.06
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.79 | model=historical_median | error band=±15.24%
- 6M: ₹4.80 | model=historical_median | error band=±21.60%
- 9M: ₹3.13 | model=hist | error band=±54.31%
- 12M: ₹2.55 | model=extra_trees | error band=±49.47%
- 18M: ₹5.45 | model=historical_median | error band=±55.81%
- 24M: ₹5.53 | model=historical_median | error band=±65.43%
- 36M: ₹4.49 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
