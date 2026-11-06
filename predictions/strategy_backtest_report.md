# V6 Historical Strategy Backtest

- Version: V6
- Rows: 54
- Plan rows: 16
- No-plan rows: 14
- Trend-blocked rows: 24
- Error rows: 0
- Adaptive target exit rate: 25.0%
- Full-entry rate: 62.5%
- Partial-exit rate: 100.0%

## Exit types
- deterioration: 10 (62.5%)
- target: 4 (25.0%)
- stop_loss: 2 (12.5%)

## Horizon evidence
- 12M: plans 4, target 0.0%, mean partial -3.11%
- 3M: plans 1, target 100.0%, mean partial 48.55%
- 9M: plans 1, target 0.0%, mean partial 20.98%
- 24M: plans 4, target 0.0%, mean partial -3.03%
- 18M: plans 5, target 60.0%, mean partial 9.75%
- 36M: plans 1, target 0.0%, mean partial -8.04%

## Partial-position outcome
- Mean: 5.36%
- Median: 2.30%
- Positive outcome rate: 56.2%
- Mean additional capital deployed: ₹13,443
- Median additional capital deployed: ₹10,530

## V6 changes
- Blocks new averaging plans when the decision-date trend is deteriorating.
- Replaces the unreachable full forecast target with an adaptive target anchored to the forecast and a 5% minimum.
- Preserves T+1 fills, partial entries, 15% stop-loss, deterioration exit and timeout.
- Historical results are evidence for research, not a guarantee of future returns.
