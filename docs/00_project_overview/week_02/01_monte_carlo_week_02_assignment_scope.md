# Monte Carlo Modeling — Week 2 Assignment Scope

## Weekly Topic

**Bounded probability distributions and decision risk**

## Required Assignments

1. Finance: Blue Ridge Digital 12-month revenue-risk model
2. Municipal engineering: Water-main construction-cost risk model

## Optional Companion Assignments

3. Finance: Triangular versus beta-PERT distributions
4. Municipal engineering: Quantity and unit-price dependency

## Expected Time

| Assignment | Expected time | Priority |
|---|---:|---|
| Blue Ridge revenue risk | 75–90 minutes | Required |
| Water-main construction cost | 75–90 minutes | Required |
| Triangular vs. beta-PERT | 25–35 minutes | Optional |
| Quantity/unit-price dependency | 25–35 minutes | Optional |

## Recommended Files

```text
week_02/
├── data/
├── excel/
├── outputs/
├── finance_revenue_forecast.ipynb
├── engineering_cost_risk.ipynb
└── week_02_reflection.md
```

Use one notebook for each required assignment.

---

# Assignment 1 — Blue Ridge Digital Revenue Risk

## Scenario

Blue Ridge Digital LLC generates approximately $2.4 million in annual revenue. Management expects 20% growth and is considering hiring four employees.

## Decision Questions

Estimate the probability that next year's revenue:

- falls below the current annual run rate;
- exceeds the preliminary $2.70 million hiring threshold; and
- reaches the $2.88 million management target.

Identify the two inputs with the greatest influence on simulated revenue.

## Source Data

Generate 24 months of revenue data using the supplied generator from the Week 2 drill package.

The dataset must include:

- monthly revenue;
- active-client count;
- final or estimated status;
- one duplicate month;
- one missing revenue value;
- one revenue value stored as formatted text;
- one impossible client count; and
- unsorted dates.

Save the raw file as:

```text
data/blue_ridge_monthly_revenue_dirty.csv
```

## Excel Workbook

Create:

```text
excel/blue_ridge_revenue_risk.xlsx
```

Required worksheets:

- `Raw_Data`
- `Clean_Data`
- `Assumptions`
- `Baseline_Forecast`
- `Simulation_Summary`
- `Dashboard`

## Data-Cleaning Tasks

- Parse the month field as a date.
- Sort observations chronologically.
- Convert revenue to numeric.
- Identify and resolve the duplicate month.
- Flag the negative active-client count.
- Document treatment of the missing revenue value.
- Distinguish estimated data from final data.
- Preserve the original raw data.
- Create a cleaning or exception log.

## Deterministic Baseline

Calculate:

```text
Current annual run rate = Sum of latest 12 cleaned months

Management revenue target = Current annual run rate × 1.20
```

Allocate the annual target across 12 months using the latest year's monthly revenue mix.

## Simulation Inputs

### Existing-Client Retention

| Distribution | Low | Most likely | High |
|---|---:|---:|---:|
| Triangular | 82% | 91% | 97% |

### New Clients Won

| New clients | Probability |
|---:|---:|
| 2 | 10% |
| 3 | 20% |
| 4 | 35% |
| 5 | 25% |
| 6 | 10% |

### Annual Revenue per New Client

| Distribution | Low | Most likely | High |
|---|---:|---:|---:|
| Triangular | $72,000 | $96,000 | $132,000 |

### New-Client Timing Factor

| Distribution | Low | Most likely | High |
|---|---:|---:|---:|
| Triangular | 0.35 | 0.60 | 0.90 |

## Trial Calculation

```text
Retained revenue
    = Current annual run rate × sampled retention rate

New-client revenue
    = Sampled new-client count
    × sampled annual revenue per client
    × sampled timing factor

Simulated annual revenue
    = Retained revenue + new-client revenue
```

## Simulation Requirements

- Use Python.
- Use `numpy.random.default_rng(20260919)`.
- Run 20,000 trials.
- Retain the sampled input values for every trial.
- Export trial-level and summary results to Excel.

## Required Results

- Mean annual revenue
- Median annual revenue
- P10, P25, P50, P75, and P90 annual revenue
- Probability of revenue below the current run rate
- Probability of revenue above $2.70 million
- Probability of revenue at or above $2.88 million
- Correlation or rank correlation between each input and annual revenue
- Ranking of the principal revenue-risk drivers

## Dashboard Requirements

