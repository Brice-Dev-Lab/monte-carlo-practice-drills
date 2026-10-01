# Monte Carlo Modeling — Week 3 Detailed Description

## Week 3 Theme

**Correlation, joint behavior, and risk accumulated across time**

Week 3 extends the Monte Carlo workflow in two important directions:

1. uncertain variables may be related rather than independent; and
2. a small single-period risk can become material when exposure continues over many periods.

The finance exercise studies two assets whose returns may move together. The municipal-engineering exercise studies a storage system exposed to 30 consecutive days of uncertain demand, supply, and pump availability.

The central principle is:

> A model must represent both the behavior of individual variables and the relationships among those variables across the relevant decision horizon.

## Learning Objectives

By completing Week 3, the learner should be able to:

- calculate and interpret covariance and correlation;
- distinguish joint sampling from independent sampling;
- simulate a correlated multi-asset portfolio;
- distinguish expected return from portfolio volatility;
- calculate and interpret maximum drawdown;
- build a sequential storage mass-balance simulation;
- distinguish a point-in-time condition from any failure during a horizon;
- calculate cumulative failure probability;
- interpret reliability over a defined planning period; and
- explain important limitations caused by independence assumptions.

## Assignment Structure

| Assignment | Primary concept | Decision output |
|---|---|---|
| Two-asset portfolio | Correlation and joint sampling | One-year downside risk |
| Water-storage reliability | Sequential simulation | Probability of a 30-day violation |
| Rebalancing comparison | Decision rules | Effect of portfolio-weight management |
| Cumulative-risk comparison | Repeated exposure | Multi-period failure probability |

## Recommended Workflow

For each main assignment:

1. Define the decision question.
2. Load and inspect the source data.
3. Clean and document exceptions.
4. Calculate a deterministic baseline.
5. Define uncertain inputs and relationships.
6. Run the Monte Carlo simulation.
7. Validate selected trials and aggregate results.
8. Export results.
9. Prepare a decision-facing interpretation.

---

# Assignment 1 — Correlated Two-Asset Portfolio

## Purpose

The portfolio assignment introduces uncertainty involving more than one variable. It demonstrates why portfolio risk cannot be calculated correctly by examining each asset independently.

The portfolio contains:

- 60% stock-market exposure through `SPY`; and
- 40% bond-market exposure through `BND`.

The initial investment is $100,000.

## Decision Context

The investor wants to understand the plausible range of portfolio values after one year.

The model must answer:

- What is the expected range of ending values?
- What is the probability of losing money?
- What is the probability of losing more than 10%?
- How severe might the maximum drawdown become during the year?
- How does the relationship between stocks and bonds affect those results?

## Why Adjusted Prices Are Used

Adjusted prices account for distributions and corporate actions reflected by the data provider. They are generally more appropriate than unadjusted closing prices for calculating historical holding-period returns.

The learner should still inspect the retrieved columns. A data provider or Python package may change its output structure, and blindly selecting a column can produce an incorrect return series.

## Data-Cleaning Purpose

The source dataset may contain:

- duplicate dates;
- missing adjusted prices;
- numeric values stored as text;
- incomplete months;
- dates in inconsistent formats; and
- observations that do not align between assets.

Both asset returns must cover the same months before covariance, correlation, or paired bootstrap sampling is calculated.

## Return Calculation

Monthly simple return is:

```text
r_t = Price_t / Price_(t−1) − 1
```

The first price observation does not have a preceding price and therefore does not produce a return.

A one-day change displayed on a market website is not an estimate of expected return. Expected return in this exercise is estimated from a historical series of monthly returns.

## Deterministic Expected Return

The portfolio's expected monthly return is:

```text
E(r_p) = w_s E(r_s) + w_b E(r_b)
```

where:

- `w_s` is the stock weight;
- `w_b` is the bond weight;
- `E(r_s)` is expected stock return; and
- `E(r_b)` is expected bond return.

With 60/40 weights:

```text
E(r_p) = 0.60 E(r_s) + 0.40 E(r_b)
```

Standard deviation is not expected return. It measures variability around the expected return.

## Portfolio Variance

Portfolio variance includes covariance:

```text
σ_p² = w_s²σ_s²
     + w_b²σ_b²
     + 2w_s w_b Cov(r_s, r_b)
```

If correlation is written explicitly:

```text
Cov(r_s, r_b) = ρ_sb σ_s σ_b
```

