# Monte Carlo Modeling — Week 2 Detailed Description

## Week 2 Theme

**Choosing bounded probability distributions and converting uncertain inputs into decision risk**

Week 2 is the transition from a basic Monte Carlo demonstration to a decision-support model.

In Week 1, the central idea was that historical observations can be resampled to create many plausible outcomes. Week 2 introduces a different situation: the available historical data are incomplete, but an analyst, manager, estimator, or engineer can still define reasonable ranges for uncertain inputs.

The focus is therefore not simply on generating random values. The focus is on answering four questions:

1. Which inputs are genuinely uncertain?
2. What values can each input reasonably take?
3. Which probability distribution best expresses the available knowledge?
4. How does the input uncertainty affect a management or engineering decision?

The two main exercises apply this process to:

- a small-business revenue and hiring decision; and
- a municipal water-main construction budget.

The two shorter companion exercises examine:

- the difference between triangular and beta-PERT distributions; and
- the effect of dependency between construction quantity and unit price.

## Central Learning Objective

By the end of Week 2, the learner should be able to explain why a Monte Carlo result is not merely a more complicated deterministic estimate.

A deterministic model produces one result from one set of assumptions:

```text
Output = f(fixed input 1, fixed input 2, fixed input 3)
```

A Monte Carlo model repeatedly samples uncertain inputs:

```text
Output_i = f(sampled input 1_i, sampled input 2_i, sampled input 3_i)
```

The result is a distribution of outcomes rather than one number. That distribution can support decisions such as:

- How likely is the company to achieve its revenue target?
- How much revenue downside should management prepare for?
- What project budget corresponds to P50 or P80 confidence?
- Which uncertain input deserves additional investigation?

## Expected Time Commitment

| Component | Expected time |
|---|---:|
| Drill 1 — Blue Ridge revenue risk | 75–90 minutes |
| Drill 2 — Water-main construction cost | 75–90 minutes |
| Drill 3 — Triangular vs. beta-PERT | 25–35 minutes |
| Drill 4 — Quantity/unit-price dependency | 25–35 minutes |
| Final reflection and file cleanup | 15–20 minutes |

The two main drills are the required work. The companion exercises are optional if workload or project responsibilities make the full week unrealistic.

## Recommended Project Structure

Week 2 should be completed without expanding the project into an elaborate notebook system.

```text
week_02/
├── data/
│   ├── blue_ridge_monthly_revenue_dirty.csv
│   └── water_main_estimate_dirty.csv
├── excel/
│   ├── blue_ridge_revenue_risk.xlsx
│   └── water_main_cost_risk_summary.xlsx
├── outputs/
│   ├── blue_ridge_simulation_results.xlsx
│   └── water_main_simulation_results.xlsx
├── finance_revenue_forecast.ipynb
├── engineering_cost_risk.ipynb
└── week_02_reflection.md
```

Use one notebook for each main drill. Inside each notebook, use the following sections:

1. Problem definition
2. Data loading and inspection
3. Data cleaning
4. Deterministic baseline
5. Uncertain-input assumptions
6. Monte Carlo simulation
7. Validation and quality control
8. Results and interpretation
9. Export to Excel

The purpose is to practice Monte Carlo modeling—not spend most of the week constructing a perfect repository architecture.

---

# Drill 1 — Blue Ridge Digital Revenue Risk

## Business Context

Blue Ridge Digital LLC is a fictional digital-marketing agency generating approximately $2.4 million in annual revenue. Management is forecasting 20% growth and is considering hiring four employees.

The management target is:

```text
$2.4 million × 1.20 = $2.88 million
```

That calculation is a target, not a probability forecast. It states what management hopes to achieve but does not state how likely the result is.

Week 2 converts that target into a risk question:

> Given uncertainty in client retention, new-client wins, account value, and start timing, what range of annual revenue is plausible?

## Decision Questions

The model must estimate:

- the probability that revenue falls below the existing run rate;
- the probability that revenue exceeds a preliminary $2.70 million hiring threshold;
- the probability that revenue reaches the $2.88 million management target; and
- which assumption contributes most to revenue uncertainty.

The $2.70 million value is only a preliminary revenue threshold. It does not prove the company can afford four employees because the model does not yet include payroll timing, collections, working capital, taxes, or minimum-cash requirements.

## Why the Drill Begins in Excel

The business model begins in Excel because a small-business owner or FP&A client is likely to review assumptions and results there.

