# Portfolio forecast report

Models retrain from the latest market history on every scheduled run.
The selected model is chosen using chronological holdout error, with a zero-return baseline included.
Forecast calibration prefers completed real forecast errors for the same stock/horizon, then falls back to walk-forward errors.
Error bands are empirical historical-error bands, not guarantees.
The first forecast horizon is a model checkpoint, not a guaranteed date.
Averaging scenarios are mathematical cost-basis calculations, not buy recommendations.

## Vedanta Iron & Steel (VISL.NS)
- Quantity: 1000.0
- Purchase price: 31.84
- Current price: 30.90999984741211
- Current P/L: ₹-930.00
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹nan | model=nan | error band=±nan
- 6M: ₹nan | model=nan | error band=±nan
- 9M: ₹nan | model=nan | error band=±nan
- 12M: ₹nan | model=nan | error band=±nan
- 18M: ₹nan | model=nan | error band=±nan
- 24M: ₹nan | model=nan | error band=±nan
- 36M: ₹nan | model=nan | error band=±nan

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Yes Bank (YESBANK.NS)
- Quantity: 902.0
- Purchase price: 23.57
- Current price: 22.71999931335449
- Current P/L: ₹-766.70
- First forecast horizon at/above purchase price: 36M

- 3M: ₹22.32611086846308 | model=zero_baseline | error band=±0.1026092398380728
- 6M: ₹23.17838413526697 | model=zero_baseline | error band=±0.1773311961471479
- 9M: ₹22.58832667211862 | model=zero_baseline | error band=±0.1669891517783204
- 12M: ₹23.141844525051347 | model=zero_baseline | error band=±0.1772912219020566
- 18M: ₹22.113317594651072 | model=zero_baseline | error band=±0.3055919808400337
- 24M: ₹22.39642540049887 | model=zero_baseline | error band=±0.2503538028128859
- 36M: ₹31.599007063994907 | model=extra_trees | error band=±0.0918745824109585

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Industries (RELIANCE.NS)
- Quantity: 13.0
- Purchase price: 1326.42
- Current price: 1226.4000244140625
- Current P/L: ₹-1300.26
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹1210.4896856075322 | model=zero_baseline | error band=±0.121669596514359
- 6M: ₹1205.6027656563317 | model=zero_baseline | error band=±0.1179211561684505
- 9M: ₹1203.592731487319 | model=zero_baseline | error band=±0.124555299501091
- 12M: ₹1202.933315819671 | model=zero_baseline | error band=±0.1267646728901323
- 18M: ₹1216.5940269484745 | model=zero_baseline | error band=±0.0624057849349136
- 24M: ₹1204.122759471354 | model=zero_baseline | error band=±0.1739137036372688
- 36M: ₹1280.4378341909378 | model=zero_baseline | error band=±0.1734733288746071

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## NTPC (NTPC.NS)
- Quantity: 26.0
- Purchase price: 367.18
- Current price: 323.6499938964844
- Current P/L: ₹-1131.78
- First forecast horizon at/above purchase price: 36M

- 3M: ₹319.88923759546105 | model=zero_baseline | error band=±0.1436309825529629
- 6M: ₹322.9951219278023 | model=zero_baseline | error band=±0.1471082512848218
- 9M: ₹321.1125673667687 | model=zero_baseline | error band=±0.1870563456994458
- 12M: ₹318.2877323959227 | model=zero_baseline | error band=±0.1677743728630877
- 18M: ₹317.0254917747915 | model=zero_baseline | error band=±0.1898587239818055
- 24M: ₹315.85334020137003 | model=zero_baseline | error band=±0.1394621350379563
- 36M: ₹639.6978487639382 | model=extra_trees | error band=±0.2588191728956684

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Indian Renewable Energy (IREDA.NS)
- Quantity: 350.0
- Purchase price: 124.5
- Current price: 114.31999969482422
- Current P/L: ₹-3563.00
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹111.80697559766944 | model=zero_baseline | error band=±0.0907094693700932
- 6M: ₹98.6474613413096 | model=extra_trees | error band=±0.0499416567100465
- 9M: ₹92.56509148023582 | model=extra_trees | error band=±0.0285750291238361
- 12M: ₹82.66890601681844 | model=extra_trees | error band=±0.0244891563732667
- 18M: ₹67.25784703345413 | model=hist | error band=±0.0387046141153177
- 24M: ₹83.07009511688449 | model=hist | error band=±0.0664171464712268
- 36M: ₹nan | model=nan | error band=±nan

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRFC (IRFC.NS)
- Quantity: 200.0
- Purchase price: 90.71
- Current price: 81.5
- Current P/L: ₹-1842.00
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹77.64129141081412 | model=zero_baseline | error band=±0.1269516058225899
- 6M: ₹74.47826910990246 | model=zero_baseline | error band=±0.2388925272602478
- 9M: ₹73.00608564383838 | model=zero_baseline | error band=±0.2854304614196425
- 12M: ₹72.08241477533595 | model=zero_baseline | error band=±0.3053465867015039
- 18M: ₹69.27499999999999 | model=zero_baseline | error band=±0.4031389702162537
- 24M: ₹73.04741779573351 | model=zero_baseline | error band=±0.4047938770178884
- 36M: ₹82.16509960829883 | model=zero_baseline | error band=±1.7141229325811291

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Tata Power (TATAPOWER.NS)
- Quantity: 70.0
- Purchase price: 437.75
- Current price: 374.7999877929688
- Current P/L: ₹-4406.50
- First forecast horizon at/above purchase price: 36M

