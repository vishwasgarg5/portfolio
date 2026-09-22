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
- Current price: 32.209999084472656
- Current P/L: ₹370.00
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
- Current price: 23.209999084472656
- Current P/L: ₹-324.72
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.22 | model=historical_median | error band=±17.82%
- 6M: ₹22.80 | model=historical_median | error band=±14.97%
- 9M: ₹22.41 | model=historical_median | error band=±23.03%
- 12M: ₹26.69 | model=extra_trees | error band=±21.33%
- 18M: ₹17.44 | model=historical_median | error band=±21.47%
- 24M: ₹25.12 | model=extra_trees | error band=±13.27%
- 36M: ₹28.17 | model=hist | error band=±16.22%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1245.4000244140625
- Current P/L: ₹-1053.26
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1264.04 | model=historical_median | error band=±14.10%
- 6M: ₹1295.38 | model=historical_median | error band=±21.97%
- 9M: ₹1379.08 | model=hist | error band=±25.66%
- 12M: ₹1521.87 | model=hist | error band=±26.03%
- 18M: ₹1207.71 | model=hist | error band=±33.73%
- 24M: ₹1383.59 | model=extra_trees | error band=±33.78%
- 36M: ₹1529.63 | model=extra_trees | error band=±43.27%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 327.6000061035156
- Current P/L: ₹-1029.08
- First forecast horizon at/above purchase price: 12M

- 3M: ₹338.87 | model=historical_median | error band=±15.08%
- 6M: ₹360.48 | model=historical_median | error band=±17.62%
- 9M: ₹362.30 | model=historical_median | error band=±18.85%
- 12M: ₹386.30 | model=historical_median | error band=±19.03%
- 18M: ₹424.56 | model=historical_median | error band=±22.55%
- 24M: ₹429.51 | model=historical_median | error band=±39.79%
- 36M: ₹497.20 | model=historical_median | error band=±51.75%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 110.30999755859376
- Current P/L: ₹-4966.50
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹101.59 | model=historical_median | error band=±6.74%
- 6M: ₹93.73 | model=historical_median | error band=±5.13%
- 9M: ₹91.36 | model=extra_trees | error band=±2.21%
- 12M: ₹81.02 | model=historical_median | error band=±2.73%
- 18M: ₹67.51 | model=hist | error band=±3.89%
- 24M: ₹78.24 | model=hist | error band=±6.24%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 79.97000122070312
- Current P/L: ₹-2148.00
- First forecast horizon at/above purchase price: 18M

- 3M: ₹75.13 | model=hist | error band=±15.02%
- 6M: ₹61.68 | model=hist | error band=±33.13%
- 9M: ₹54.40 | model=hist | error band=±59.58%
- 12M: ₹88.16 | model=hist | error band=±74.04%
- 18M: ₹173.36 | model=historical_median | error band=±205.32%
- 24M: ₹669.95 | model=hist | error band=±56.60%
- 36M: ₹580.49 | model=hist | error band=±302.56%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 367.2000122070313
- Current P/L: ₹-4938.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹373.91 | model=historical_median | error band=±12.16%
- 6M: ₹380.40 | model=historical_median | error band=±10.78%
- 9M: ₹376.73 | model=historical_median | error band=±14.33%
- 12M: ₹382.60 | model=historical_median | error band=±18.83%
- 18M: ₹486.91 | model=historical_median | error band=±44.88%
- 24M: ₹624.78 | model=historical_median | error band=±76.59%
- 36M: ₹463.05 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 165.49000549316406
- Current P/L: ₹-16963.20
- First forecast horizon at/above purchase price: 36M

