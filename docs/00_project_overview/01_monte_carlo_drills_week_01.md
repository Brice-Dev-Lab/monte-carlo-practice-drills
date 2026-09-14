# Monte Carlo Modeling Drills — Week 1

## Weekly Theme

**From deterministic estimates to distributions of possible outcomes**

This week introduces four foundational ideas:

1. cleaning data before estimating uncertainty;
2. calculating returns correctly;
3. empirical resampling versus assumed probability distributions; and
4. interpreting probability of loss or capacity exceedance.

Do the drills in order. The companion drills are intentionally shorter.

## Setup

Use Python 3.12 and `uv`.

```bash
uv init
uv add numpy pandas scipy matplotlib seaborn openpyxl xlsxwriter yfinance
```

Recommended folders:

```text
week_01/
├── data/
│   ├── raw/
│   └── processed/
├── excel/
├── notebooks/
├── outputs/
└── README.md
```

For every simulation, use a local generator:

```python
rng = np.random.default_rng(20260914)
```

---

# Drill 1 — Finance: One-Asset Return and Loss Risk

## Estimated Time

75–90 minutes

## Scenario

A small-business owner has $100,000 of excess cash. She is considering investing $40,000 in a broad-market exchange-traded fund while retaining $60,000 in cash. She wants to understand the range of possible one-year values—not merely the historical average return.

Use **SPY** as the default ticker. You may substitute another liquid ETF.

## Decision Question

Based on historical monthly returns, what is the simulated probability that the $40,000 investment loses money over the next 12 months, and what are its P10, P50, and P90 ending values?

## Important Distinction

The expected return is an estimate of the center of the return distribution. Standard deviation measures dispersion around that center. Standard deviation is **not** the expected return.

## Part A — Start in Excel

Create `finance_01_portfolio_risk.xlsx` with these sheets:

- `Instructions`
- `Raw_Prices`
- `Clean_Prices`
- `Monthly_Returns`
- `Assumptions`
- `Simulation_Output`
- `Dashboard`

### Data Option A — Yahoo Finance

In Python, retrieve approximately ten years of monthly SPY data and save the untouched result to `data/raw/SPY_monthly_raw.csv`.

```python
import yfinance as yf

raw = yf.download(
    "SPY",
    start="2016-01-01",
    end="2026-01-01",
    interval="1mo",
    auto_adjust=False,
    progress=False,
)
raw.to_csv("data/raw/SPY_monthly_raw.csv")
```

If the API output structure differs, inspect the returned columns instead of forcing the code to run unchanged.

### Data Option B — Synthetic Fallback

Generate 120 monthly returns with a modest positive mean, volatility, and occasional negative shocks. Convert them to a price series beginning at 100. Deliberately add:

- one duplicate date;
- two missing adjusted prices;
- one numeric value stored as text;
- rows in descending date order; and
- one clearly labeled provisional final row.

### Cleaning Tasks

In Excel or Power Query:

1. Standardize the date column.
2. Sort chronologically.
3. Remove duplicate dates using a documented rule.
4. Decide how to treat missing adjusted prices.
5. Exclude the provisional/incomplete month.
6. Confirm prices are numeric and greater than zero.
7. Preserve the untouched raw data.

### Return Calculation

Calculate simple monthly returns:

```text
Return_t = Adjusted_Close_t / Adjusted_Close_(t-1) - 1
```

On the `Assumptions` sheet, calculate:

- arithmetic mean monthly return;
- median monthly return;
- monthly standard deviation;
- minimum and maximum monthly return;
- observation count; and
- deterministic one-year ending value using the mean monthly return.

Do not multiply the monthly arithmetic mean by 12 and then compound that number as though it were a monthly return.

## Part B — Simulate in Python

Import the cleaned monthly returns from Excel. Use **empirical bootstrap sampling** for the first model: each simulated month is randomly selected, with replacement, from the cleaned historical monthly returns.

Run at least 10,000 trials of 12 months each.

For trial `i`:

```text
Ending Value_i = 40,000 × product(1 + sampled monthly returns)
```

Calculate:

- mean and median ending value;
- P10, P50, and P90 ending values;
- probability ending value is below $40,000;
- probability loss exceeds 10%; and
- mean annual simulated return.

Export:

- one row per trial to `Simulation_Output`;
- a compact summary table;
- a histogram-ready set of bins; and
- metadata containing the seed, number of trials, ticker, data period, and refresh date.

## Part C — Finish in Excel

Build a one-page dashboard containing:

- initial investment;
- deterministic ending value;
- simulated mean and median;
- P10/P50/P90 ending values;
- probability of loss;
- probability of losing more than 10%;
- histogram of ending values; and
- a short recommendation or caution statement.

