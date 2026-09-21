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
- Current price: 30.850000381469727
- Current P/L: ₹-990.00
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

- 3M: ₹23.32 | model=zero_baseline | error band=±16.19%
- 6M: ₹22.78 | model=zero_baseline | error band=±18.82%
- 9M: ₹22.72 | model=zero_baseline | error band=±15.31%
- 12M: ₹25.98 | model=extra_trees | error band=±21.45%
- 18M: ₹23.22 | model=zero_baseline | error band=±16.38%
- 24M: ₹24.41 | model=zero_baseline | error band=±20.94%
- 36M: ₹26.59 | model=hist | error band=±44.75%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1244.199951171875
- Current P/L: ₹-1068.86
- First forecast horizon at/above purchase price: 36M

- 3M: ₹1225.80 | model=zero_baseline | error band=±10.42%
- 6M: ₹1205.92 | model=zero_baseline | error band=±13.67%
- 9M: ₹1231.26 | model=zero_baseline | error band=±17.68%
- 12M: ₹1243.68 | model=zero_baseline | error band=±18.10%
- 18M: ₹1260.59 | model=zero_baseline | error band=±12.10%
- 24M: ₹1316.75 | model=zero_baseline | error band=±21.11%
- 36M: ₹1370.44 | model=zero_baseline | error band=±28.57%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 328.1000061035156
- Current P/L: ₹-1016.08
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹326.32 | model=zero_baseline | error band=±13.53%
- 6M: ₹329.30 | model=zero_baseline | error band=±11.97%
- 9M: ₹333.60 | model=zero_baseline | error band=±16.59%
- 12M: ₹323.51 | model=zero_baseline | error band=±17.87%
- 18M: ₹322.41 | model=zero_baseline | error band=±13.16%
- 24M: ₹325.81 | model=zero_baseline | error band=±34.12%
- 36M: ₹348.05 | model=extra_trees | error band=±51.35%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 111.5199966430664
- Current P/L: ₹-4543.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹109.07 | model=zero_baseline | error band=±9.28%
- 6M: ₹98.27 | model=extra_trees | error band=±5.14%
- 9M: ₹91.45 | model=extra_trees | error band=±2.86%
- 12M: ₹81.64 | model=extra_trees | error band=±2.54%
- 18M: ₹68.02 | model=hist | error band=±3.76%
- 24M: ₹79.98 | model=hist | error band=±6.76%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.55000305175781
- Current P/L: ₹-2032.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹76.74 | model=zero_baseline | error band=±12.70%
- 6M: ₹73.61 | model=zero_baseline | error band=±23.89%
- 9M: ₹72.16 | model=zero_baseline | error band=±28.54%
- 12M: ₹71.05 | model=zero_baseline | error band=±30.53%
- 18M: ₹68.47 | model=zero_baseline | error band=±40.31%
- 24M: ₹72.44 | model=zero_baseline | error band=±40.86%
- 36M: ₹587.27 | model=hist | error band=±171.42%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 367.2999877929688
- Current P/L: ₹-4931.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹366.24 | model=zero_baseline | error band=±11.28%
- 6M: ₹369.99 | model=zero_baseline | error band=±11.36%
- 9M: ₹360.55 | model=zero_baseline | error band=±10.91%
- 12M: ₹362.01 | model=zero_baseline | error band=±19.06%
- 18M: ₹371.24 | model=zero_baseline | error band=±49.45%
- 24M: ₹412.17 | model=zero_baseline | error band=±75.27%
- 36M: ₹422.39 | model=zero_baseline | error band=±92.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 165.0
- Current P/L: ₹-17115.10
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹173.91 | model=extra_trees | error band=±11.61%
- 6M: ₹156.94 | model=zero_baseline | error band=±27.13%
- 9M: ₹160.81 | model=zero_baseline | error band=±22.36%
- 12M: ₹167.52 | model=zero_baseline | error band=±21.64%
- 18M: ₹184.60 | model=hist | error band=±39.04%
- 24M: ₹188.01 | model=zero_baseline | error band=±33.38%
- 36M: ₹172.56 | model=zero_baseline | error band=±23.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 87.9000015258789
- Current P/L: ₹-8655.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹86.41 | model=zero_baseline | error band=±17.82%
- 6M: ₹68.22 | model=extra_trees | error band=±22.49%
- 9M: ₹80.39 | model=zero_baseline | error band=±25.11%
- 12M: ₹82.75 | model=zero_baseline | error band=±33.11%
- 18M: ₹87.80 | model=zero_baseline | error band=±39.50%
- 24M: ₹91.08 | model=zero_baseline | error band=±35.62%
- 36M: ₹81.70 | model=zero_baseline | error band=±32.74%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.959999084472656
- Current P/L: ₹-38992.24
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹37.49 | model=zero_baseline | error band=±36.52%
- 6M: ₹37.34 | model=zero_baseline | error band=±21.98%
- 9M: ₹31.33 | model=hist | error band=±15.20%
- 12M: ₹35.62 | model=zero_baseline | error band=±15.08%
- 18M: ₹19.44 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 193.3999938964844
- Current P/L: ₹-6639.20
- First forecast horizon at/above purchase price: 18M

