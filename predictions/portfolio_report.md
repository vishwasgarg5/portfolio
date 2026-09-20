# Portfolio forecast report

Models retrain from the latest market history on every scheduled run.
The selected model is chosen using chronological holdout error, with a zero-return baseline included.
Forecast calibration prefers completed real forecast errors for the same stock/horizon, then falls back to walk-forward errors.
Error bands are empirical historical-error bands, not guarantees.
The first forecast horizon is a model checkpoint, not a guaranteed date.
Averaging scenarios are mathematical cost-basis calculations, not buy recommendations.

## Vedanta (VEDL.NS)
- Quantity: 1000.0
- Purchase price: 31.84
- Current price: 267.6000061035156
- Current P/L: ₹235760.01
- First forecast horizon at/above purchase price: 3M

- 3M: ₹276.8058954502872 | model=zero_baseline | error band=±0.2595302176627327
- 6M: ₹385.7530119422864 | model=extra_trees | error band=±0.279389918322958
- 9M: ₹282.85367444577633 | model=zero_baseline | error band=±0.44851538661944
- 12M: ₹265.14016039231774 | model=zero_baseline | error band=±0.0665209321538449

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Yes Bank (YESBANK.NS)
- Quantity: 902.0
- Purchase price: 23.57
- Current price: 22.71999931335449
- Current P/L: ₹-766.70
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹22.32611086846308 | model=zero_baseline | error band=±0.1026092398380728
- 6M: ₹23.17838413526697 | model=zero_baseline | error band=±0.1773311961471479
- 9M: ₹22.58832667211862 | model=zero_baseline | error band=±0.1669891517783204
- 12M: ₹23.141844525051347 | model=zero_baseline | error band=±0.1772912219020566

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1226.4000244140625
- Current P/L: ₹-1300.26
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹1210.489711410854 | model=zero_baseline | error band=±0.121669596514359
- 6M: ₹1205.560588565795 | model=zero_baseline | error band=±0.1179211561684505
- 9M: ₹1203.2837258862758 | model=zero_baseline | error band=±0.124555299501091
- 12M: ₹1202.6076088441089 | model=zero_baseline | error band=±0.1267646728901323

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.6499938964844
- Current P/L: ₹-1131.78
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹319.765296976007 | model=zero_baseline | error band=±0.1440316655060467
- 6M: ₹322.9951291894078 | model=zero_baseline | error band=±0.1469221102711968
- 9M: ₹321.08941084898606 | model=zero_baseline | error band=±0.1865886739666216
- 12M: ₹318.2866403799079 | model=zero_baseline | error band=±0.1679153939661098

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 114.31999969482422
- Current P/L: ₹-3563.00
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹111.80697559766944 | model=zero_baseline | error band=±0.0907094693700932
- 6M: ₹98.6474613413096 | model=extra_trees | error band=±0.0499416567100465
- 9M: ₹92.56509148023582 | model=extra_trees | error band=±0.0285750291238361
- 12M: ₹82.66890601681844 | model=extra_trees | error band=±0.0244891563732667

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 81.5
- Current P/L: ₹-1842.00
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹77.64129141081412 | model=zero_baseline | error band=±0.126951616831218
- 6M: ₹74.47826910990246 | model=zero_baseline | error band=±0.2388925272602478
- 9M: ₹73.00608564383838 | model=zero_baseline | error band=±0.2854304973898272
- 12M: ₹72.26365470293021 | model=zero_baseline | error band=±0.3053465867015039

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 374.7999877929688
- Current P/L: ₹-4406.50
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹372.1474721662168 | model=zero_baseline | error band=±0.1206691391171583
- 6M: ₹370.3195928657527 | model=zero_baseline | error band=±0.2095998672702385
- 9M: ₹368.0047355360284 | model=zero_baseline | error band=±0.1430471842801336
- 12M: ₹362.4735458981036 | model=zero_baseline | error band=±0.120063595416391

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 166.8300018310547
- Current P/L: ₹-16547.80
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹165.3011278589485 | model=zero_baseline | error band=±0.1218457990848099
- 6M: ₹163.77740475359175 | model=zero_baseline | error band=±0.2111260546065209
- 9M: ₹162.4890848699956 | model=zero_baseline | error band=±0.2294251082867883
- 12M: ₹131.80282492731027 | model=hist | error band=±0.3342311527270394

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.11000061035156
- Current P/L: ₹-9192.00
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹84.26214311556551 | model=zero_baseline | error band=±0.1543476746494886
- 6M: ₹81.97674871673212 | model=zero_baseline | error band=±0.1396703784988164
- 9M: ₹79.13112058736395 | model=zero_baseline | error band=±0.2688824818249044
- 12M: ₹77.70874306623607 | model=zero_baseline | error band=±0.2492963640382119

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.38999938964844
- Current P/L: ₹-40612.18
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹36.915799331568685 | model=zero_baseline | error band=±0.3651626321694365
- 6M: ₹36.76362602347633 | model=zero_baseline | error band=±0.2198056886542646
- 9M: ₹31.52427719816447 | model=hist | error band=±0.1519661978460541
- 12M: ₹35.066315274844506 | model=zero_baseline | error band=±0.1488179615907147

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 194.25
- Current P/L: ₹-6566.10
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹198.17925772639924 | model=zero_baseline | error band=±0.1630591210735261
- 6M: ₹191.6288526439038 | model=zero_baseline | error band=±0.1611072315965186
- 9M: ₹193.40908612087975 | model=zero_baseline | error band=±0.2651487870874482
- 12M: ₹191.377842530296 | model=zero_baseline | error band=±0.1769888140833325

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.95000076293945
- Current P/L: ₹-3122.21
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹61.501358457042485 | model=zero_baseline | error band=±0.136894384354561
- 6M: ₹60.096463494542434 | model=zero_baseline | error band=±0.2448438053935798
- 9M: ₹57.36916819805054 | model=zero_baseline | error band=±0.2587218823018374
- 12M: ₹55.543518729290405 | model=zero_baseline | error band=±0.3233604007301392

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.1299991607666
- Current P/L: ₹-42480.00
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹19.777690757589024 | model=zero_baseline | error band=±0.2023789826414095
- 6M: ₹19.53015309292357 | model=zero_baseline | error band=±0.3702286900873363
- 9M: ₹17.97975171931189 | model=zero_baseline | error band=±0.5253313190996973
- 12M: ₹18.49890459759304 | model=zero_baseline | error band=±0.5981551823093351

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 476.75
- Current P/L: ₹-26647.85
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹449.6670734096313 | model=zero_baseline | error band=±0.1404823883263311
- 6M: ₹446.2698207016832 | model=zero_baseline | error band=±0.1953178049040285
- 9M: ₹430.087787022773 | model=zero_baseline | error band=±0.301621381745977
- 12M: ₹432.6615323074935 | model=zero_baseline | error band=±0.2579002410420697

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.230000019073486
- Current P/L: ₹-6706.15
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹4.866980285262271 | model=zero_baseline | error band=±0.1737479010600275
- 6M: ₹4.450766149188372 | model=zero_baseline | error band=±0.406091510033354
- 9M: ₹4.445500016212463 | model=zero_baseline | error band=±0.4865911098075764
- 12M: ₹4.445500016212463 | model=zero_baseline | error band=±0.5591598937141424

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