Excel is used to:

- preserve the raw monthly revenue data;
- clean and document the historical information;
- establish the current revenue run rate;
- build the deterministic 20% growth forecast;
- record probability assumptions; and
- present the final management dashboard.

Python is used for the simulation because it can generate and analyze thousands of trials transparently and reproducibly.

The workflow is:

```text
Messy revenue data
        ↓
Excel cleaning and deterministic baseline
        ↓
Python Monte Carlo simulation
        ↓
Excel management dashboard and recommendation
```

## Data-Cleaning Purpose

The provided revenue dataset intentionally contains:

- currency values stored as text;
- a missing revenue observation;
- a duplicate month;
- an impossible negative active-client count;
- an estimated rather than final observation; and
- dates presented out of chronological order.

These defects are not busywork. They demonstrate that simulation quality depends on the data and assumptions entering the model.

The cleaning process should produce:

- one valid observation per month;
- a numeric revenue field;
- reasonable active-client counts;
- clearly documented treatment of missing and estimated values; and
- a chronologically sorted analysis dataset.

## Deterministic Baseline

The deterministic model establishes a control case:

```text
Current annual run rate = sum of latest 12 cleaned months

Management target = current annual run rate × 1.20
```

The latest 12-month revenue pattern should be used to allocate the annual target across months. This preserves observed seasonality without requiring a formal time-series model.

The deterministic model is important because it allows the learner to verify that the simulation model has been constructed correctly. If all uncertain inputs are fixed at their assumed values, the result should be explainable with a hand calculation.

## Uncertain Revenue Drivers

### Existing-Client Retention

Retention is modeled using a triangular distribution:

| Parameter | Value |
|---|---:|
| Low | 82% |
| Most likely | 91% |
| High | 97% |

The distribution is bounded because retention cannot reasonably be negative or greater than 100%.

The triangular distribution is appropriate for this introductory drill because management can express a pessimistic, most-likely, and optimistic estimate even without a large historical retention dataset.

### New Clients Won

New-client count is discrete:

| New clients | Probability |
|---:|---:|
| 2 | 10% |
| 3 | 20% |
| 4 | 35% |
| 5 | 25% |
| 6 | 10% |

This variable must be discrete because the business cannot win 3.7 clients.

The probabilities must total 100%.

### Annual Revenue per New Client

Annual revenue per new client is modeled using:

| Parameter | Value |
|---|---:|
| Low | $72,000 |
| Most likely | $96,000 |
| High | $132,000 |

The upper and lower bounds prevent the model from generating negative revenue or implausibly large client values.

### Client-Start Timing

A client beginning in July does not produce a full year of revenue. The timing factor represents the portion of annual revenue recognized during the forecast year:

| Parameter | Value |
|---|---:|
| Low | 0.35 |
| Most likely | 0.60 |
| High | 0.90 |

Ignoring this factor would incorrectly treat every new client as though the engagement began January 1.

## Trial Calculation

Each simulation trial follows this logic:

```text
Retained revenue
    = Current annual run rate × sampled retention rate

New-client revenue
    = Sampled client count
    × sampled annual revenue per client
    × sampled timing factor

Total simulated revenue
    = Retained revenue + new-client revenue
```

Run 20,000 trials using a recorded random seed.

## Required Results

The Python output must include:

- mean annual revenue;
- median annual revenue;
- P10, P25, P50, P75, and P90 revenue;
- probability of revenue below the current run rate;
- probability of revenue above $2.70 million;
- probability of revenue at or above $2.88 million; and
- sensitivity of total revenue to each uncertain input.

## Interpretation of Percentiles

For revenue, the lower percentiles generally represent less favorable outcomes.

For example:

```text
P10 revenue = a value that approximately 10% of simulated outcomes fall below
```

P10 is therefore useful as a downside-planning measure.

P90 revenue is an optimistic result, not a conservative budget value. The direction of risk matters: low revenue is unfavorable, whereas high project cost is unfavorable.

## Excel Dashboard

The final dashboard should communicate:

- current annual revenue;
- deterministic management target;
- simulated mean and median;
- P10, P50, and P90 revenue;
- probability of exceeding $2.70 million;
- probability of reaching $2.88 million;
- annual-revenue histogram;
- cumulative probability chart; and
- the two most influential revenue drivers.

The dashboard should finish with a management conclusion. A reasonable conclusion may be that the revenue outlook justifies continuing the hiring analysis, but it does not authorize hiring until cash collections and payroll are modeled.

