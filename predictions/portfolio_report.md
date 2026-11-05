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
- Current price: 27.350000381469727
- Current P/L: ₹-4490.00
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
- Current price: 16.239999771118164
- Current P/L: ₹-6611.66
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹16.21 | model=historical_median | error band=±17.82%
- 6M: ₹15.88 | model=historical_median | error band=±14.98%
- 9M: ₹15.55 | model=historical_median | error band=±23.03%
- 12M: ₹16.64 | model=extra_trees | error band=±21.35%
- 18M: ₹12.47 | model=historical_median | error band=±22.19%
- 24M: ₹14.23 | model=extra_trees | error band=±13.68%
- 36M: ₹4.87 | model=hist | error band=±16.14%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1313.4000244140625
- Current P/L: ₹-169.26
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1330.23 | model=historical_median | error band=±14.10%
- 6M: ₹1360.58 | model=historical_median | error band=±21.97%
- 9M: ₹1448.45 | model=hist | error band=±25.66%
- 12M: ₹1874.98 | model=hist | error band=±26.03%
- 18M: ₹1587.59 | model=historical_median | error band=±33.73%
- 24M: ₹1861.32 | model=extra_trees | error band=±37.53%
- 36M: ₹2363.92 | model=historical_median | error band=±43.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 316.70001220703125
- Current P/L: ₹-1312.48
- First forecast horizon at/above purchase price: 18M

- 3M: ₹326.90 | model=historical_median | error band=±15.08%
- 6M: ₹341.99 | model=historical_median | error band=±23.64%
- 9M: ₹348.54 | model=historical_median | error band=±18.85%
- 12M: ₹366.43 | model=historical_median | error band=±19.03%
- 18M: ₹418.66 | model=historical_median | error band=±22.96%
- 24M: ₹422.77 | model=historical_median | error band=±48.46%
- 36M: ₹490.19 | model=historical_median | error band=±54.06%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 110.1500015258789
- Current P/L: ₹-5022.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹96.27 | model=extra_trees | error band=±5.99%
- 6M: ₹100.59 | model=hist | error band=±5.48%
- 9M: ₹83.32 | model=extra_trees | error band=±2.27%
- 12M: ₹81.21 | model=historical_median | error band=±2.65%
- 18M: ₹65.53 | model=hist | error band=±3.88%
- 24M: ₹56.21 | model=extra_trees | error band=±7.50%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.12999725341797
- Current P/L: ₹-2116.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹67.64 | model=hist | error band=±12.89%
- 6M: ₹68.68 | model=hist | error band=±30.77%
- 9M: ₹68.50 | model=hist | error band=±59.58%
- 12M: ₹59.40 | model=hist | error band=±74.00%
- 18M: ₹162.98 | model=historical_median | error band=±206.28%
- 24M: ₹182.35 | model=hist | error band=±57.98%
- 36M: ₹657.50 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 364.5499877929688
- Current P/L: ₹-5124.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹370.47 | model=historical_median | error band=±12.16%
- 6M: ₹373.97 | model=historical_median | error band=±17.04%
- 9M: ₹373.69 | model=historical_median | error band=±14.33%
- 12M: ₹371.89 | model=historical_median | error band=±17.45%
- 18M: ₹489.08 | model=historical_median | error band=±43.39%
- 24M: ₹597.44 | model=historical_median | error band=±79.04%
- 36M: ₹491.23 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 198.3999938964844
- Current P/L: ₹-6761.10
- First forecast horizon at/above purchase price: 24M

- 3M: ₹185.63 | model=extra_trees | error band=±9.56%
- 6M: ₹171.57 | model=extra_trees | error band=±21.50%
- 9M: ₹168.02 | model=extra_trees | error band=±27.78%
- 12M: ₹184.36 | model=extra_trees | error band=±24.83%
- 18M: ₹149.65 | model=hist | error band=±29.78%
- 24M: ₹258.50 | model=historical_median | error band=±45.45%
- 36M: ₹277.77 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.9800033569336
- Current P/L: ₹-10731.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹80.96 | model=historical_median | error band=±18.12%
- 6M: ₹80.34 | model=extra_trees | error band=±16.41%
- 9M: ₹71.51 | model=extra_trees | error band=±26.21%
- 12M: ₹72.69 | model=extra_trees | error band=±40.49%
- 18M: ₹144.22 | model=hist | error band=±38.65%
- 24M: ₹154.91 | model=hist | error band=±66.34%
- 36M: ₹162.90 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 35.09000015258789
- Current P/L: ₹-44306.78
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹29.19 | model=historical_median | error band=±12.25%
- 6M: ₹24.32 | model=extra_trees | error band=±16.47%
- 9M: ₹23.26 | model=hist | error band=±9.69%
- 12M: ₹22.56 | model=historical_median | error band=±5.22%
- 18M: ₹17.76 | model=hist | error band=±4.41%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 180.0800018310547
- Current P/L: ₹-7784.72
- First forecast horizon at/above purchase price: 24M

- 3M: ₹179.08 | model=historical_median | error band=±20.77%
- 6M: ₹163.90 | model=extra_trees | error band=±20.87%
- 9M: ₹183.64 | model=historical_median | error band=±23.72%
- 12M: ₹185.46 | model=historical_median | error band=±16.77%
- 18M: ₹204.64 | model=historical_median | error band=±29.46%
- 24M: ₹322.30 | model=extra_trees | error band=±28.60%
- 36M: ₹246.03 | model=historical_median | error band=±26.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 57.54999923706055
- Current P/L: ₹-3589.41
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹50.11 | model=extra_trees | error band=±17.98%
- 6M: ₹55.77 | model=historical_median | error band=±29.42%
- 9M: ₹56.41 | model=historical_median | error band=±34.89%
- 12M: ₹57.81 | model=historical_median | error band=±42.65%
- 18M: ₹64.98 | model=historical_median | error band=±66.42%
- 24M: ₹73.24 | model=historical_median | error band=±86.22%
- 36M: ₹101.61 | model=historical_median | error band=±95.18%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 18.700000762939453
- Current P/L: ₹-47947.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹17.71 | model=historical_median | error band=±31.94%
- 6M: ₹18.08 | model=historical_median | error band=±27.32%
- 9M: ₹17.41 | model=historical_median | error band=±45.34%
- 12M: ₹18.75 | model=historical_median | error band=±61.50%
- 18M: ₹21.87 | model=historical_median | error band=±129.52%
- 24M: ₹22.09 | model=hist | error band=±99.85%
- 36M: ₹44.07 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 457.7000122070313
- Current P/L: ₹-27809.90
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹417.45 | model=extra_trees | error band=±14.99%
- 6M: ₹444.70 | model=historical_median | error band=±21.31%
- 9M: ₹447.31 | model=historical_median | error band=±32.40%
- 12M: ₹510.44 | model=historical_median | error band=±48.64%
- 18M: ₹583.55 | model=historical_median | error band=±68.18%
- 24M: ₹556.10 | model=historical_median | error band=±65.73%
- 36M: ₹768.23 | model=hist | error band=±104.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.099999904632568
- Current P/L: ₹-6833.42
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.93 | model=historical_median | error band=±15.24%
- 6M: ₹4.96 | model=historical_median | error band=±21.60%
- 9M: ₹2.94 | model=hist | error band=±54.31%
- 12M: ₹3.36 | model=extra_trees | error band=±49.47%
- 18M: ₹5.63 | model=historical_median | error band=±55.81%
- 24M: ₹5.73 | model=historical_median | error band=±65.43%
- 36M: ₹4.64 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