- 3M: ₹171.06 | model=extra_trees | error band=±9.56%
- 6M: ₹157.29 | model=extra_trees | error band=±21.50%
- 9M: ₹141.38 | model=extra_trees | error band=±27.91%
- 12M: ₹154.48 | model=extra_trees | error band=±21.79%
- 18M: ₹183.60 | model=hist | error band=±29.78%
- 24M: ₹217.19 | model=historical_median | error band=±41.29%
- 36M: ₹236.43 | model=historical_median | error band=±41.55%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.69999694824219
- Current P/L: ₹-9015.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹87.63 | model=historical_median | error band=±18.12%
- 6M: ₹70.16 | model=extra_trees | error band=±16.72%
- 9M: ₹61.36 | model=extra_trees | error band=±26.21%
- 12M: ₹59.25 | model=extra_trees | error band=±40.49%
- 18M: ₹71.97 | model=hist | error band=±38.65%
- 24M: ₹116.39 | model=historical_median | error band=±61.31%
- 36M: ₹176.06 | model=historical_median | error band=±88.20%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 37.83000183105469
- Current P/L: ₹-36519.69
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹38.94 | model=extra_trees | error band=±12.46%
- 6M: ₹26.32 | model=hist | error band=±16.43%
- 9M: ₹31.92 | model=hist | error band=±10.35%
- 12M: ₹30.78 | model=extra_trees | error band=±11.23%
- 18M: ₹20.18 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 189.42999267578125
- Current P/L: ₹-6980.62
- First forecast horizon at/above purchase price: 24M

- 3M: ₹191.00 | model=historical_median | error band=±20.10%
- 6M: ₹171.29 | model=extra_trees | error band=±20.87%
- 9M: ₹198.47 | model=historical_median | error band=±20.33%
- 12M: ₹196.45 | model=historical_median | error band=±16.82%
- 18M: ₹214.73 | model=historical_median | error band=±29.46%
- 24M: ₹332.45 | model=extra_trees | error band=±28.85%
- 36M: ₹240.55 | model=hist | error band=±26.49%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.06999969482422
- Current P/L: ₹-3186.45
- First forecast horizon at/above purchase price: 36M

- 3M: ₹61.14 | model=historical_median | error band=±17.98%
- 6M: ₹62.27 | model=historical_median | error band=±25.50%
- 9M: ₹61.99 | model=historical_median | error band=±34.89%
- 12M: ₹63.71 | model=historical_median | error band=±38.32%
- 18M: ₹70.87 | model=historical_median | error band=±69.37%
- 24M: ₹81.50 | model=historical_median | error band=±86.61%
- 36M: ₹110.66 | model=historical_median | error band=±115.14%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 20.88999938964844
- Current P/L: ₹-43020.00
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.29 | model=historical_median | error band=±32.27%
- 6M: ₹22.01 | model=extra_trees | error band=±25.23%
- 9M: ₹20.73 | model=historical_median | error band=±47.41%
- 12M: ₹21.31 | model=historical_median | error band=±59.35%
- 18M: ₹15.71 | model=extra_trees | error band=±97.85%
- 24M: ₹37.05 | model=historical_median | error band=±104.21%
- 36M: ₹47.42 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 470.2000122070313
- Current P/L: ₹-27047.40
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹420.67 | model=hist | error band=±15.04%
- 6M: ₹456.98 | model=historical_median | error band=±21.55%
- 9M: ₹464.04 | model=historical_median | error band=±32.44%
- 12M: ₹537.25 | model=historical_median | error band=±48.54%
- 18M: ₹604.25 | model=historical_median | error band=±68.41%
- 24M: ₹580.70 | model=historical_median | error band=±55.83%
- 36M: ₹362.75 | model=extra_trees | error band=±115.01%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.159999847412109
- Current P/L: ₹-6774.68
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.95 | model=historical_median | error band=±20.55%
- 6M: ₹5.19 | model=historical_median | error band=±22.15%
- 9M: ₹2.48 | model=extra_trees | error band=±48.03%
- 12M: ₹2.08 | model=extra_trees | error band=±53.68%
- 18M: ₹5.73 | model=historical_median | error band=±51.51%
- 24M: ₹6.15 | model=historical_median | error band=±59.44%
- 36M: ₹4.61 | model=historical_median | error band=±88.69%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
