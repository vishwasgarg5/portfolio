# V6 Historical Strategy Backtest

- Version: V6
- Rows: 106
- Plan rows: 24
- No-plan rows: 30
- Trend-blocked rows: 52
- Error rows: 0
- Adaptive target exit rate: 16.7%
- Full-entry rate: 66.7%
- Partial-exit rate: 100.0%

## Exit types
- deterioration: 18 (75.0%)
- target: 4 (16.7%)
- stop_loss: 2 (8.3%)

## Horizon evidence
- 12M: plans 4, target 25.0%, mean partial 3.97%
- 18M: plans 5, target 0.0%, mean partial 2.31%
- 36M: plans 6, target 0.0%, mean partial -0.47%
- 6M: plans 2, target 50.0%, mean partial 23.77%
- 9M: plans 1, target 0.0%, mean partial 33.10%
- 24M: plans 6, target 33.3%, mean partial 9.70%

## Partial-position outcome
- Mean: 6.81%
- Median: 3.96%
- Positive outcome rate: 66.7%
- Mean additional capital deployed: ₹14,508
- Median additional capital deployed: ₹10,157

## V6 changes
- Blocks new averaging plans when the decision-date trend is deteriorating.
- Replaces the unreachable full forecast target with an adaptive target anchored to the forecast and a 5% minimum.
- Preserves T+1 fills, partial entries, 15% stop-loss, deterioration exit and timeout.
- Historical results are evidence for research, not a guarantee of future returns.