The covariance term determines how much diversification occurs. Two volatile assets can form a less volatile portfolio when their returns do not move together strongly.

## Correlation

Correlation measures the direction and strength of linear co-movement:

- `+1` indicates perfect positive co-movement;
- `0` indicates no linear relationship; and
- `−1` indicates perfect negative co-movement.

Correlation is not constant through time and does not prove causation. Historical correlation is an input estimate, not a law governing future returns.

## Model A — Paired Bootstrap

Model A samples a complete historical row.

If a stock return from a particular month is selected, the bond return from that same month is selected. This retains the observed joint behavior of the two assets.

Conceptually:

```text
selected row i → stock return_i and bond return_i
```

This approach preserves:

- each asset's empirical return distribution; and
- the empirical dependence between the assets.

## Model B — Independent Bootstrap

Model B samples stock and bond returns separately:

```text
selected stock row i → stock return_i
selected bond row j  → bond return_j
```

Each marginal return distribution is retained, but the historical relationship is removed.

Comparing the models demonstrates whether dependence materially changes the portfolio's simulated risk.

If the results are similar, that does not mean the model failed. It may mean the observed correlation was weak or that the chosen risk metrics are not highly sensitive to it over a 12-month horizon.

## Monthly Rebalancing

The primary model assumes the portfolio returns to 60/40 each month:

```text
r_portfolio,t = 0.60r_stock,t + 0.40r_bond,t
```

The one-year ending value is:

```text
Ending value = $100,000 × ∏(1 + r_portfolio,t)
```

Monthly rebalancing holds the intended risk allocation constant but ignores transaction costs, taxes, bid–ask spreads, and practical rebalancing thresholds.

## Maximum Drawdown

Maximum drawdown measures the largest peak-to-trough decline within a simulated path.

For each month:

```text
Running peak_t = maximum portfolio value observed through month t

Drawdown_t = Portfolio value_t / Running peak_t − 1

Maximum drawdown = minimum Drawdown_t
```

Ending value and maximum drawdown answer different questions. A portfolio can recover and finish above its starting value while still experiencing a substantial interim drawdown.

## Required Interpretation

The final dashboard should distinguish:

- expected outcome;
- downside percentile;
- probability of loss;
- probability of a loss greater than 10%; and
- interim drawdown risk.

The conclusion should not claim that the historical bootstrap predicts next year's return. It describes outcomes generated under the assumption that historical monthly behavior remains informative.

## Common Errors

- Using one-day market changes as expected returns
- Using price levels instead of calculated returns
- Failing to align asset dates
- Averaging asset standard deviations to calculate portfolio volatility
- Omitting covariance
- Sampling assets independently in the paired model
- Adding monthly returns instead of compounding them
- Calculating drawdown only from the starting value
- Treating P10 as a guaranteed lower bound
- Ignoring the effect of the portfolio rule

## Definition of Completion

Assignment 1 is complete when the learner can explain:

1. how monthly returns were calculated;
2. how covariance affects portfolio volatility;
3. how paired sampling differs from independent sampling;
4. how one simulated ending value is calculated;
5. how maximum drawdown differs from total return; and
6. what the selected downside metrics mean for the investor.

---

# Assignment 2 — Water-Storage Reliability

## Purpose

The storage assignment introduces a sequential engineering simulation. Each day's ending storage becomes the next day's beginning storage.

This differs from a model in which every trial is independent and produces only one output. The system's state evolves across 30 simulated days.

## System Definition

| Variable | Value |
|---|---:|
| Usable maximum storage | 1.50 MG |
| Beginning storage | 1.20 MG |
| Minimum operating criterion | 0.30 MG |
| Simulation horizon | 30 days |

This is a planning-level storage mass balance. It is not a hydraulic model and does not calculate:

- system pressure;
- head loss;
- pump operating points;
- fire-flow performance;
- water age; or
- hydraulic transients.

## Decision Context

The utility needs to understand whether variable demand, variable supply, and pump events could cause the tank to fall below the minimum operating criterion.

The relevant risk is not merely whether the tank ends Day 30 below 0.30 MG. A violation on any intervening day matters.

## Data-Cleaning Purpose

The operating dataset intentionally contains:

- a duplicated date;
- missing demand;
- supply stored with unit text;
- impossible negative demand;
- inconsistent pump-status information; and
- unsorted observations.

The cleaned data must have:

- one record per day;
- numeric demand and supply;
- standardized units;
- documented treatment of missing and invalid values; and
- standardized pump-status categories.

## Deterministic Baseline

The deterministic calculation uses mean demand and mean supply for every day:

```text
S_t = min(S_max, S_(t−1) + Q_supply,t − Q_demand,t)
```

where:

- `S_t` is ending storage;
- `S_max` is 1.50 MG;
- `Q_supply,t` is daily supply; and
- `Q_demand,t` is daily demand.

The deterministic result provides:

- minimum storage;
- Day 30 ending storage; and
- a pass/fail check against 0.30 MG.

The deterministic model can pass even when the stochastic model shows risk because average conditions conceal unfavorable combinations and sequences.

## Historical Row Sampling

Demand, supply, and temperature are sampled together from a complete historical row.

This preserves observed relationships such as:

- hotter days coinciding with higher demand; and
- operational conditions affecting recorded supply.

Sampling each column independently would create combinations that may not reflect observed operating behavior.

## Pump-State Events

For every simulated day, select one pump state:

| State | Probability | Supply multiplier |
|---|---:|---:|
| Normal | 96.0% | 1.00 |
| Reduced capacity | 3.5% | 0.65 |
| Outage | 0.5% | 0.00 |

The sampled historical supply is multiplied by the pump-state factor.

This introductory model treats daily pump states as independent. It therefore does not represent repair duration, failure persistence, or conditional failure probability.

## Sequential Trial Calculation

For each 30-day trial:

1. Set beginning storage to 1.20 MG.
2. Sample one historical operating row.
3. Sample the pump state.
4. Adjust supply using the pump-state multiplier.
5. Calculate unconstrained ending storage.
6. Record any deficit or minimum-storage violation.
7. Cap usable storage at 1.50 MG.
8. Carry ending storage into the next day.
9. Repeat through Day 30.

The unconstrained value should be retained before clamping storage at zero. Otherwise, the magnitude of a storage deficit is hidden.

## Reliability Metrics

### Probability of Any Violation

```text
P(any violation)
    = Number of trials with at least one day below 0.30 MG
      ÷ Total number of trials
```

### Thirty-Day Reliability

```text
Reliability = 1 − P(any violation)
```

Reliability must always be stated with its horizon. “98% reliable over 30 days” is different from 98% daily reliability or 98% annual reliability.

### Violation Days

The number of violation days measures duration or recurrence within the horizon. It is distinct from the binary indicator of whether any violation occurred.

### Minimum Storage

The minimum storage reached during the 30-day path is the principal severity metric.

### First Violation Day

The distribution of first violation day indicates how quickly the system becomes vulnerable under unfavorable conditions.

## Required Interpretation

The engineering summary should state:

- deterministic minimum storage;
- simulated probability of any violation;
- 30-day reliability;
- P10 and median minimum storage;
- likely timing of failures;
- dominant reliability driver; and
- recommended next analysis or operational action.

Possible next actions include:

- collecting better SCADA data;
- estimating pump failure and repair duration;
- evaluating alternative pump schedules;
- testing emergency supply conditions;
- increasing usable storage; or
- performing a hydraulic model.

## Common Errors

- Resetting storage to 1.20 MG every day
- Examining only Day 30 storage
- Failing to cap storage at 1.50 MG
- Clamping storage to zero before recording deficit
- Applying the pump multiplier to demand instead of supply
- Treating any violation and number of violation days as the same measure
- Interpreting 30-day reliability as annual reliability
- Sampling related historical columns independently
- Treating independent one-day outages as realistic multi-day failures

## Definition of Completion

Assignment 2 is complete when the learner can explain:

1. how the cleaned operating data were created;
2. how storage evolves from one day to the next;
3. how historical-row and pump-state sampling work;
4. how any violation differs from an ending violation;
5. what 30-day reliability means; and
6. which additional data would most improve the analysis.

---

# Assignment 3 — Rebalancing Versus Buy-and-Hold

## Purpose

The companion finance assignment isolates the effect of the investment rule.

Both strategies use identical sampled returns but apply them differently.

## Monthly Rebalancing

At the start of each month, restore the portfolio to 60% stocks and 40% bonds.

This maintains the intended asset allocation.

## Buy-and-Hold

Invest $60,000 and $40,000 initially and allow each position to evolve independently.

If stocks outperform bonds, the stock weight rises. If stocks underperform, the stock weight falls.

