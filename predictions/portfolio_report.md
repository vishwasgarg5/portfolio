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
- Current price: 23.170000076293945
- Current P/L: ₹-360.80
- First forecast horizon at/above purchase price: 12M

- 3M: ₹23.18 | model=historical_median | error band=±17.82%
- 6M: ₹22.77 | model=historical_median | error band=±14.96%
- 9M: ₹22.37 | model=historical_median | error band=±19.95%
- 12M: ₹26.64 | model=extra_trees | error band=±21.94%
- 18M: ₹17.42 | model=historical_median | error band=±21.68%
- 24M: ₹25.29 | model=extra_trees | error band=±13.30%
- 36M: ₹29.91 | model=hist | error band=±16.29%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1243.9000244140625
- Current P/L: ₹-1072.76
- First forecast horizon at/above purchase price: 9M

- 3M: ₹1262.52 | model=historical_median | error band=±14.10%
- 6M: ₹1293.82 | model=historical_median | error band=±21.97%
- 9M: ₹1383.49 | model=hist | error band=±25.66%
- 12M: ₹1530.03 | model=hist | error band=±26.03%
- 18M: ₹1191.76 | model=hist | error band=±33.73%
- 24M: ₹1383.87 | model=extra_trees | error band=±33.75%
- 36M: ₹1529.52 | model=extra_trees | error band=±43.28%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 327.79998779296875
- Current P/L: ₹-1023.88
- First forecast horizon at/above purchase price: 12M

- 3M: ₹339.21 | model=historical_median | error band=±15.08%
- 6M: ₹361.08 | model=historical_median | error band=±17.62%
- 9M: ₹362.52 | model=historical_median | error band=±18.85%
- 12M: ₹386.79 | model=historical_median | error band=±19.03%
- 18M: ₹425.40 | model=historical_median | error band=±22.55%
- 24M: ₹431.87 | model=historical_median | error band=±39.92%
- 36M: ₹496.82 | model=historical_median | error band=±51.44%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 110.4000015258789
- Current P/L: ₹-4935.00
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹101.67 | model=historical_median | error band=±6.92%
- 6M: ₹93.81 | model=historical_median | error band=±5.23%
- 9M: ₹91.35 | model=extra_trees | error band=±2.20%
- 12M: ₹81.09 | model=historical_median | error band=±2.73%
- 18M: ₹67.36 | model=hist | error band=±3.78%
- 24M: ₹78.38 | model=hist | error band=±6.24%
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 80.19999694824219
- Current P/L: ₹-2102.00
- First forecast horizon at/above purchase price: 12M

- 3M: ₹74.63 | model=hist | error band=±17.38%
- 6M: ₹75.14 | model=historical_median | error band=±27.15%
- 9M: ₹48.79 | model=hist | error band=±60.10%
- 12M: ₹90.73 | model=hist | error band=±77.06%
- 18M: ₹172.22 | model=historical_median | error band=±202.30%
- 24M: ₹676.43 | model=hist | error band=±41.64%
- 36M: ₹568.35 | model=hist | error band=±339.39%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 368.8999938964844
- Current P/L: ₹-4819.50
- First forecast horizon at/above purchase price: 18M

- 3M: ₹375.64 | model=historical_median | error band=±12.16%
- 6M: ₹382.17 | model=historical_median | error band=±10.78%
- 9M: ₹378.47 | model=historical_median | error band=±14.33%
- 12M: ₹384.37 | model=historical_median | error band=±18.83%
- 18M: ₹489.16 | model=historical_median | error band=±44.88%
- 24M: ₹627.67 | model=historical_median | error band=±76.59%
- 36M: ₹447.87 | model=extra_trees | error band=±157.00%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 165.3800048828125
- Current P/L: ₹-16997.30
- First forecast horizon at/above purchase price: 36M

