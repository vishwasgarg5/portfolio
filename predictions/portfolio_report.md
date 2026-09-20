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
- 6M: ₹386.8957287521312 | model=extra_trees | error band=±0.2793900439264843
- 9M: ₹282.62244492268894 | model=zero_baseline | error band=±0.44851538661944
- 12M: ₹265.01994472841074 | model=zero_baseline | error band=±0.0636258527028815

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

- 3M: ₹1210.4896856075322 | model=zero_baseline | error band=±0.121669596514359
- 6M: ₹1205.3941726938417 | model=zero_baseline | error band=±0.1179211561684505
- 9M: ₹1203.4479194521457 | model=zero_baseline | error band=±0.124555299501091
- 12M: ₹1202.9333129034217 | model=zero_baseline | error band=±0.1267646728901323

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.6499938964844
- Current P/L: ₹-1131.78
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹319.79782621583865 | model=zero_baseline | error band=±0.1442767874579123
- 6M: ₹322.9951291894078 | model=zero_baseline | error band=±0.1468399214964297
- 9M: ₹321.2349024398807 | model=zero_baseline | error band=±0.186889444658113
- 12M: ₹318.3816957247965 | model=zero_baseline | error band=±0.1675520343245297

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

- 3M: ₹77.64129141081412 | model=zero_baseline | error band=±0.1269516058225899
- 6M: ₹74.47826910990246 | model=zero_baseline | error band=±0.2388925272602478
- 9M: ₹73.00608564383838 | model=zero_baseline | error band=±0.2854304614196425
- 12M: ₹72.15899169906177 | model=zero_baseline | error band=±0.3053465867015039

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 374.7999877929688
- Current P/L: ₹-4406.50
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹372.1474792502408 | model=zero_baseline | error band=±0.1206691391171583
- 6M: ₹370.1118257243032 | model=zero_baseline | error band=±0.2119905861467288
- 9M: ₹368.00474247921375 | model=zero_baseline | error band=±0.1430471832611151
- 12M: ₹363.3456931257477 | model=zero_baseline | error band=±0.120063595416391

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 166.8300018310547
- Current P/L: ₹-16547.80
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹165.2944134866297 | model=zero_baseline | error band=±0.1218457990848099
- 6M: ₹163.77740726068538 | model=zero_baseline | error band=±0.2111260930044564
- 9M: ₹162.4890848699956 | model=zero_baseline | error band=±0.2294251082867883
- 12M: ₹130.890117440377 | model=hist | error band=±0.3342311730483648

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

- 3M: ₹198.17925389485453 | model=zero_baseline | error band=±0.1630591210735261
- 6M: ₹191.62885611615528 | model=zero_baseline | error band=±0.1613105595863367
- 9M: ₹193.2690245878141 | model=zero_baseline | error band=±0.2651487870874482
- 12M: ₹191.377842530296 | model=zero_baseline | error band=±0.1772067816339376

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.95000076293945
- Current P/L: ₹-3122.21
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹61.501359579915786 | model=zero_baseline | error band=±0.1368944830333346
- 6M: ₹60.18324041332392 | model=zero_baseline | error band=±0.2448438053935798
- 9M: ₹57.820211091256354 | model=zero_baseline | error band=±0.2465687914167373
- 12M: ₹55.543518240232224 | model=zero_baseline | error band=±0.3233604007301392

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

- 3M: ₹449.6670567991425 | model=zero_baseline | error band=±0.1404823883263311
- 6M: ₹446.2698207016832 | model=zero_baseline | error band=±0.1953178049040285
- 9M: ₹430.0877806897431 | model=zero_baseline | error band=±0.301621381745977
- 12M: ₹432.6615394623378 | model=zero_baseline | error band=±0.2579002787327289

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.230000019073486
- Current P/L: ₹-6706.15
- First forecast horizon at/above purchase price: Not reached in 12M forecast

- 3M: ₹4.866980285262271 | model=zero_baseline | error band=±0.1737629375929208
- 6M: ₹4.450766149188372 | model=zero_baseline | error band=±0.406091510033354
- 9M: ₹4.445500016212463 | model=zero_baseline | error band=±0.4865911098075763
- 12M: ₹4.445500016212463 | model=zero_baseline | error band=±0.5590578443477995

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
