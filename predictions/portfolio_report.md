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
- Current price: 26.739999771118164
- Current P/L: ₹-5100.00
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
- Current price: 17.239999771118164
- Current P/L: ₹-5709.66
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹17.20 | model=historical_median | error band=±17.82%
- 6M: ₹16.85 | model=historical_median | error band=±14.97%
- 9M: ₹16.50 | model=historical_median | error band=±19.95%
- 12M: ₹17.94 | model=extra_trees | error band=±21.36%
- 18M: ₹13.20 | model=historical_median | error band=±21.60%
- 24M: ₹14.96 | model=extra_trees | error band=±13.75%
- 36M: ₹8.83 | model=hist | error band=±16.34%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1335.4000244140625
- Current P/L: ₹116.74
- First forecast horizon at/above purchase price: 3M

- 3M: ₹1352.37 | model=historical_median | error band=±14.10%
- 6M: ₹1383.14 | model=historical_median | error band=±21.97%
- 9M: ₹1356.47 | model=extra_trees | error band=±25.66%
- 12M: ₹1619.11 | model=hist | error band=±26.03%
- 18M: ₹1789.03 | model=hist | error band=±33.73%
- 24M: ₹1635.04 | model=extra_trees | error band=±37.82%
- 36M: ₹2403.11 | model=historical_median | error band=±43.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 327.0
- Current P/L: ₹-1044.68
- First forecast horizon at/above purchase price: 12M

- 3M: ₹338.07 | model=historical_median | error band=±15.10%
- 6M: ₹352.59 | model=historical_median | error band=±23.64%
- 9M: ₹358.92 | model=historical_median | error band=±18.89%
- 12M: ₹373.43 | model=historical_median | error band=±18.98%
- 18M: ₹433.33 | model=historical_median | error band=±22.92%
- 24M: ₹433.73 | model=historical_median | error band=±53.20%
- 36M: ₹501.01 | model=historical_median | error band=±68.53%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 120.1999969482422
- Current P/L: ₹-1505.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹99.03 | model=extra_trees | error band=±6.00%
- 6M: ₹96.94 | model=hist | error band=±9.02%
- 9M: ₹86.01 | model=extra_trees | error band=±2.28%
- 12M: ₹88.77 | model=historical_median | error band=±2.65%
- 18M: ₹66.69 | model=hist | error band=±3.88%
- 24M: ₹64.44 | model=extra_trees | error band=±6.92%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 86.69999694824219
- Current P/L: ₹-802.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹63.52 | model=hist | error band=±12.89%
- 6M: ₹68.08 | model=hist | error band=±30.77%
- 9M: ₹72.52 | model=hist | error band=±59.58%
- 12M: ₹55.77 | model=hist | error band=±74.00%
- 18M: ₹166.97 | model=historical_median | error band=±206.28%
- 24M: ₹145.74 | model=hist | error band=±55.98%
- 36M: ₹721.45 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 360.0
- Current P/L: ₹-5442.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹365.83 | model=historical_median | error band=±12.16%
- 6M: ₹369.23 | model=historical_median | error band=±17.04%
- 9M: ₹368.97 | model=historical_median | error band=±14.33%
- 12M: ₹367.08 | model=historical_median | error band=±17.45%
- 18M: ₹482.98 | model=historical_median | error band=±43.39%
- 24M: ₹590.41 | model=historical_median | error band=±79.04%
- 36M: ₹540.49 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 197.9900054931641
- Current P/L: ₹-6888.20
- First forecast horizon at/above purchase price: 24M