- 3M: ₹194.40 | model=zero_baseline | error band=±19.99%
- 6M: ₹188.39 | model=zero_baseline | error band=±10.79%
- 9M: ₹188.85 | model=zero_baseline | error band=±21.67%
- 12M: ₹192.75 | model=zero_baseline | error band=±27.73%
- 18M: ₹280.11 | model=extra_trees | error band=±34.79%
- 24M: ₹326.04 | model=extra_trees | error band=±27.72%
- 36M: ₹231.99 | model=hist | error band=±26.89%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.43000030517578
- Current P/L: ₹-3160.17
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹59.79 | model=zero_baseline | error band=±14.56%
- 6M: ₹60.09 | model=zero_baseline | error band=±20.65%
- 9M: ₹56.75 | model=zero_baseline | error band=±27.54%
- 12M: ₹56.19 | model=zero_baseline | error band=±29.67%
- 18M: ₹54.05 | model=zero_baseline | error band=±43.53%
- 24M: ₹56.62 | model=zero_baseline | error band=±41.34%
- 36M: ₹98.75 | model=extra_trees | error band=±116.46%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.190000534057617
- Current P/L: ₹-42345.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹20.49 | model=zero_baseline | error band=±31.10%
- 6M: ₹22.35 | model=extra_trees | error band=±23.32%
- 9M: ₹20.40 | model=extra_trees | error band=±48.34%
- 12M: ₹21.29 | model=zero_baseline | error band=±72.66%
- 18M: ₹12.76 | model=extra_trees | error band=±143.81%
- 24M: ₹16.49 | model=hist | error band=±96.66%
- 36M: ₹6.71 | model=extra_trees | error band=±62.69%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 471.25
- Current P/L: ₹-26983.35
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹444.48 | model=zero_baseline | error band=±14.05%
- 6M: ₹441.12 | model=zero_baseline | error band=±19.53%
- 9M: ₹425.13 | model=zero_baseline | error band=±30.16%
- 12M: ₹427.67 | model=zero_baseline | error band=±25.79%
- 18M: ₹412.24 | model=zero_baseline | error band=±36.59%
- 24M: ₹502.73 | model=zero_baseline | error band=±39.81%
- 36M: ₹460.70 | model=zero_baseline | error band=±19.47%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.079999923706055
- Current P/L: ₹-6853.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.86 | model=zero_baseline | error band=±25.20%
- 6M: ₹4.47 | model=zero_baseline | error band=±30.52%
- 9M: ₹4.32 | model=zero_baseline | error band=±47.90%
- 12M: ₹4.32 | model=zero_baseline | error band=±53.23%
- 18M: ₹4.32 | model=zero_baseline | error band=±69.76%
- 24M: ₹4.32 | model=zero_baseline | error band=±67.98%
- 36M: ₹4.32 | model=zero_baseline | error band=±87.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
