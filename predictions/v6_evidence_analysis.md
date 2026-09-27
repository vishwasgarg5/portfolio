# V6 Evidence Analysis

- Plan rows: 24
- Deterioration exits: 18 (75.0%)
- Target exits: 4 (16.7%)
- Stop-loss exits: 2 (8.3%)
- Mean days to exit: 40.7
- Median days to exit: 42.0
- Mean partial outcome: 6.81%

## Deterioration timing
- Mean deterioration exit: 41.9 days
- Median deterioration exit: 42.0 days
- Exits within 20 days: 6 / 18
- Exits within 60 days: 12 / 18

## By horizon
- 12M: plans 4, target 25.0%, deterioration 75.0%, positive partial 75.0%, mean partial 3.97%
- 18M: plans 5, target 0.0%, deterioration 100.0%, positive partial 60.0%, mean partial 2.31%
- 24M: plans 6, target 33.3%, deterioration 66.7%, positive partial 66.7%, mean partial 9.70%
- 36M: plans 6, target 0.0%, deterioration 66.7%, positive partial 66.7%, mean partial -0.47%
- 6M: plans 2, target 50.0%, deterioration 50.0%, positive partial 50.0%, mean partial 23.77%
- 9M: plans 1, target 0.0%, deterioration 100.0%, positive partial 100.0%, mean partial 33.10%

## By stock
- IRFC.NS: plans 3, target 1, deterioration 2, mean partial 36.21%
- NTPC.NS: plans 2, target 1, deterioration 1, mean partial 8.19%
- PALASHSECU.NS: plans 5, target 0, deterioration 3, mean partial -1.57%
- RELIANCE.NS: plans 4, target 0, deterioration 4, mean partial 1.81%
- RPOWER.NS: plans 1, target 0, deterioration 1, mean partial -5.67%
- STARCEMENT.NS: plans 1, target 0, deterioration 1, mean partial -4.95%
- TATAPOWER.NS: plans 3, target 0, deterioration 3, mean partial -6.23%
- WIPRO.NS: plans 5, target 2, deterioration 3, mean partial 13.67%

## Interpretation
- Deterioration exits dominate V6 and are often early relative to the intended horizon.
- This supports testing a deterioration grace period rather than immediately replacing the strategy.
- The next experiment should preserve V6 as the baseline and test a V6.1 grace-period variant on the same historical origins.
- No V7 promotion should occur until V6.1 is compared directly with V6 on target rate, downside, positive-outcome rate, capital deployment and exit timing.