Use language such as “10% of simulated outcomes were below…” rather than claiming the model knows the future.

## Validation Checks

- When every sampled monthly return is replaced with the historical mean, does Python reproduce the Excel deterministic result?
- Does changing the seed alter individual trials but leave the main summary reasonably stable?
- Are any ending values negative? If so, investigate the input-return data.
- Compare 1,000, 10,000, and 100,000 trials. How stable is the P10 value?

## Interpretation Questions

1. Why can the simulated median differ from the deterministic value based on the arithmetic mean?
2. Does the probability of loss measure maximum possible loss?
3. What market behavior is missing when individual months are sampled independently?
4. Would this simulation alone justify investing operating cash?

---

# Drill 2 — Municipal Engineering: Culvert Capacity Exceedance

## Estimated Time

75–90 minutes

## Scenario

A municipality has 30 years of annual peak-flow estimates for a drainage crossing. The existing culvert has an estimated hydraulic capacity of **700 cfs**. The city is considering whether the current crossing presents enough risk to justify a more detailed alternatives analysis.

## Decision Question

Using historical resampling, what is the probability that flow exceeds 700 cfs in any single year and at least once during the next 10 years?

## Create the Raw Dataset

Create `data/raw/engineering/week_01/annual_peak_flows_dirty.csv` using this generator, then work only from the saved dirty file:

```python
from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(20260914)
years = np.arange(1996, 2026)
flows = rng.lognormal(mean=np.log(420), sigma=0.38, size=len(years))

df = pd.DataFrame(
    {
        "Water Year": years,
        "Peak Flow": np.round(flows, 1),
        "Units": "cfs",
        "Status": "Final",
    }
)

# Inject realistic defects. Peak Flow holds a stray string, so it must be
# object dtype -- pandas refuses to upcast float64 on assignment.
df["Peak Flow"] = df["Peak Flow"].astype(object)
df.loc[5, "Peak Flow"] = np.nan
df.loc[12, "Peak Flow"] = " 515.6 "
df.loc[18, "Units"] = "CFS"
df.loc[23, "Peak Flow"] = -45.0
df.loc[28, "Status"] = "Provisional"
df = pd.concat([df, df.iloc[[9]]], ignore_index=True)
df = df.sample(frac=1, random_state=41).reset_index(drop=True)

Path("data/raw/engineering/week_01").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/engineering/week_01/annual_peak_flows_dirty.csv", index=False)
```

## Data-Cleaning Tasks

1. Strip whitespace and standardize column names.
2. Coerce peak flow to numeric while logging conversion failures.
3. Standardize units.
4. Identify the duplicate water year.
5. Flag the negative flow as physically invalid.
6. Decide whether the provisional observation belongs in the analysis.
7. Decide how to handle the missing flow. Do not silently replace it with the mean.
8. Save the clean dataset and a separate exception log.

## Deterministic Baseline

Calculate:

- mean, median, standard deviation, minimum, and maximum flow;
- historical fraction of valid annual peaks exceeding 700 cfs; and
- empirical percentile corresponding to 700 cfs.

Plot the historical histogram and empirical CDF.

## Monte Carlo Simulation

Use empirical bootstrap sampling from the cleaned annual peaks.

### Model A — One-Year Risk

Run 100,000 trials, sampling one annual peak in each trial.

```text
Exceedance = Simulated Peak Flow > 700 cfs
```

### Model B — Ten-Year Planning-Horizon Risk

Run 100,000 trials containing 10 sampled annual peaks. A trial is a failure if **one or more** of its ten years exceeds 700 cfs.

Calculate:

- annual exceedance probability;
- ten-year probability of at least one exceedance;
- expected number of exceedance years in ten years;
- distribution of the maximum ten-year flow; and
- P50, P80, P90, and P95 of the maximum ten-year flow.

## Analytical Check

If annual events are assumed independent and annual exceedance probability is `p`, compare the simulated result with:

```text
P(at least one exceedance in n years) = 1 - (1 - p)^n
```

Explain why a 10% annual exceedance probability does **not** mean a 10% chance over ten years.

## Deliverable

Create a one-page Excel or Markdown decision summary containing:

- data period and number of usable observations;
- capacity threshold;
- annual exceedance probability;
- 10-year exceedance probability;
- distribution of maximum 10-year flow;
- primary limitations; and
- recommendation for the next level of study.

Do not call the empirical result a regulatory design storm or a calibrated flood-frequency analysis.

## Interpretation Questions

1. What assumption permits the analytical 10-year formula?
2. How does the short record affect confidence in tail risk?
3. Does an exceedance necessarily mean structural failure or flooding?
4. What additional hydraulic, survey, rainfall, or condition data would improve the decision?

