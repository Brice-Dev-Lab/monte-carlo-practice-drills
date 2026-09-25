# Monte Carlo Modeling Drills — Week 2

## Weekly Concept

**Choosing bounded distributions and translating input uncertainty into decision risk**

Week 1 introduced empirical sampling and exceedance probability. Week 2 moves to **parametric distributions**—especially triangular, beta-PERT, lognormal, and discrete distributions—when historical data are limited but reasonable low, most-likely, and high estimates are available.

The central lesson is:

> A Monte Carlo model is only as defensible as the assumptions used to generate its inputs.

## This Week's Workload

| Drill | Domain | Target time | Priority |
|---|---|---:|---|
| 1. Blue Ridge revenue forecast | Finance | 75–90 minutes | Required |
| 2. Water-main construction cost | Municipal engineering | 75–90 minutes | Required |
| 3. Distribution comparison | Finance | 25–35 minutes | Companion |
| 4. Quantity/unit-price dependency | Municipal engineering | 25–35 minutes | Companion |

If time is limited, complete Drills 1 and 2. The companion drills can wait.

## Scope Control

Use one notebook for each main drill:

```text
week_02/
├── finance_revenue_forecast.ipynb
├── engineering_cost_risk.ipynb
├── data/
├── excel/
└── outputs/
```

Do not create separate ingestion, EDA, baseline, simulation, and reporting notebooks this week. Use labeled sections inside each notebook:

1. Load and inspect
2. Clean
3. Deterministic baseline
4. Simulation assumptions
5. Monte Carlo simulation
6. Validation
7. Export

---

# Drill 1 — Finance: Blue Ridge 12-Month Revenue Risk

## Scenario

Blue Ridge Digital LLC is a fictional digital-marketing agency with approximately $2.4 million in annual revenue. Management expects 20% growth next year, but the forecast depends on client retention, new-client wins, and the timing of account starts.

Management wants a range of plausible annual revenue outcomes before committing to four new employees.

## Decision Question

What is the probability that next year's revenue:

- falls below the current $2.4 million run rate;
- reaches the $2.88 million management target; and
- supports a preliminary hiring threshold of $2.70 million?

This drill addresses revenue only. Payroll, cash collections, and the full hiring decision will be added in later weeks.

## Part A — Generate the Messy Source Data

Run this once and save the result as `data/blue_ridge_monthly_revenue_dirty.csv`:

```python
from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(20260919)

months = pd.date_range("2024-01-01", periods=24, freq="MS")
seasonality = np.array(
    [0.92, 0.95, 0.98, 1.00, 1.02, 1.04, 0.97, 0.96, 1.03, 1.08, 1.10, 0.95]
)
trend = np.linspace(0.96, 1.08, 24)
base_revenue = 185_000
noise = rng.normal(1.0, 0.055, 24)

revenue = base_revenue * np.tile(seasonality, 2) * trend * noise

df = pd.DataFrame(
    {
        "Month": months,
        "Revenue": np.round(revenue, 2),
        "Active Clients": rng.integers(15, 20, 24),
        "Status": "Final",
    }
)

# Add realistic defects.
df.loc[4, "Revenue"] = f"${df.loc[4, 'Revenue']:,.2f}"
df.loc[9, "Revenue"] = np.nan
df.loc[16, "Active Clients"] = -1
df.loc[22, "Status"] = "Estimate"
df = pd.concat([df, df.iloc[[7]]], ignore_index=True)
df = df.sample(frac=1, random_state=19).reset_index(drop=True)

output = Path("data/blue_ridge_monthly_revenue_dirty.csv")
output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)
```

## Part B — Start in Excel

Create `excel/blue_ridge_revenue_risk.xlsx` with these sheets:

- `Raw_Data`
- `Clean_Data`
- `Assumptions`
- `Baseline_Forecast`
- `Simulation_Summary`
- `Dashboard`

Import the raw CSV into `Raw_Data`. Use Power Query or documented Excel steps to:

1. Parse `Month` as a date.
2. Convert `Revenue` to numeric after removing currency symbols and commas.
3. Identify the duplicate month.
4. Flag the impossible negative client count.
5. Decide how to treat the missing-revenue month.
6. Distinguish final values from the estimated month.
7. Sort the clean result chronologically.

Do not overwrite the raw sheet.

## Deterministic Baseline

Build a simple 12-month forecast using:

```text
Current annualized run rate = Sum of the latest 12 cleaned months
Management growth assumption = 20%
Target annual revenue = Current run rate × 1.20
```

Create a monthly baseline by applying the most recent year's monthly revenue mix to the annual target.

The baseline is not expected to be sophisticated. It is the control case used to check the simulation.

## Part C — Define the Simulation Inputs

Model three drivers:

| Driver | Suggested distribution | Parameters |
|---|---|---|
| Existing-client retention rate | Triangular | low 82%, mode 91%, high 97% |
| New clients won during year | Discrete | 2, 3, 4, 5, or 6 clients with probabilities 10%, 20%, 35%, 25%, 10% |
| Annual revenue per new client | Triangular | $72,000 low, $96,000 mode, $132,000 high |

Use the latest 12-month run rate as the existing-client revenue base.

For each trial:

```text
Retained revenue = Current run rate × retention rate
New-client revenue = New clients × annual revenue per new client × timing factor
Simulated annual revenue = Retained revenue + new-client revenue
```

Use a triangular timing factor with:

```text
low = 0.35
mode = 0.60
high = 0.90
```

The timing factor represents the portion of a full year's revenue recognized because clients begin throughout the year.

## Part D — Run the Simulation in Python

Run 20,000 trials with:

```python
rng = np.random.default_rng(20260919)
```

Required outputs:

- mean and median annual revenue;
- P10, P25, P50, P75, and P90 revenue;
- probability revenue is below the current run rate;
- probability revenue reaches the management target;
- probability revenue exceeds the $2.70 million preliminary hiring threshold; and
- correlations between each sampled input and simulated revenue.

Export:

- a trial-level table containing the four sampled inputs and annual revenue;
- a summary table;
- a percentile table; and
- a sensitivity table.

## Part E — Finish in Excel

Build a management-facing dashboard containing:

- current annual revenue run rate;
- deterministic 20% growth target;
- simulated mean and median;
- P10, P50, and P90 revenue;
- probability of reaching $2.88 million;
- probability of exceeding $2.70 million;
- histogram of annual revenue;
- cumulative probability or percentile chart; and
- top two revenue-risk drivers.

Add a brief recommendation such as:

> The revenue simulation supports advancing the hiring analysis, but revenue alone is insufficient to authorize four hires. Payroll timing, collections, and minimum-cash requirements must be incorporated before a final decision.

## Quality-Control Checks

- Verify the probabilities assigned to new-client counts sum to 100%.
- Confirm retention never falls below 0% or exceeds 100%.
- Confirm new-client revenue and timing factors cannot be negative.
- Force all inputs to their most-likely values and compare the result with a hand calculation.
- Confirm all trial revenues equal retained revenue plus new-client revenue.
- Compare results using 5,000 and 20,000 trials.
- Make certain the Excel dashboard is linked to exported results rather than manually typed values.

## Interpretation Questions

1. Why can the simulated median be below the deterministic 20% growth target?
2. Which assumption contributes most to revenue uncertainty?
3. Is the mean or P50 more useful for management planning here?
4. What is missing before recommending the hiring of four employees?
5. How might retention and new-client wins be dependent in the real business?

## Brief Solution Checkpoints

- The simulation should not automatically center on the 20% target; the target is a management goal, not a probability distribution.
- New-client revenue must be reduced by the timing factor. Treating every client as if it starts January 1 will overstate revenue.
- A strong probability of exceeding $2.70 million does not establish that cash will be available when payroll is due.

---

# Drill 2 — Municipal Engineering: Water-Main Construction Cost Risk

## Scenario

A municipality is preparing a planning-level estimate for a 6,000-linear-foot, 12-inch PVC water-main replacement. The project includes open-cut pipe installation, pavement restoration, fittings, traffic control, mobilization, and a construction contingency.

The deterministic estimate uses fixed quantities and unit prices. The project manager wants a probabilistic estimate to determine the P50 and P80 construction budgets.

## Decision Question

What are the simulated P50 and P80 construction costs, and what contingency above the deterministic base estimate is required to fund the project at P80?

## Part A — Generate the Messy Estimate

Run this once and save the output as `data/water_main_estimate_dirty.csv`:

```python
from pathlib import Path

import pandas as pd

rows = [
    ["WM-01", "12-in PVC water main", "LF", "6,000", "$185.00", "Pipeline"],
    ["PV-01", "12-in gate valve", "EA", "12", "$8,500", "Appurtenance"],
    ["FT-01", "Fittings and restraints", "LS", "1", "$185,000", "Appurtenance"],
    ["PR-01", "Asphalt pavement restoration", "SY", "8,400", "$74.00", "Restoration"],
    ["TC-01", "Maintenance of traffic", "LS", "1", "$310,000", "General"],
    ["MB-01", "Mobilization", "%", "8%", "", "General"],
    ["WM-01", "12-in PVC water main", "LF", "6000", "$185.00", "Pipeline"],
    ["UN-01", "Unknown utility conflict allowance", "LS", "1", "TBD", "Risk"],
]

df = pd.DataFrame(
    rows,
    columns=["Item ID", "Description", "Unit", "Quantity", "Unit Price", "Category"],
)

output = Path("data/water_main_estimate_dirty.csv")
output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)
```

## Part B — Clean and Establish the Baseline

In the notebook:

1. Standardize column names.
2. Remove currency symbols and commas from numeric fields.
3. Separate the percentage-based mobilization item from quantity × unit-price items.
4. Identify and resolve the duplicated `WM-01` row.
5. Retain the unknown-utility item as an explicit risk rather than silently entering zero.
6. Create an exception log documenting the duplicate, percentage item, and `TBD` unit price.

Calculate the deterministic direct cost:

```text
Direct item cost = Quantity × Unit price
Subtotal before mobilization = Sum of direct item costs
Mobilization = 8% × Subtotal before mobilization
Deterministic base estimate = Subtotal + Mobilization
```

For the deterministic baseline only, use a $150,000 allowance for unknown utility conflicts.

Do not add a general contingency to the base estimate; the purpose of the simulation is to derive a risk-based amount.

## Part C — Define the Cost Distributions

Use these preliminary distributions:

| Cost driver | Distribution | Low | Most likely | High |
|---|---|---:|---:|---:|
| Installed pipeline unit price | Triangular | $165/LF | $185/LF | $235/LF |
| Pavement quantity | Triangular | 7,500 SY | 8,400 SY | 10,500 SY |
| Pavement unit price | Triangular | $65/SY | $74/SY | $105/SY |
| Fittings/restraints | Triangular | $160,000 | $185,000 | $260,000 |
| Traffic control | Triangular | $260,000 | $310,000 | $475,000 |
| Utility conflicts | Discrete scenario | See below | | |
| Mobilization | Triangular percentage | 7% | 8% | 11% |

Model unknown utility conflicts with this discrete distribution:

| Cost | Probability |
|---:|---:|
| $50,000 | 20% |
| $150,000 | 45% |
| $300,000 | 25% |
| $600,000 | 10% |

Keep pipe quantity, valve quantity, and valve unit price fixed this week so the model remains manageable.

## Part D — Run the Simulation

Run 20,000 trials using:

```python
rng = np.random.default_rng(20260919)
```

For every trial:

1. Sample each uncertain input.
2. Calculate each bid-item cost.
3. Calculate the subtotal before mobilization.
4. Apply the sampled mobilization percentage.
5. Calculate total construction cost.

Report:

- mean and median total cost;
- P10, P50, P80, and P90 cost;
- probability of exceeding the deterministic base estimate;
- P80 contingency in dollars;
- P80 contingency as a percentage of deterministic base cost; and
- rank correlation between each uncertain input and total cost.

## Required Visuals

- Histogram of simulated construction cost
- Cumulative distribution curve with deterministic, P50, and P80 markers
- Tornado or horizontal bar chart of sensitivity rankings

## Decision Summary

Write a five-sentence summary that states:

1. the deterministic base estimate;
2. the P50 estimate;
3. the P80 estimate;
4. the P80 contingency amount and percentage; and
5. the two primary cost-risk drivers and recommended next estimating action.

## Quality-Control Checks

- Confirm duplicate bid items were not counted twice.
- Confirm the utility-conflict probabilities total 100%.
- Confirm quantities, unit prices, and mobilization remain nonnegative.
- Recalculate one selected trial manually.
- Force all triangular samples to their modes and utility conflicts to $150,000; confirm the result is consistent with the deterministic baseline.
- Compare the P80 from 5,000 and 20,000 trials.
- Confirm mobilization is applied once and only once.

## Interpretation Questions

