# V6 Matched Hold-Only Benchmark

- Matched V6 plan exits: 24
- Hold-only entry uses the market close on the V6 plan date.
- Hold-only exit uses the market close on the same V6 strategy exit date.
- V6 return is the persisted V6 partial-position outcome.
- This is a matched counterfactual for evaluation; it does not use future information to construct the V6 decision.

## Overall
- V6 positive outcome rate: 66.7%
- Hold-only positive outcome rate: 20.8%
- V6 mean return: 6.81%
- Hold-only mean return: -2.27%
- V6 median return: 3.96%
- Hold-only median return: -2.56%
- Mean V6 return minus hold-only return: 9.08%
- Mean incremental profit versus hold-only: ₹3,931

## Horizon comparison
| Horizon | N | V6 mean | Hold mean | Mean delta | V6 positive | Hold positive |
|---|---:|---:|---:|---:|---:|---:|
| 12M | 4 | 3.97% | -0.05% | 4.02% | 75.0% | 25.0% |
| 18M | 5 | 2.31% | -5.78% | 8.08% | 60.0% | 0.0% |
| 24M | 6 | 9.70% | 2.73% | 6.98% | 66.7% | 50.0% |
| 36M | 6 | -0.47% | -4.76% | 4.29% | 66.7% | 16.7% |
| 6M | 2 | 23.77% | -5.99% | 29.76% | 50.0% | 0.0% |
| 9M | 1 | 33.10% | -1.19% | 34.30% | 100.0% | 0.0% |

## Interpretation guardrail
- This benchmark uses the V6 exit date to evaluate the counterfactual, so it is not a live trading rule.
- It does not prove that V6 is superior; it quantifies what the existing position would have returned over the same realized exit window.
- A future promotion decision should also consider drawdown, capital deployment and a separate out-of-sample control.
