# Monte Carlo Modeling — Week 3 Assignment Scope

## Weekly Topic

**Correlation, portfolio behavior, and cumulative reliability risk**

## Required Assignments

1. Finance: Correlated two-asset portfolio simulation
2. Municipal engineering: Water-storage reliability simulation

## Optional Companion Assignments

3. Finance: Monthly rebalancing versus buy-and-hold
4. Municipal engineering: Daily versus cumulative failure probability

## Expected Time

| Assignment | Expected time | Priority |
|---|---:|---|
| Correlated two-asset portfolio | 75–90 minutes | Required |
| Water-storage reliability | 75–90 minutes | Required |
| Rebalancing vs. buy-and-hold | 25–35 minutes | Optional |
| Daily vs. cumulative risk | 25–35 minutes | Optional |

## Recommended Files

```text
week_03/
├── data/
├── excel/
├── outputs/
├── finance_portfolio_risk.ipynb
├── engineering_storage_reliability.ipynb
└── week_03_reflection.md
```

Use one notebook for each required assignment.

---

# Assignment 1 — Correlated Two-Asset Portfolio

## Scenario

A business owner is considering investing $100,000 in a portfolio containing:

- 60% U.S. stock-market ETF; and
- 40% U.S. bond-market ETF.

Use `SPY` and `BND` as the default tickers. Use approximately ten complete years of monthly adjusted-price data or the synthetic fallback from the full Week 3 drill package.

## Decision Questions

Determine:

- the simulated range of one-year ending values;
- the probability of finishing below $100,000;
- the probability of losing more than 10%;
- the effect of preserving stock–bond correlation; and
- the downside risk created by breaking the observed asset pairing.

## Excel Workbook

Create:

```text
excel/two_asset_portfolio_risk.xlsx
```

Required worksheets:

- `Raw_Prices`
- `Clean_Prices`
- `Monthly_Returns`
- `Assumptions`
- `Baseline`
- `Simulation_Summary`
- `Dashboard`

## Source Data

Use either:

1. Yahoo Finance monthly adjusted prices for `SPY` and `BND`; or
2. the synthetic two-asset price generator from the complete Week 3 package.

Preserve the untouched raw-data snapshot.

## Data-Cleaning Tasks

- Standardize and sort dates.
- Remove duplicate dates using a documented rule.
- Convert adjusted-price fields to numeric.
- Identify incomplete months.
- Address missing adjusted prices.
- Align the two assets to common observation dates.
- Calculate monthly simple returns.
- Create a cleaning or exception log.

Use:

```text
Monthly return_t = Adjusted price_t / Adjusted price_(t−1) − 1
```

## Deterministic Baseline

Calculate in Excel:

- arithmetic mean monthly return for each asset;
- monthly standard deviation for each asset;
- covariance between asset returns;
- correlation between asset returns;
- expected monthly portfolio return;
- portfolio monthly variance and standard deviation; and
- deterministic one-year ending value.

Use:

```text
Expected portfolio return
    = 0.60 × mean stock return
    + 0.40 × mean bond return
```

```text
Portfolio variance
    = w_stock²σ_stock²
    + w_bond²σ_bond²
    + 2w_stock w_bond Cov(stock, bond)
```

```text
Deterministic ending value
    = $100,000 × (1 + expected monthly portfolio return)^12
```

## Monte Carlo Model A — Preserve Historical Pairing

- Bootstrap complete monthly-return rows.
- When a stock return is selected, use the bond return from the same historical month.
- Preserve the observed relationship between the assets.

## Monte Carlo Model B — Break Historical Pairing

- Sample stock returns independently from the stock-return series.
- Sample bond returns independently from the bond-return series.
- Preserve each individual return distribution while removing observed dependence.

## Portfolio Rule

Assume monthly rebalancing to 60% stocks and 40% bonds:

```text
Monthly portfolio return
    = 0.60 × stock return + 0.40 × bond return

Ending value
    = $100,000 × product(1 + monthly portfolio returns)
```

## Simulation Requirements

- Use Python.
- Use `numpy.random.default_rng(20260926)`.
- Run 20,000 trials.
- Simulate 12 months per trial.
- Retain ending value and drawdown results for each trial.
- Export trial-level and summary results to Excel.