- 3M: ₹190.44 | model=extra_trees | error band=±9.56%
- 6M: ₹184.22 | model=extra_trees | error band=±21.50%
- 9M: ₹179.06 | model=extra_trees | error band=±27.72%
- 12M: ₹189.51 | model=extra_trees | error band=±24.44%
- 18M: ₹181.62 | model=hist | error band=±29.78%
- 24M: ₹257.97 | model=historical_median | error band=±45.45%
- 36M: ₹276.91 | model=historical_median | error band=±45.37%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 80.0199966430664
- Current P/L: ₹-11019.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹79.98 | model=historical_median | error band=±18.12%
- 6M: ₹84.73 | model=extra_trees | error band=±16.41%
- 9M: ₹75.22 | model=extra_trees | error band=±26.21%
- 12M: ₹76.69 | model=extra_trees | error band=±40.49%
- 18M: ₹127.94 | model=hist | error band=±38.65%
- 24M: ₹109.19 | model=hist | error band=±66.34%
- 36M: ₹160.82 | model=historical_median | error band=±106.12%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 34.43000030517578
- Current P/L: ₹-46182.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹28.69 | model=historical_median | error band=±12.32%
- 6M: ₹24.52 | model=extra_trees | error band=±16.40%
- 9M: ₹23.47 | model=hist | error band=±9.69%
- 12M: ₹23.59 | model=historical_median | error band=±4.71%
- 18M: ₹17.30 | model=hist | error band=±4.61%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 174.99000549316406
- Current P/L: ₹-8222.46
- First forecast horizon at/above purchase price: 24M

- 3M: ₹174.07 | model=historical_median | error band=±20.77%
- 6M: ₹163.25 | model=extra_trees | error band=±20.87%
- 9M: ₹178.28 | model=historical_median | error band=±23.72%
- 12M: ₹180.19 | model=historical_median | error band=±16.77%
- 18M: ₹198.91 | model=historical_median | error band=±29.46%
- 24M: ₹276.39 | model=extra_trees | error band=±28.46%
- 36M: ₹239.18 | model=historical_median | error band=±37.19%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 59.560001373291016
- Current P/L: ₹-3442.68
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹52.55 | model=extra_trees | error band=±17.98%
- 6M: ₹57.75 | model=historical_median | error band=±29.42%
- 9M: ₹58.37 | model=historical_median | error band=±34.89%
- 12M: ₹59.80 | model=historical_median | error band=±42.65%
- 18M: ₹67.28 | model=historical_median | error band=±60.32%
- 24M: ₹77.25 | model=historical_median | error band=±86.22%
- 36M: ₹105.26 | model=historical_median | error band=±95.65%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 19.31999969482422
- Current P/L: ₹-46552.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹18.31 | model=historical_median | error band=±31.94%
- 6M: ₹18.70 | model=historical_median | error band=±27.39%
- 9M: ₹17.97 | model=historical_median | error band=±45.34%
- 12M: ₹19.38 | model=historical_median | error band=±61.50%
- 18M: ₹22.39 | model=historical_median | error band=±129.72%
- 24M: ₹20.58 | model=hist | error band=±99.85%
- 36M: ₹45.56 | model=historical_median | error band=±119.70%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 472.1000061035156
- Current P/L: ₹-26931.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹476.06 | model=extra_trees | error band=±14.96%
- 6M: ₹458.58 | model=historical_median | error band=±21.31%
- 9M: ₹461.07 | model=historical_median | error band=±32.40%
- 12M: ₹526.30 | model=historical_median | error band=±48.64%
- 18M: ₹601.20 | model=historical_median | error band=±68.18%
- 24M: ₹573.03 | model=historical_median | error band=±65.92%
- 36M: ₹882.22 | model=hist | error band=±104.31%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.400000095367432
- Current P/L: ₹-6539.72
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹5.23 | model=historical_median | error band=±15.24%
- 6M: ₹5.24 | model=historical_median | error band=±21.60%
- 9M: ₹3.08 | model=hist | error band=±54.31%
- 12M: ₹4.53 | model=extra_trees | error band=±49.47%
- 18M: ₹5.96 | model=historical_median | error band=±55.81%
- 24M: ₹6.11 | model=historical_median | error band=±65.43%
- 36M: ₹4.93 | model=historical_median | error band=±59.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
