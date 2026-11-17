# V6 Historical Strategy Backtest

- Version: V6
- Rows: 54
- Plan rows: 14
- No-plan rows: 16
- Trend-blocked rows: 24
- Error rows: 0
- Adaptive target exit rate: 28.6%
- Full-entry rate: 57.1%
- Partial-exit rate: 100.0%

## Exit types
- deterioration: 8 (57.1%)
- target: 4 (28.6%)
- stop_loss: 2 (14.3%)

## Horizon evidence
- 12M: plans 4, target 0.0%, mean partial -3.11%
- 3M: plans 1, target 100.0%, mean partial 48.55%
- 9M: plans 1, target 0.0%, mean partial 20.98%
- 24M: plans 4, target 0.0%, mean partial -3.03%
- 18M: plans 4, target 75.0%, mean partial 13.16%

## Partial-position outcome
- Mean: 6.97%
- Median: 2.65%
- Positive outcome rate: 64.3%
- Mean additional capital deployed: ₹14,299
- Median additional capital deployed: ₹10,530

## V6 changes
- Blocks new averaging plans when the decision-date trend is deteriorating.
- Replaces the unreachable full forecast target with an adaptive target anchored to the forecast and a 5% minimum.
- Preserves T+1 fills, partial entries, 15% stop-loss, deterioration exit and timeout.
- Historical results are evidence for research, not a guarantee of future returns.