## Required Results

For Models A and B, calculate:

- mean ending value;
- median ending value;
- P10, P25, P50, P75, and P90 ending value;
- probability of finishing below $100,000;
- probability of losing more than 10%;
- mean maximum drawdown; and
- P90 maximum drawdown.

## Dashboard Requirements

- Starting investment
- Portfolio weights
- Historical stock–bond correlation
- Deterministic ending value
- Model A P10, P50, and P90 ending value
- Probability of loss
- Probability of losing more than 10%
- Ending-value histogram
- Model A versus Model B comparison
- Short investment-risk interpretation

## Validation Checks

- Confirm weights total 100%.
- Confirm prices are ordered chronologically before return calculation.
- Confirm the first price observation has no calculated return.
- Hand-calculate one monthly portfolio return.
- Confirm Model A uses identical row indices for both assets.
- Confirm Model B samples the two assets independently.
- Force monthly returns to their historical means and verify the deterministic result.
- Compare results at 5,000 and 20,000 trials.
- Investigate implausible ending values or drawdowns.

## Interpretation Questions

1. Why must covariance be included in portfolio volatility?
2. Which model better reflects the observed asset relationship?
3. Did breaking historical pairing materially change downside risk?
4. Why is P10 not a guaranteed minimum ending value?
5. What market behavior is missing from the bootstrap model?

## Deliverables

- Raw and clean price data
- Monthly-return table
- Cleaning or exception log
- Excel deterministic baseline
- Python simulation notebook
- Trial-level outputs for Models A and B
- Summary comparison table
- Excel dashboard
- Short risk interpretation

---

# Assignment 2 — Water-Storage Reliability

## Scenario

A municipal water system operates a ground-storage tank with:

- 1.50 MG of usable operating storage;
- 1.20 MG beginning storage; and
- 0.30 MG minimum operating-storage criterion.

Daily demand and supply vary. Reduced pump capacity and outages can occur.

## Decision Questions

Determine:

- the probability that storage falls below 0.30 MG during a 30-day period;
- the expected number of violation days;
- the distribution of minimum storage;
- the likely timing of the first violation; and
- the primary reliability driver.

## Source Data

Use the synthetic 90-day operating-data generator from the complete Week 3 package.

Required fields:

- date;
- daily demand in MG;
- daily supply in MG;
- maximum temperature; and
- pump status.

The dirty source data should include:

- a missing demand value;
- a supply value stored with units as text;
- an impossible negative demand;
- a duplicated date;
- unsorted records; and
- reduced-capacity operating days.

Save as:

```text
data/water_storage_operations_dirty.csv
```

## Data-Cleaning Tasks

- Parse and sort dates.
- Identify and resolve the duplicated date.
- Convert the supply value containing `MG` to numeric.
- Flag the negative demand as invalid.
- Document treatment of the missing demand observation.
- Standardize pump-status categories.
- Confirm all flow volumes use MG/day.
- Create a cleaning or exception log.

## Deterministic Baseline

Use average cleaned daily demand and average cleaned daily supply.

Start with 1.20 MG and calculate 30 days using:

```text
Ending storage_t
    = min(1.50, Beginning storage_t + Supply_t − Demand_t)

Beginning storage_(t+1)
    = Ending storage_t
```

Report:

- average daily demand;
- average daily supply;
- minimum storage;
- ending storage after 30 days; and
- whether the deterministic model violates 0.30 MG.

## Historical Operating Sampling

- Sample complete historical rows of demand, supply, and temperature.
- Preserve the observed relationship among the variables.

## Pump-State Distribution

| Pump state | Daily probability | Supply multiplier |
|---|---:|---:|
| Normal | 96.0% | 1.00 |
| Reduced capacity | 3.5% | 0.65 |
| Outage | 0.5% | 0.00 |

Sample one pump state for each simulated day.

## Simulation Requirements

- Use Python.
- Use `numpy.random.default_rng(20260926)`.
- Run 20,000 trials.
- Simulate 30 consecutive days per trial.
- Start each trial at 1.20 MG.
- Cap available storage at 1.50 MG.
- Record storage deficit before clamping a negative value.

## Trial-Level Outputs

For each trial, retain:

- minimum storage;
- ending storage;
- number of days below 0.30 MG;
- whether any violation occurred;
- first violation day;
- number of reduced-capacity days; and
- number of outage days.

## Required Results

- Probability of at least one 30-day violation
- Reliability, calculated as `1 − probability of any violation`
- Expected number of violation days
- P10, P50, and P90 minimum storage
- Distribution of first violation day
- Probability of ending below 0.30 MG
- Relationship between outages, reduced-capacity days, and violations

## Required Visuals

- Histogram of minimum 30-day storage
- Cumulative distribution of minimum storage
- Bar chart of first-violation day
- Five randomly selected storage trajectories
- One storage trajectory from a failed trial

## Validation Checks

- Confirm storage does not exceed 1.50 MG.
- Record deficits before clamping storage at zero.
- Confirm pump-state probabilities total 100%.
- Confirm simulated outage frequency is approximately 0.5%.
- Manually calculate the first three days of one trial.
- Force demand and supply to their historical means and compare with the baseline.
- Compare results at 5,000 and 20,000 trials.
- Confirm `any violation` and `number of violation days` are separate metrics.

## Interpretation Questions

1. Why can the deterministic model pass while the simulation shows failure risk?
2. What is the difference between ending below 0.30 MG and falling below it at any time?
3. Does 98% reliability mean the tank will fail exactly twice in 100 months?
4. How does independently resampling pump state each day limit the model?
5. What additional SCADA or maintenance data would improve the model?

## Deliverables

- Clean operating dataset
- Cleaning or exception log
- Deterministic 30-day storage calculation
- Python simulation notebook
- Trial-level reliability output
- Summary and percentile tables
- Required reliability plots
- Five-sentence engineering decision summary

---

# Optional Assignment 3 — Monthly Rebalancing vs. Buy-and-Hold

## Starting Portfolio

```text
Stocks: $60,000
Bonds:  $40,000
Total: $100,000
```

## Strategy A — Monthly Rebalancing

Reset the portfolio to 60% stocks and 40% bonds at the beginning of each simulated month.

## Strategy B — Buy-and-Hold

Make the initial investment and allow weights to drift for 12 months.

## Tasks

- Use 10,000 paired-return trials from Assignment 1.
- Calculate mean and median ending value for each strategy.
- Calculate P10 and P90 ending value.
- Calculate probability of loss.
- Calculate average final stock weight.
- Report the range of final stock weights under buy-and-hold.
- Identify practical costs omitted from the model.

## Deliverables

- Strategy comparison table
- Ending-value comparison chart
- One-paragraph interpretation

---

# Optional Assignment 4 — Daily vs. Cumulative Failure Risk

## Scenario

Assume an independent 1% probability of failure on any day.

## Analytical Calculation

Use:

```text
P(at least one failure in n days)
    = 1 − (1 − p)^n
```

## Tasks

- Calculate the probability of at least one failure over 1, 7, 30, 90, and 365 days.
- Verify each result using 100,000 Monte Carlo trials.
- Plot planning horizon against cumulative failure probability.
- Repeat the analysis using a 0.1% daily probability.
- Compare the exact result with the approximation `n × p`.
- Explain the independence assumption.
- Explain how multi-day outages would violate independence.

## Deliverables

- Analytical-results table
- Monte Carlo verification table
- Planning-horizon probability chart
- One-paragraph engineering interpretation

---

# Week 3 Completion Checklist

- [ ] Raw price and operating data preserved
- [ ] Cleaning exceptions documented
- [ ] Deterministic baselines calculated
- [ ] Portfolio covariance included
- [ ] Paired and independent sampling distinguished
- [ ] Simulation horizons stated
- [ ] Random seed and trial count recorded
- [ ] At least one trial from each model manually checked
- [ ] Results compared at two trial counts
- [ ] Finance results exported to an Excel dashboard
- [ ] Engineering reliability reported for the full 30-day horizon
- [ ] Limitations and next actions documented

# Week 3 Reflection

Answer briefly:

1. Where did dependence change a result or its interpretation?
2. Which percentile was most useful for the finance decision?
3. Which reliability metric was most useful for the engineering decision?
4. What did the deterministic baselines fail to reveal?
5. Which model assumption should be improved first?