1. Why is the simulated mean not necessarily equal to the deterministic base estimate?
2. What does a P80 budget mean in plain language?
3. Does a P80 budget guarantee that the project will not exceed budget?
4. Why should utility conflicts be treated as a discrete scenario rather than a normal distribution?
5. Which field investigation would provide the greatest value for reducing uncertainty?

## Brief Solution Checkpoints

- The P80 contingency is `P80 total cost − deterministic base estimate`; it is not an assumed 20% markup.
- The high-cost utility-conflict scenario should occur in approximately 10% of a large set of trials.
- Pipeline unit price will likely be a major risk driver because it applies to 6,000 LF.
- Pavement quantity and pavement unit price jointly influence restoration cost, even though they are modeled independently in this introductory drill.

---

# Drill 3 — Finance Companion: Triangular vs. Beta-PERT

## Objective

Understand how two bounded distributions using the same low, most-likely, and high estimates can produce different results.

## Scenario

Management estimates annual revenue per new client as:

```text
Low:          $72,000
Most likely:  $96,000
High:        $132,000
```

## Tasks

1. Generate 50,000 samples from a triangular distribution.
2. Generate 50,000 samples from a beta-PERT distribution using the same three estimates and a conventional shape parameter of 4.
3. Compare the mean, median, standard deviation, P10, and P90.
4. Plot the two distributions on the same chart.
5. State which distribution places more weight near the most-likely estimate.

For beta-PERT:

```text
alpha = 1 + shape × (mode − low) / (high − low)
beta  = 1 + shape × (high − mode) / (high − low)

PERT sample = low + Beta(alpha, beta) × (high − low)
```

## Interpretation Questions

1. Why is choosing a distribution more than a cosmetic modeling decision?
2. Which distribution better reflects a manager who is confident in the most-likely estimate?
3. What evidence would justify one choice over the other?

## Solution Checkpoint

With the conventional PERT shape parameter, beta-PERT should concentrate more observations near the mode and produce fewer values near the limits than the triangular distribution.

---

# Drill 4 — Municipal Engineering Companion: Quantity and Unit-Price Dependency

## Objective

Recognize when treating inputs as independent can understate or distort project risk.

## Scenario

In Drill 2, pavement-restoration quantity and unit price were sampled independently. In practice, they may be related:

- a larger restoration area may attract more competitive pricing and reduce unit price; or
- extensive restoration may reflect difficult site conditions that also increase unit price.

## Tasks

Run two 20,000-trial models using only pavement cost:

```text
Pavement cost = Pavement quantity × Pavement unit price
```

### Model A — Independent Inputs

Sample quantity and unit price independently using the Drill 2 triangular assumptions.

### Model B — Positively Correlated Inputs

Create standardized correlated normal values with a target correlation of approximately `+0.50`, convert them to uniform percentiles, and use inverse triangular distributions to generate quantity and unit price.

Compare:

- correlation achieved between quantity and unit price;
- mean pavement cost;
- standard deviation;
- P50, P80, and P90 pavement cost; and
- probability pavement cost exceeds $800,000.

## Interpretation Questions

1. How did positive correlation change the upper tail?
2. Why can correlation matter even if the individual input distributions are unchanged?
3. What project evidence would support positive versus negative correlation?

## Solution Checkpoint

Positive correlation should generally increase the probability that high quantities and high unit prices occur together, producing a heavier upper cost tail than the independent-input model.

---

# Week 2 Completion Checklist

- [ ] Raw source data retained unchanged
- [ ] Cleaning exceptions documented
- [ ] Deterministic baseline calculated before simulation
- [ ] Distribution choices and parameters recorded
- [ ] Bounds checked for physical and financial plausibility
- [ ] Random seed and trial count recorded
- [ ] At least one trial manually recalculated
- [ ] Simulation stability checked at two trial counts
- [ ] Finance results exported to an Excel dashboard
- [ ] Engineering P50 and P80 costs reported
- [ ] Sensitivity results interpreted
- [ ] Limitations stated without overstating predictive certainty

# End-of-Week Reflection

Write five short answers:

1. Which distribution choice was hardest to justify?
2. Which model input had the greatest effect on the result?
3. Where did bounded distributions prevent unrealistic values?
4. How did the probabilistic result change the decision compared with the deterministic baseline?
5. What information would you collect before using either model on a real assignment?