- 3M: ₹372.1474792502408 | model=zero_baseline | error band=±0.1206691391171583
- 6M: ₹370.3196014507105 | model=zero_baseline | error band=±0.2095998598519424
- 9M: ₹368.00474247921375 | model=zero_baseline | error band=±0.1430471594319639
- 12M: ₹363.9232026382201 | model=zero_baseline | error band=±0.120063595416391
- 18M: ₹369.3314170070304 | model=zero_baseline | error band=±0.1581891425874584
- 24M: ₹431.0199859619141 | model=zero_baseline | error band=±0.8700925645030617
- 36M: ₹824.1453635840013 | model=extra_trees | error band=±0.9829248350042032

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Wipro (WIPRO.NS)
- Quantity: 310.0
- Purchase price: 220.21
- Current price: 166.8300018310547
- Current P/L: ₹-16547.80
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹165.29436625242897 | model=zero_baseline | error band=±0.1218457990848099
- 6M: ₹163.77740475359175 | model=zero_baseline | error band=±0.2111260546065209
- 9M: ₹162.4890848699956 | model=zero_baseline | error band=±0.2294251082867883
- 12M: ₹130.9677749418297 | model=hist | error band=±0.3342311451989333
- 18M: ₹195.46386842806717 | model=extra_trees | error band=±0.3585218602276186
- 24M: ₹174.41191303606504 | model=zero_baseline | error band=±0.3693482625254503
- 36M: ₹164.15527247241155 | model=zero_baseline | error band=±0.1919529319518747

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Palash Securities (PALASHSECU.NS)
- Quantity: 300.0
- Purchase price: 116.75
- Current price: 86.11000061035156
- Current P/L: ₹-9192.00
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹84.26214311556551 | model=zero_baseline | error band=±0.1543476746494886
- 6M: ₹81.97674871673212 | model=zero_baseline | error band=±0.1396703784988164
- 9M: ₹79.13112058736395 | model=zero_baseline | error band=±0.2688824818249044
- 12M: ₹77.70874306623607 | model=zero_baseline | error band=±0.2492963640382119
- 18M: ₹85.9227125334834 | model=zero_baseline | error band=±0.4229715288488708
- 24M: ₹87.91712039777039 | model=zero_baseline | error band=±0.3246016118950754
- 36M: ₹84.14786119366823 | model=zero_baseline | error band=±0.279215596880218

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Ola Electric Mobility (OLAELEC.NS)
- Quantity: 2842.0
- Purchase price: 50.68
- Current price: 36.38999938964844
- Current P/L: ₹-40612.18
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹36.915799331568685 | model=zero_baseline | error band=±0.3651626321694365
- 6M: ₹36.76362602347633 | model=zero_baseline | error band=±0.2198056886542646
- 9M: ₹31.52427719816447 | model=hist | error band=±0.1519661978460541
- 12M: ₹35.066315274844506 | model=zero_baseline | error band=±0.1488179615907147
- 18M: ₹20.42697249011409 | model=hist | error band=±0.0422251328640204
- 24M: ₹nan | model=nan | error band=±nan
- 36M: ₹nan | model=nan | error band=±nan

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Star Cement (STARCEMENT.NS)
- Quantity: 86.0
- Purchase price: 270.6
- Current price: 194.25
- Current P/L: ₹-6566.10
- First forecast horizon at/above purchase price: 36M