## Common Errors

- Treating the 20% growth target as the expected value of the simulation
- Omitting the new-client timing factor
- Using a normal distribution that permits impossible retention values
- Allowing a noninteger client count
- Confusing annual revenue with annual cash receipts
- Reporting the mean without showing downside percentiles
- Treating correlation as proof of causation in the sensitivity analysis
- Typing dashboard values manually rather than linking exported results

## Definition of Completion

Drill 1 is complete when the learner can explain:

1. how the raw revenue data were cleaned;
2. how the deterministic target was calculated;
3. why each probability distribution was chosen;
4. how one trial calculates revenue;
5. what the P10, P50, and P90 values mean; and
6. why the simulation alone does not authorize the hiring decision.

---

# Drill 2 — Water-Main Construction Cost Risk

## Engineering Context

The project is a planning-level estimate for approximately 6,000 linear feet of 12-inch PVC water-main replacement. The work includes:

- open-cut water-main installation;
- valves;
- fittings and restraint;
- asphalt-pavement restoration;
- maintenance of traffic;
- mobilization; and
- unknown utility conflicts.

Traditional estimating produces a deterministic base cost and then often applies a standard contingency percentage. The purpose of this drill is to estimate contingency from the modeled uncertainty rather than assume a generic percentage.

## Decision Question

The model must determine:

- the deterministic base estimate;
- the simulated P50 construction cost;
- the simulated P80 construction cost;
- the contingency required to fund the project at P80; and
- the dominant cost-risk drivers.

## Why P50 and P80 Matter

For project cost, higher values are unfavorable.

```text
P50 cost = approximately 50% of outcomes are at or below this value

P80 cost = approximately 80% of outcomes are at or below this value
```

P80 is a more conservative funding value than P50 because it provides a greater probability that the available budget will be sufficient.

P80 does not guarantee that the project will remain within budget. Approximately 20% of modeled outcomes still exceed P80 if the model assumptions are representative.

## Data-Cleaning Purpose

The raw estimate includes:

- currency symbols and commas;
- a duplicated water-main bid item;
- mobilization expressed as a percentage rather than a unit-price item;
- a `TBD` utility-conflict allowance; and
- mixed item types and calculation rules.

The cleaning process should distinguish:

- direct quantity × unit-price items;
- lump-sum items;
- percentage-based items;
- duplicated records; and
- uncertain allowances requiring separate modeling.

The duplicate pipeline row must not be counted twice. The unknown-utility item must not be silently converted to zero.

## Deterministic Baseline

For direct items:

```text
Item cost = Quantity × Unit price
```

Then:

```text
Subtotal before mobilization
    = Sum of direct and lump-sum costs

Mobilization
    = 8% × subtotal before mobilization

Deterministic base estimate
    = Subtotal before mobilization + mobilization
```

Use $150,000 as the deterministic unknown-utility allowance.

Do not add a general contingency to the baseline. The difference between the selected simulated percentile and the base estimate will become the modeled contingency.

## Uncertain Cost Drivers

| Driver | Distribution | Low | Most likely | High |
|---|---|---:|---:|---:|
| Installed pipeline unit price | Triangular | $165/LF | $185/LF | $235/LF |
| Pavement quantity | Triangular | 7,500 SY | 8,400 SY | 10,500 SY |
| Pavement unit price | Triangular | $65/SY | $74/SY | $105/SY |
| Fittings and restraint | Triangular | $160,000 | $185,000 | $260,000 |
| Traffic control | Triangular | $260,000 | $310,000 | $475,000 |
| Mobilization | Triangular | 7% | 8% | 11% |

The pipe quantity, number of valves, and valve unit price remain fixed to limit the number of variables introduced at once.

## Utility-Conflict Scenarios

Unknown utility conflicts are modeled as discrete outcomes:

| Conflict cost | Probability | Interpretation |
|---:|---:|---|
| $50,000 | 20% | Limited conflicts |
| $150,000 | 45% | Typical allowance condition |
| $300,000 | 25% | Significant relocations or field changes |
| $600,000 | 10% | Major conflict condition |

A discrete distribution is appropriate because the cost represents distinct project conditions rather than continuous measurement error.

## Trial Calculation

Each trial should:

1. sample the installed pipeline unit price;
2. sample pavement quantity and unit price;
3. sample fittings/restraint cost;
4. sample traffic-control cost;
5. select one utility-conflict scenario;
6. calculate subtotal before mobilization;
7. sample the mobilization percentage;
8. apply mobilization once; and
9. calculate total construction cost.

