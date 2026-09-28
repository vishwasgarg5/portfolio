# V6.3 Recovery-vs-Failure Feature Analysis

- V6 deterioration exits analysed: 18
- Features use only information available on the deterioration-exit date.
- No future recovery information is used to construct the exit-date features.

## Recovery definition
- Primary: price reaches at least +5% above the V6 exit price within the next 60 trading sessions.
- Secondary: same test within 120 trading sessions.

## Outcome counts
- 60-session: {'recovered_5pct': 12, 'not_recovered_5pct': 6}
- 120-session: {'recovered_5pct': 13, 'not_recovered_5pct': 5}

## ma20_gap_pct by 60-session outcome
                    count      mean    median
outcome_60d                                  
not_recovered_5pct      6 -0.027217 -0.019094
recovered_5pct         12 -0.042996 -0.037460

## ma50_gap_pct by 60-session outcome
                    count      mean    median
outcome_60d                                  
not_recovered_5pct      6 -0.040367 -0.032849
recovered_5pct         12 -0.053073 -0.047746

## ma20_slope_5d_pct by 60-session outcome
                    count      mean    median
outcome_60d                                  
not_recovered_5pct      6 -0.014349 -0.013053
recovered_5pct         12 -0.014036 -0.013328

## below_prior10_low by 60-session outcome
                    count      mean  median
outcome_60d                                
not_recovered_5pct      6  0.333333     0.0
recovered_5pct         12  0.250000     0.0

## below_prior20_low by 60-session outcome
                    count      mean  median
outcome_60d                                
not_recovered_5pct      6  0.166667     0.0
recovered_5pct         12  0.250000     0.0

## entries_reached by 60-session outcome
                    count  mean  median
outcome_60d                            
not_recovered_5pct      6  2.00     2.0
recovered_5pct         12  1.75     2.0

## partial_profit_percent by 60-session outcome
                    count      mean    median
outcome_60d                                  
not_recovered_5pct      6  0.012068  0.009847
recovered_5pct         12  0.056977  0.029311

## Candidate rule coverage
- Below prior 10-day low: 27.8%
- Below prior 20-day low: 22.2%
- Negative 5-day MA20 slope: 83.3%

## Interpretation
- This is feature discovery, not a strategy promotion test.
- Any V6.3 rule must be fixed from this analysis and then tested on the same historical origins without using future outcomes.
- No V7 promotion should occur from this analysis alone.
