# V6 Historical Strategy Backtest

- Version: V6
- Rows: 54
- Plan rows: 15
- No-plan rows: 15
- Trend-blocked rows: 24
- Error rows: 0
- Adaptive target exit rate: 26.7%
- Full-entry rate: 60.0%
- Partial-exit rate: 100.0%

## Exit types
- deterioration: 9 (60.0%)
- target: 4 (26.7%)
- stop_loss: 2 (13.3%)

## Horizon evidence
- 12M: plans 4, target 0.0%, mean partial -3.11%
- 3M: plans 1, target 100.0%, mean partial 48.55%
- 9M: plans 1, target 0.0%, mean partial 20.98%
- 24M: plans 4, target 0.0%, mean partial -3.03%
- 18M: plans 5, target 60.0%, mean partial 9.75%

## Partial-position outcome
- Mean: 6.25%
- Median: 2.56%
- Positive outcome rate: 60.0%
- Mean additional capital deployed: ₹14,083
- Median additional capital deployed: ₹10,741

## V6 changes
- Blocks new averaging plans when the decision-date trend is deteriorating.
- Replaces the unreachable full forecast target with an adaptive target anchored to the forecast and a 5% minimum.
- Preserves T+1 fills, partial entries, 15% stop-loss, deterioration exit and timeout.
- Historical results are evidence for research, not a guarantee of future returns.