---

# Drill 3 — Finance Companion: Distribution Choice Challenge

## Estimated Time

30–45 minutes

## Scenario

Blue Ridge Digital is preparing a 13-week cash forecast. Management gives you these uncertain inputs:

| Input | Current estimate | Known constraints |
|---|---:|---|
| Weekly new sales | $46,000 | Positive; occasionally much higher than normal |
| Collection delay | 45 days | Cannot be negative; clusters near 30, 45, and 60 days |
| Employee start date | Week 5 | Discrete week; may be delayed |
| Monthly software cost | $18,000 | Contractual base plus usage charges |
| Client churn event | 0 or 1 | Either occurs or does not occur during the forecast |

## Task

For each input:

1. Decide whether it should be fixed, categorical, discrete, or continuous.
2. Propose one possible distribution or empirical-sampling method.
3. State its parameters in plain language.
4. Identify required bounds.
5. State one dependency with another business variable.
6. Explain what data you would request before finalizing the assumption.

Create an assumptions register with these columns:

```text
Input | Unit | Base Case | Uncertainty Method | Parameters | Bounds |
Dependency | Data Source | Rationale | Owner | Review Date
```

## Mini-Simulation

Choose **weekly new sales** and compare 10,000 samples from:

- a normal distribution; and
- a lognormal or triangular distribution with a similar center.

Compare the minimum, maximum, mean, median, P10, and P90. Identify any impossible or implausible values.

## Interpretation Question

Which distribution would you use provisionally, and what evidence could cause you to change it?

---

# Drill 4 — Municipal Engineering Companion: Convergence and Contingency

## Estimated Time

30–45 minutes

## Scenario

A preliminary water-main estimate contains the following uncertain cost components:

| Component | Base estimate |
|---|---:|
| Pipeline construction | $4,200,000 |
| Roadway restoration | $650,000 |
| Utility conflicts | $300,000 |
| Mobilization and general conditions | $500,000 |

For this introductory drill, assume each component varies independently using triangular distributions:

| Component | Low | Most likely | High |
|---|---:|---:|---:|
| Pipeline construction | 90% | 100% | 125% |
| Roadway restoration | 85% | 100% | 140% |
| Utility conflicts | 50% | 100% | 250% |
| Mobilization/general conditions | 95% | 100% | 120% |

## Decision Question

What contingency is required for the authorized project budget to equal the simulated P80 cost?

## Tasks

1. Calculate the deterministic base estimate.
2. Simulate total cost using 100, 1,000, 10,000, and 100,000 trials.
3. Record mean, P50, P80, P90, minimum, and maximum for each trial count.
4. Calculate:

```text
P80 Contingency = P80 Simulated Cost - Deterministic Base Estimate
Contingency % = P80 Contingency / Deterministic Base Estimate
```

5. Plot P80 versus trial count.
6. Repeat each trial count using five different seeds and compare stability.

## Important Limitation

Independence is a temporary teaching assumption. Construction components often share escalation, market, weather, site-condition, and schedule drivers. Note how independence may understate aggregate risk.

## Interpretation Questions

1. At what trial count does P80 become sufficiently stable for this exercise?
2. Why is the maximum simulated value a poor basis for routine contingency?
3. Does a P80 budget guarantee the project will not exceed budget?
4. Which input needs the most estimating effort, and why?

---

# Weekly Review

After all four drills, write a 200–300 word reflection answering:

1. What did Monte Carlo reveal that the deterministic calculation concealed?
2. Where did data cleaning change a calculated result?
3. Which probability statement was easiest to misinterpret?
4. What distinction can you now make between expected return and volatility?
5. What one modeling habit will you carry into Week 2?

## Week 1 Completion Checklist

- [ ] Raw data retained unchanged
- [ ] Cleaning decisions documented
- [ ] Deterministic baselines calculated
- [ ] Random seed recorded
- [ ] Trial count recorded
- [ ] Simulation output checked for impossible values
- [ ] At least one convergence check completed
- [ ] Finance results returned to an Excel dashboard
- [ ] Engineering result stated as a decision risk
- [ ] Limitations documented
- [ ] Interpretation questions answered in the learner's own words

## Optional Solution Checkpoints

Use these only after attempting the drills:

- In Drill 1, the simulated ending value is based on compounded sampled monthly returns—not the standard deviation and not a one-day price change.
- In Drill 2, the simulated 10-year probability should be close to `1 - (1 - p)^10` when years are sampled independently.
- In Drill 3, a distribution that permits materially negative sales is inappropriate unless refunds or reversals are explicitly being modeled.
- In Drill 4, the P80 contingency is the difference between P80 total cost and the deterministic base estimate; it is not automatically 20%.