The model should run 20,000 trials with a recorded random seed.

## Required Results

Report:

- mean total cost;
- median total cost;
- P10, P50, P80, and P90 total cost;
- probability of exceeding the deterministic base estimate;
- P80 contingency in dollars;
- P80 contingency as a percentage of deterministic base cost; and
- sensitivity ranking for the uncertain inputs.

The contingency calculations are:

```text
P80 contingency
    = P80 simulated cost − deterministic base estimate

P80 contingency percentage
    = P80 contingency ÷ deterministic base estimate
```

P80 does not mean “add 20%.” The percentile and the contingency percentage are different concepts.

## Required Visuals

### Cost Histogram

Shows the frequency and shape of simulated total construction cost.

### Cumulative Distribution

Shows the probability that total cost is at or below a given value. Mark:

- deterministic base estimate;
- P50 cost;
- P80 cost; and
- P90 cost.

### Sensitivity Chart

Use a horizontal bar chart or tornado-style chart showing rank correlation between each uncertain input and total cost.

The chart should answer:

> Which uncertain assumptions have the greatest influence on total project cost?

## Engineering Interpretation

The final write-up should state:

1. the deterministic estimate;
2. the P50 cost;
3. the P80 cost;
4. the P80 contingency amount and percentage;
5. the leading risk drivers; and
6. the recommended action to reduce uncertainty.

Examples of uncertainty-reduction actions include:

- additional subsurface utility engineering;
- improved pavement-restoration limits;
- contractor or supplier pricing;
- better traffic-control planning;
- refinement of fittings and restraint requirements; and
- escalation analysis tied to the anticipated bid date.

## Common Errors

- Counting the duplicate water-main row twice
- Treating `TBD` as zero
- Applying mobilization more than once
- Applying mobilization after contingency when the model defines it on direct cost
- Using a normal distribution that permits negative quantities or prices
- Confusing P80 with an 80% contingency
- Calculating contingency from the simulated mean instead of the chosen percentile
- Reporting cost percentiles without explaining their direction
- Assuming independent quantity and unit price without identifying the limitation

## Definition of Completion

Drill 2 is complete when the learner can explain:

1. how the estimate was cleaned;
2. how the deterministic cost was calculated;
3. why each uncertain input uses its selected distribution;
4. how the discrete utility scenarios work;
5. what P50 and P80 mean;
6. how the P80 contingency was derived; and
7. which investigation would most effectively reduce cost uncertainty.

---

# Drill 3 — Triangular Versus Beta-PERT

## Purpose

This companion exercise demonstrates that low, most-likely, and high estimates do not uniquely define one probability distribution.

Both triangular and beta-PERT distributions can use the same three values:

```text
Low:          $72,000
Most likely:  $96,000
High:        $132,000
```

However, they distribute probability differently.

## Triangular Distribution

The triangular distribution connects the low, mode, and high using straight-line probability density.

It is:

- simple to explain;
- easy to implement;
- bounded; and
- useful when information is limited.

It can place more probability toward the bounds than an analyst intends.

## Beta-PERT Distribution

Beta-PERT uses a scaled beta distribution. With a conventional shape parameter of 4, it places more emphasis near the most-likely estimate and less near the low and high bounds.

It is often useful when the estimator believes:

- the minimum and maximum are possible but unusual; and
- the most-likely value deserves greater weight.

## Required Comparison

Generate 50,000 samples from each distribution and compare:

- mean;
- median;
- standard deviation;
- P10;
- P90; and
- distribution shape.

The lesson is not that beta-PERT is always superior. The lesson is that the distribution should match the strength and meaning of the available judgment.

## Completion Standard

The learner should be able to explain why identical low/mode/high inputs can still produce different means, tails, and decision percentiles.

---

# Drill 4 — Quantity and Unit-Price Dependency

## Purpose

The main construction-cost model initially treats pavement quantity and unit price as independent.

Independence means that knowing the sampled quantity provides no information about the sampled unit price. That assumption may be unrealistic.

Possible real-world relationships include:

- larger quantities producing lower unit prices because fixed costs are spread over more work;
- larger quantities occurring on a more complex project and therefore increasing unit prices;
- weather or access problems increasing both restoration quantity and productivity cost; and
- schedule compression increasing quantities performed per period while also increasing price.