- 3M: ₹198.17925389485453 | model=zero_baseline | error band=±0.1630591210735261
- 6M: ₹191.62885611615528 | model=zero_baseline | error band=±0.1612550396703453
- 9M: ₹193.31449795307668 | model=zero_baseline | error band=±0.2651487870874482
- 12M: ₹191.377842530296 | model=zero_baseline | error band=±0.1772067816339376
- 18M: ₹188.628496298904 | model=zero_baseline | error band=±0.144816714503543
- 24M: ₹193.2048418071556 | model=zero_baseline | error band=±0.2931173531933522
- 36M: ₹339.4363933170742 | model=hist | error band=±0.1854318511118305

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SJVN (SJVN.NS)
- Quantity: 73.0
- Purchase price: 106.72
- Current price: 63.95000076293945
- Current P/L: ₹-3122.21
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹61.501358457042485 | model=zero_baseline | error band=±0.136894384354561
- 6M: ₹59.89331439541779 | model=zero_baseline | error band=±0.2448438053935798
- 9M: ₹57.36916819805054 | model=zero_baseline | error band=±0.26095962628416
- 12M: ₹55.54351828765541 | model=zero_baseline | error band=±0.3233603436888575
- 18M: ₹57.14817172610819 | model=zero_baseline | error band=±0.433717007625958
- 24M: ₹59.666621863650576 | model=zero_baseline | error band=±0.4729365759938901
- 36M: ₹60.47440538256716 | model=zero_baseline | error band=±0.7064671117209592

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## Reliance Power (RPOWER.NS)
- Quantity: 2250.0
- Purchase price: 40.01
- Current price: 21.1299991607666
- Current P/L: ₹-42480.00
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹19.777690757589024 | model=zero_baseline | error band=±0.2023789826414095
- 6M: ₹19.53015309292357 | model=zero_baseline | error band=±0.3702286900873363
- 9M: ₹17.97975171931189 | model=zero_baseline | error band=±0.5253313190996973
- 12M: ₹18.49890459759304 | model=zero_baseline | error band=±0.5981551823093351
- 18M: ₹19.99426887695324 | model=zero_baseline | error band=±0.7697307606483321
- 24M: ₹19.838557263444883 | model=zero_baseline | error band=±0.8046874801013362
- 36M: ₹24.29949903488159 | model=zero_baseline | error band=±1.776504041812016

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## IRCTC (IRCTC.NS)
- Quantity: 61.0
- Purchase price: 913.6
- Current price: 476.75
- Current P/L: ₹-26647.85
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹449.6670648784663 | model=zero_baseline | error band=±0.1404823883263311
- 6M: ₹446.2698207016832 | model=zero_baseline | error band=±0.1953178049040285
- 9M: ₹430.0877952212421 | model=zero_baseline | error band=±0.301621381745977
- 12M: ₹432.6615394623378 | model=zero_baseline | error band=±0.2579002410420697
- 18M: ₹417.04847795750914 | model=zero_baseline | error band=±0.3658601138022184
- 24M: ₹508.6023914565709 | model=zero_baseline | error band=±0.3981280318178282
- 36M: ₹466.0796204838345 | model=zero_baseline | error band=±0.1947131108825131

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv

## SEPC (SEPC.NS)
- Quantity: 979.0
- Purchase price: 12.08
- Current price: 5.230000019073486
- Current P/L: ₹-6706.15
- First forecast horizon at/above purchase price: Not reached in 36M forecast

- 3M: ₹4.866980285262271 | model=zero_baseline | error band=±0.1737831182313016
- 6M: ₹4.450766149188372 | model=zero_baseline | error band=±0.406091510033354
- 9M: ₹4.445500016212463 | model=zero_baseline | error band=±0.4865911098075763
- 12M: ₹4.445500016212463 | model=zero_baseline | error band=±0.558497770241943
- 18M: ₹4.445500016212463 | model=zero_baseline | error band=±0.6625710144922514
- 24M: ₹4.445500016212463 | model=zero_baseline | error band=±0.6438905266553971
- 36M: ₹4.454988633881189 | model=zero_baseline | error band=±0.7025396048603215

Dividend data: upcoming ex-date/cum-date and historical ex-day/recovery analysis are in the report CSV.
Averaging scenarios: see predictions/averaging_scenarios.csv