- 3M: ₹171.37 | model=extra_trees | error band=±9.56%
- 6M: ₹157.16 | model=extra_trees | error band=±21.50%
- 9M: ₹141.20 | model=extra_trees | error band=±27.62%
- 12M: ₹154.71 | model=extra_trees | error band=±21.79%
- 18M: ₹182.49 | model=hist | error band=±29.78%
- 24M: ₹217.05 | model=historical_median | error band=±41.29%
- 36M: ₹236.27 | model=historical_median | error band=±41.55%

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
- 9M: ₹61.05 | model=extra_trees | error band=±26.21%
- 12M: ₹58.89 | model=extra_trees | error band=±40.49%
- 18M: ₹72.78 | model=hist | error band=±38.65%
- 24M: ₹116.39 | model=historical_median | error band=±61.31%
- 36M: ₹176.06 | model=historical_median | error band=±88.23%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 38.02000045776367
- Current P/L: ₹-35979.72
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹38.81 | model=extra_trees | error band=±12.46%
- 6M: ₹26.29 | model=hist | error band=±16.43%
- 9M: ₹32.01 | model=hist | error band=±10.35%
- 12M: ₹30.89 | model=extra_trees | error band=±11.24%
- 18M: ₹20.13 | model=hist | error band=±4.57%
- 24M: N/A — Insufficient history for target_24M: 0 labelled rows < 80
- 36M: N/A — Insufficient history for target_36M: 0 labelled rows < 80

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 191.22000122070312
- Current P/L: ₹-6826.68
- First forecast horizon at/above purchase price: 24M

- 3M: ₹192.81 | model=historical_median | error band=±20.10%
- 6M: ₹171.33 | model=extra_trees | error band=±20.87%
- 9M: ₹200.34 | model=historical_median | error band=±20.33%
- 12M: ₹198.31 | model=historical_median | error band=±16.77%
- 18M: ₹216.79 | model=historical_median | error band=±29.46%
- 24M: ₹332.66 | model=extra_trees | error band=±28.45%
- 36M: ₹216.68 | model=hist | error band=±26.48%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.09999847412109
- Current P/L: ₹-3184.26
- First forecast horizon at/above purchase price: 36M

- 3M: ₹61.17 | model=historical_median | error band=±17.98%
- 6M: ₹62.30 | model=historical_median | error band=±25.69%
- 9M: ₹62.02 | model=historical_median | error band=±34.89%
- 12M: ₹63.74 | model=historical_median | error band=±38.32%
- 18M: ₹70.91 | model=historical_median | error band=±66.42%
- 24M: ₹81.48 | model=historical_median | error band=±86.61%
- 36M: ₹110.71 | model=historical_median | error band=±119.99%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 20.959999084472656
- Current P/L: ₹-42862.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹20.36 | model=historical_median | error band=±32.27%
- 6M: ₹22.00 | model=extra_trees | error band=±25.44%
- 9M: ₹19.90 | model=extra_trees | error band=±47.41%
- 12M: ₹21.32 | model=historical_median | error band=±59.34%
- 18M: ₹14.69 | model=extra_trees | error band=±97.85%
- 24M: ₹37.18 | model=historical_median | error band=±104.21%
- 36M: ₹47.49 | model=historical_median | error band=±100.21%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 473.5
- Current P/L: ₹-26846.10
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹434.79 | model=extra_trees | error band=±15.10%
- 6M: ₹460.28 | model=historical_median | error band=±21.53%
- 9M: ₹463.05 | model=historical_median | error band=±35.64%
- 12M: ₹541.02 | model=historical_median | error band=±44.53%
- 18M: ₹608.86 | model=historical_median | error band=±68.21%
- 24M: ₹584.77 | model=historical_median | error band=±47.59%
- 36M: ₹364.76 | model=extra_trees | error band=±115.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.190000057220459
- Current P/L: ₹-6745.31
- First forecast horizon at/above purchase price: Not reached in available forecast

- 3M: ₹4.93 | model=historical_median | error band=±20.53%
- 6M: ₹5.22 | model=historical_median | error band=±21.94%
- 9M: ₹2.47 | model=extra_trees | error band=±48.03%
- 12M: ₹2.14 | model=extra_trees | error band=±53.68%
- 18M: ₹5.76 | model=historical_median | error band=±51.51%
- 24M: ₹6.19 | model=historical_median | error band=±61.92%
- 36M: ₹4.63 | model=historical_median | error band=±88.09%

Dividend data: upcoming and historical analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