## Comparison

Model pavement cost under two cases:

```text
Pavement cost = Quantity × Unit price
```

### Case A — Independent

Sample quantity and unit price independently.

### Case B — Positively Correlated

Use a target correlation of approximately `+0.50`, so larger quantities are more likely to occur with higher unit prices.

Compare:

- achieved input correlation;
- mean pavement cost;
- standard deviation;
- P50, P80, and P90 cost; and
- probability cost exceeds $800,000.

## Expected Learning

Positive correlation should increase the occurrence of high-quantity/high-price combinations and generally increase upper-tail cost risk.

The individual quantity and unit-price distributions do not change. Only their dependency changes. If the cost results change, that demonstrates why correlation is a modeling assumption rather than a minor statistical detail.

## Completion Standard

The learner should be able to explain:

- what independence means;
- why quantity and unit price might be dependent;
- how positive correlation affects the upper tail; and
- what project evidence would justify the selected relationship.

---

# Week 2 Validation Requirements

Every Week 2 model should include:

- a reproducible random seed;
- a stated trial count;
- documented input distributions;
- validation that probabilities total 100%;
- checks preventing impossible values;
- one manually recalculated trial;
- a comparison of results using at least two trial counts;
- a deterministic control calculation;
- a sensitivity analysis; and
- a written statement of limitations.

## Model Stability

Run the main simulations at both 5,000 and 20,000 trials.

The exact trial results will change, but the principal metrics should become reasonably stable:

- mean;
- median;
- selected percentiles;
- probability of exceeding a threshold; and
- sensitivity rankings.

If results change materially as trial count increases, either more trials are required or the model has a coding or tail-behavior issue that needs investigation.

# Week 2 Deliverables

## Finance Deliverables

- Clean monthly revenue dataset
- Cleaning or exception log
- Excel deterministic baseline
- Python simulation notebook
- Trial-level output
- Summary and percentile tables
- Sensitivity table
- Excel management dashboard
- Short hiring-analysis recommendation

## Engineering Deliverables

- Clean bid-item estimate
- Exception log
- Deterministic base estimate
- Python simulation notebook
- Trial-level total-cost output
- P50/P80/P90 summary
- Cost histogram
- Cumulative distribution curve
- Sensitivity chart
- Five- or six-sentence engineering recommendation

## Companion Deliverables

- Triangular versus beta-PERT comparison table and chart
- Independent versus correlated pavement-cost comparison

# Recommended Weekly Sequence

## Session 1 — Finance Setup

- Generate and import the Blue Ridge data.
- Clean the data in Excel.
- Calculate the annual run rate and deterministic target.
- Document the four probability assumptions.

## Session 2 — Finance Simulation and Dashboard

- Run the Python simulation.
- Validate the results.
- Export the summaries.
- Build the Excel dashboard.
- Write the preliminary management conclusion.

## Session 3 — Engineering Setup

- Generate and clean the construction estimate.
- Resolve duplicate and special-calculation items.
- Calculate the deterministic base estimate.
- Build the assumptions table.

## Session 4 — Engineering Simulation and Interpretation

- Run the cost simulation.
- Calculate P50, P80, and P90.
- Derive P80 contingency.
- Create the sensitivity and distribution visuals.
- Write the engineering recommendation.

## Optional Session 5 — Companion Exercises

- Compare triangular and beta-PERT.
- Compare independent and correlated pavement inputs.

# Final Week 2 Reflection

Answer these questions in `week_02_reflection.md`:

1. Which distribution choice was hardest to justify?
2. Which input had the greatest influence on the finance result?
3. Which input had the greatest influence on the engineering result?
4. Where did bounded distributions prevent unrealistic values?
5. How did P10 revenue differ in meaning from P80 cost?
6. How did correlation affect the construction-cost tail?
7. What additional data would provide the greatest value before either model was used professionally?
8. What did the Monte Carlo model reveal that the deterministic baseline concealed?

# Week 2 Definition of Done

Week 2 is complete when the learner can independently:

- distinguish a target from an expected value;
- distinguish a discrete variable from a continuous variable;
- define and justify bounded inputs;
- calculate a deterministic baseline;
- run a reproducible Monte Carlo simulation;
- interpret P10, P50, P80, and P90 in the correct direction;
- derive a risk-based construction contingency;
- identify leading risk drivers;
- explain the effect of input dependency; and
- communicate the result without presenting simulation as a prediction.