## Required Comparison

Compare:

- ending-value distribution;
- probability of loss;
- downside percentile;
- final stock weight; and
- allocation drift.

The analysis should recognize that monthly rebalancing omits transaction costs and taxes.

## Definition of Completion

The learner should be able to explain why two portfolio rules can produce different outcomes from the same return paths.

---

# Assignment 4 — Daily Versus Cumulative Failure Risk

## Purpose

This companion engineering assignment separates daily failure probability from cumulative risk over a planning horizon.

If daily failure probability is `p` and daily events are independent:

```text
P(no failures in n days) = (1 − p)^n
```

Therefore:

```text
P(at least one failure in n days) = 1 − (1 − p)^n
```

## Required Horizons

Calculate the cumulative probability over:

- 1 day;
- 7 days;
- 30 days;
- 90 days; and
- 365 days.

Repeat for:

- 1.0% daily risk; and
- 0.1% daily risk.

## Approximation

For small `p` and short horizons:

```text
P(at least one failure) ≈ n × p
```

This approximation deteriorates as `n × p` becomes larger and can eventually produce impossible values greater than 100%.

## Independence Limitation

The formula assumes daily failures are independent. It is inappropriate when:

- one failure persists across several days;
- a common cause affects multiple days;
- failure probability changes with system condition; or
- a previous event changes the probability of another event.

## Definition of Completion

The learner should be able to distinguish:

- single-day failure probability;
- expected number of failures;
- probability of at least one failure; and
- reliability over a stated horizon.

---

# Week 3 Validation Requirements

Every Week 3 model should include:

- a deterministic baseline;
- a reproducible random seed;
- a stated trial count and horizon;
- documented sampling method;
- explicit treatment of dependence;
- one manually checked path or trial;
- a comparison at two trial counts;
- inspection of extreme outcomes;
- clear units; and
- a written limitations statement.

# Week 3 Deliverables

## Finance

- Raw and clean adjusted-price data
- Monthly returns
- Deterministic return and volatility calculation
- Paired-bootstrap simulation
- Independent-bootstrap comparison
- Drawdown results
- Excel dashboard
- Risk interpretation

## Municipal Engineering

- Raw and clean operating data
- Deterministic storage trajectory
- Thirty-day Monte Carlo simulation
- Reliability and violation metrics
- Storage trajectories and distribution plots
- Engineering recommendation

## Optional Companions

- Rebalancing versus buy-and-hold comparison
- Analytical and simulated cumulative-risk comparison

# Recommended Weekly Sequence

## Session 1 — Portfolio Data and Baseline

- Retrieve or generate prices.
- Clean and align both asset series.
- Calculate monthly returns.
- Calculate expected return, covariance, and portfolio volatility.

## Session 2 — Portfolio Simulation and Dashboard

- Run paired and independent bootstrap models.
- Calculate ending values and drawdowns.
- Validate selected trials.
- Export results and build the dashboard.

## Session 3 — Storage Data and Baseline

- Generate and clean operating data.
- Calculate mean demand and supply.
- Build the deterministic 30-day storage trajectory.
- Define pump-state probabilities.

## Session 4 — Storage Simulation and Interpretation

- Run the 30-day reliability simulation.
- Calculate violation and minimum-storage metrics.
- Create the required plots.
- Write the engineering decision summary.

## Optional Session 5 — Companion Assignments

- Compare rebalancing with buy-and-hold.
- Compare daily with cumulative failure probability.

# Final Reflection

Answer in `week_03_reflection.md`:

1. How did dependence affect the portfolio result?
2. Did paired and independent sampling produce materially different downside risk?
3. What did maximum drawdown reveal that ending value did not?
4. Why did the deterministic storage result differ from the probabilistic result?
5. Which reliability metric best communicated the engineering risk?
6. How did the planning horizon change the interpretation of failure probability?
7. Which independence assumption is least defensible?
8. What additional data would provide the greatest improvement?

# Week 3 Definition of Done

Week 3 is complete when the learner can independently:

- calculate asset returns from aligned price data;
- distinguish expected return from volatility;
- incorporate covariance into portfolio risk;
- preserve or remove dependence intentionally;
- simulate compounded portfolio outcomes;
- calculate maximum drawdown;
- simulate sequential storage behavior;
- calculate any-failure probability and reliability;
- distinguish daily risk from cumulative risk; and
- communicate limitations without presenting the simulation as a prediction.