- Current annual run rate
- Deterministic management target
- Simulated mean and median
- P10, P50, and P90 revenue
- Probability of exceeding $2.70 million
- Probability of reaching $2.88 million
- Histogram of simulated revenue
- Cumulative probability or percentile chart
- Sensitivity chart
- Two- or three-sentence management conclusion

## Validation Checks

- Confirm new-client probabilities total 100%.
- Confirm retention remains between 0% and 100%.
- Confirm new-client counts are integers.
- Confirm sampled revenue and timing factors are nonnegative.
- Manually recalculate one selected trial.
- Force inputs to their most-likely values and verify the result.
- Compare results using 5,000 and 20,000 trials.
- Confirm dashboard values are linked to exported results.

## Interpretation Questions

1. Why can the simulated median differ from the 20% growth target?
2. Which input contributes most to revenue uncertainty?
3. Is the mean or P50 more useful for planning?
4. What additional analysis is required before authorizing four hires?
5. How could client retention and new-client wins be related?

## Deliverables

- Clean revenue dataset
- Cleaning or exception log
- Excel deterministic forecast
- Python simulation notebook
- Trial-level simulation output
- Summary, percentile, and sensitivity tables
- Excel dashboard
- Short management recommendation

---

# Assignment 2 — Water-Main Construction-Cost Risk

## Scenario

A municipality is preparing a planning-level estimate for 6,000 linear feet of 12-inch PVC water-main replacement. The project includes open-cut installation, valves, fittings and restraint, pavement restoration, maintenance of traffic, mobilization, and unknown utility conflicts.

## Decision Questions

Determine:

- the deterministic base estimate;
- the simulated P50 and P80 construction costs;
- the contingency required to fund the project at P80; and
- the two inputs with the greatest influence on total cost.

## Source Estimate

Create the following raw estimate:

| Item ID | Description | Unit | Quantity | Unit price | Category |
|---|---|---|---:|---:|---|
| WM-01 | 12-inch PVC water main | LF | 6,000 | $185 | Pipeline |
| PV-01 | 12-inch gate valve | EA | 12 | $8,500 | Appurtenance |
| FT-01 | Fittings and restraints | LS | 1 | $185,000 | Appurtenance |
| PR-01 | Asphalt pavement restoration | SY | 8,400 | $74 | Restoration |
| TC-01 | Maintenance of traffic | LS | 1 | $310,000 | General |
| MB-01 | Mobilization | % | 8% | — | General |
| WM-01 | Duplicate water-main row | LF | 6,000 | $185 | Pipeline |
| UN-01 | Unknown utility conflicts | LS | 1 | TBD | Risk |

Save the raw file as:

```text
data/water_main_estimate_dirty.csv
```

## Data-Cleaning Tasks

- Standardize column names.
- Remove currency symbols and commas from numeric fields.
- Identify and remove the duplicate water-main item.
- Separate percentage-based mobilization from unit-price items.
- Retain unknown utility conflicts as an explicit risk item.
- Document the duplicate, percentage item, and `TBD` price in an exception log.
- Preserve the original raw estimate.

## Deterministic Baseline

Use:

```text
Item cost = Quantity × Unit price

Subtotal before mobilization = Sum of direct and lump-sum costs

Mobilization = 8% × Subtotal before mobilization

Deterministic base estimate = Subtotal + Mobilization
```

Use $150,000 as the deterministic allowance for utility conflicts.

Do not add a general contingency to the deterministic base estimate.

## Simulation Inputs

| Driver | Distribution | Low | Most likely | High |
|---|---|---:|---:|---:|
| Installed pipeline unit price | Triangular | $165/LF | $185/LF | $235/LF |
| Pavement quantity | Triangular | 7,500 SY | 8,400 SY | 10,500 SY |
| Pavement unit price | Triangular | $65/SY | $74/SY | $105/SY |
| Fittings and restraints | Triangular | $160,000 | $185,000 | $260,000 |
| Maintenance of traffic | Triangular | $260,000 | $310,000 | $475,000 |
| Mobilization | Triangular | 7% | 8% | 11% |

Keep the following fixed:

- pipeline quantity;
- valve quantity; and
- valve unit price.

## Utility-Conflict Scenarios

| Utility-conflict cost | Probability |
|---:|---:|
| $50,000 | 20% |
| $150,000 | 45% |
| $300,000 | 25% |
| $600,000 | 10% |

## Trial Calculation

For each trial:

1. Sample the installed pipeline unit price.
2. Calculate pipeline cost.
3. Sample pavement quantity and unit price.
4. Calculate pavement-restoration cost.
5. Sample fittings and restraint cost.
6. Sample traffic-control cost.
7. Select one utility-conflict scenario.
8. Add fixed valve cost.
9. Calculate subtotal before mobilization.
10. Sample the mobilization percentage.
11. Apply mobilization once.
12. Calculate total construction cost.

## Simulation Requirements

- Use Python.
- Use `numpy.random.default_rng(20260919)`.
- Run 20,000 trials.
- Retain all sampled input values and calculated costs.
- Export trial-level and summary results.

## Required Results

- Mean total construction cost
- Median total construction cost
- P10, P50, P80, and P90 construction cost
- Probability of exceeding the deterministic base estimate
- P80 contingency in dollars
- P80 contingency as a percentage of deterministic base cost
- Correlation or rank correlation between each uncertain input and total cost
- Ranking of principal cost-risk drivers

Use:

```text
P80 contingency
    = P80 simulated cost − deterministic base estimate

P80 contingency percentage
    = P80 contingency ÷ deterministic base estimate
```

## Required Visuals

- Histogram of simulated construction cost
- Cumulative distribution curve
- Markers for deterministic cost, P50, P80, and P90
- Sensitivity or tornado chart

## Validation Checks

- Confirm the duplicate bid item is counted only once.
- Confirm utility-conflict probabilities total 100%.
- Confirm quantities, prices, and percentages remain nonnegative.
- Verify the $600,000 conflict scenario occurs in approximately 10% of trials.
- Manually recalculate one selected trial.
- Force triangular inputs to their modes and utility conflicts to $150,000.
- Compare P80 using 5,000 and 20,000 trials.
- Confirm mobilization is applied once.

## Interpretation Questions

1. Why can the simulated mean differ from the deterministic estimate?
2. What does P80 mean in plain language?
3. Does a P80 budget guarantee the project will remain within budget?
4. Why are utility conflicts represented as discrete scenarios?
5. Which investigation would most effectively reduce cost uncertainty?

## Deliverables

- Clean bid-item estimate
- Cleaning or exception log
- Deterministic base estimate
- Python simulation notebook
- Trial-level simulation output
- P50/P80/P90 summary table
- Cost histogram
- Cumulative distribution curve
- Sensitivity chart
- Five- or six-sentence engineering recommendation

---

# Optional Assignment 3 — Triangular vs. Beta-PERT

## Inputs

```text
Low:          $72,000
Most likely:  $96,000
High:        $132,000
```

## Tasks

- Generate 50,000 triangular samples.
- Generate 50,000 beta-PERT samples using a shape parameter of 4.
- Compare mean, median, standard deviation, P10, and P90.
- Plot both distributions on one chart.
- Identify which distribution places more weight near the most-likely value.
- State which distribution is more appropriate when management is confident in the mode.

## Deliverables

- Summary comparison table
- Overlaid distribution chart
- One-paragraph interpretation

---

# Optional Assignment 4 — Quantity and Unit-Price Dependency

## Cost Relationship

```text
Pavement cost = Pavement quantity × Pavement unit price
```

## Model A — Independent Inputs

Sample pavement quantity and unit price independently using the Assignment 2 triangular distributions.

## Model B — Positively Correlated Inputs

Use a target correlation of approximately `+0.50` between pavement quantity and pavement unit price.

## Tasks

- Run 20,000 trials for each model.
- Report achieved input correlation.
- Compare mean, standard deviation, P50, P80, and P90 pavement cost.
- Compare the probability that pavement cost exceeds $800,000.
- Explain how positive correlation affects upper-tail cost risk.

## Deliverables

- Independent-versus-correlated comparison table
- Distribution or cumulative-probability chart
- One-paragraph interpretation

---

# Week 2 Completion Checklist

- [ ] Required raw data generated and preserved
- [ ] Cleaning exceptions documented
- [ ] Deterministic baselines completed
- [ ] Input distributions recorded
- [ ] Random seed recorded
- [ ] 20,000-trial simulations completed
- [ ] One trial from each model manually checked
- [ ] Results compared at two trial counts
- [ ] Finance results exported to an Excel dashboard
- [ ] Engineering P50 and P80 costs reported
- [ ] Sensitivity results interpreted
- [ ] Management and engineering recommendations written
- [ ] Model limitations documented

# Week 2 Reflection

Answer briefly:

1. Which input distribution was hardest to justify?
2. Which input drove the finance result?
3. Which input drove the engineering result?
4. How did P10 revenue differ in meaning from P80 cost?
5. What did the simulations reveal that the deterministic baselines did not?

