# Monte Carlo Modeling Drills — Week 5 Detailed Description

## Weekly Concept

**Sensitivity analysis and risk drivers**

The first four weeks focused on constructing uncertainty models and interpreting outcome distributions. Week 5 asks the next management question:

> Which assumptions are responsible for the risk, and what can we do about them?

Sensitivity analysis is not merely a colorful tornado chart. A useful analysis distinguishes:

- inputs that vary widely but have little effect on the decision;
- inputs with modest uncertainty but strong financial or engineering leverage;
- discrete events that affect only a subset of trials but dominate the upper tail;
- inputs whose apparent importance is created by model structure or double counting; and
- assumptions that management can influence from those it must simply monitor.

Use sensitivity results to prioritize additional data, design development, negotiation, mitigation, or management attention.

## Workload

| Drill | Domain | Target time | Priority |
|---|---|---:|---|
| 1. Blue Ridge DCF valuation | Finance | 90–120 minutes | Required |
| 2. Wastewater-upgrade contingency | Municipal engineering | 75–90 minutes | Required |
| 3. Utility-conflict information value | Municipal engineering | 45–60 minutes | Standard |
| 4. Municipal pursuit go/no-go | Director/management | 45–60 minutes | Standard |

If the week becomes crowded, finish Drills 1 and 2 and complete the deterministic portion of Drill 4. Drill 3 can follow as a focused weekend exercise.

## Suggested Repository Structure

```text
week_05/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── excel/
│   └── blue_ridge_dcf_risk.xlsx
├── notebooks/
│   ├── finance_dcf_valuation.ipynb
│   ├── engineering_cost_contingency.ipynb
│   ├── engineering_sue_information_value.ipynb
│   └── director_pursuit_go_no_go.ipynb
├── outputs/
└── README.md
```

Use one notebook per drill with these sections:

1. Load and inspect
2. Clean and document exceptions
3. Deterministic baseline
4. Simulation assumptions
5. Monte Carlo model
6. Sensitivity and validation
7. Interpretation and export

---

# Drill 1 — Finance: Blue Ridge DCF Valuation Under Uncertainty

## Scenario

Blue Ridge Digital has approximately $2.4 million in annual revenue and is evaluating its long-term value before committing to a larger hiring and growth plan. Management has prepared a five-year forecast, but revenue growth, margins, working-capital needs, capital expenditures, and valuation assumptions remain uncertain.

The purpose is not to manufacture a precise company value. It is to establish a defensible valuation range and determine which assumptions deserve the most management attention.

## Decision Question

What is the distribution of enterprise value, what is the probability that value exceeds $3.5 million, and which three assumptions drive the largest changes in value?

## Part A — Messy Source Data

Create an Excel source file with three years of historical income-statement and balance-sheet drivers plus management’s five-year forecast assumptions.

Include at least these fields:

- fiscal year;
- revenue;
- cost of services;
- operating expenses;
- depreciation and amortization;
- accounts receivable;
- accounts payable;
- capital expenditures;
- tax rate;
- management revenue-growth assumption;
- target EBITDA margin; and
- forecast working-capital assumptions.

Inject realistic defects:

- `Revenue`, `Sales`, and `Net Sales` used for the same account;
- one duplicated account-year row;
- currency stored as text;
- expenses represented with mixed positive and negative conventions;
- a missing accounts-payable balance;
- one capital-expenditure value entered as a positive cash inflow;
- fiscal years stored as both dates and text;
- a percentage entered once as `18` and elsewhere as `0.18`; and
- one forecast assumption that is stale or labeled with the wrong year.

Preserve the raw data and create a cleaning-exception log.

## Part B — Start in Excel

Create `excel/blue_ridge_dcf_risk.xlsx` with:

- `Raw_Financials`
- `Clean_Financials`
- `Historical_Analysis`
- `Assumptions`
- `DCF_Baseline`
- `Simulation_Summary`
- `Sensitivity`
- `Dashboard`

### Cleaning Tasks

1. Standardize account names through a mapping table.
2. Convert amounts and percentages to consistent numeric formats.
3. Apply one accounting-sign convention.
4. Resolve the duplicate without deleting evidence from the raw sheet.
5. Estimate or flag the missing payable balance using a documented method.
6. Correct the capex sign for cash-flow calculations.
7. Confirm each fiscal year contains one value for each required account.
8. Separate historical actuals from management assumptions.

### Deterministic DCF Baseline

Build a five-year unlevered free-cash-flow model:

```text
Revenue_t = Revenue_(t−1) × (1 + Growth_t)

EBITDA_t = Revenue_t × EBITDA margin_t

EBIT_t = EBITDA_t − D&A_t

NOPAT_t = EBIT_t × (1 − Tax rate_t)

FCF_t = NOPAT_t + D&A_t − Capex_t − Change in NWC_t
```

Discount annual free cash flow using the weighted average cost of capital. Calculate terminal value using the perpetual-growth method:

```text
Terminal value = FCF_5 × (1 + g) / (WACC − g)
```

Require `WACC > terminal growth` in every deterministic and simulated case.

Use a baseline such as:

| Assumption | Base value |
|---|---:|
| Year 1–5 revenue growth | 12%, 11%, 10%, 8%, 6% |
| EBITDA margin | 18% rising to 20% |
| Tax rate | 25% |
| Capex as % of revenue | 3.0% |
| Net working capital as % of revenue | 10% |
| WACC | 14% |
| Terminal growth | 3% |

The exact deterministic enterprise value becomes the Python control result.

## Part C — Monte Carlo Assumptions

Run 20,000 trials with:

```python
rng = np.random.default_rng(20261010)
```

Use preliminary assumptions:

| Driver | Distribution | Parameters |
|---|---|---|
| Year 1 revenue growth | Beta-PERT | 4%, 12%, 20% |
| Long-run growth fade | Triangular | 3%, 6%, 9% in Year 5 |
| EBITDA margin in Year 5 | Beta-PERT | 14%, 20%, 24% |
| NWC as % of revenue | Triangular | 7%, 10%, 15% |
| Capex as % of revenue | Triangular | 2%, 3%, 5% |
| WACC | Triangular | 11%, 14%, 18% |
| Terminal growth | Triangular | 1.5%, 3%, 4.5% |

Interpolate annual revenue growth between the sampled Year 1 and Year 5 values. Interpolate EBITDA margin from the current cleaned margin to the sampled Year 5 margin.

For Week 5, use one transparent dependency rule rather than a full correlation matrix:

```text
If Year 1 growth is below 8%, reduce sampled Year 5 EBITDA margin by 1–3 percentage points.
```

Document this as a modeling judgment and rerun once without it to measure its impact.

Reject or resample any trial in which terminal growth is greater than or equal to WACC minus 1 percentage point.

## Part D — Required Results

Calculate:

- mean and median enterprise value;
- P10, P25, P50, P75, and P90 value;
- probability value exceeds $3.5 million;
- probability value falls below $2.5 million;
- probability terminal value exceeds 75% of enterprise value;
- expected terminal-value share; and
- deterministic-versus-simulated comparison.

## Sensitivity Analysis

Use at least two methods:

### Method 1 — Spearman Rank Correlation

Calculate the rank correlation between every sampled input and enterprise value. Plot the absolute correlations in descending order while retaining each sign.

### Method 2 — Controlled Input Shock

Hold all other assumptions at their deterministic values. Set each major input separately to its low and high values and record the change in enterprise value. Present the result as a tornado table or chart.

Explain why rankings may differ:

- Spearman correlation evaluates variation across the full simulation;
- the tornado test isolates one assumption at a time;
- nonlinear constraints can change the apparent importance; and
- correlation is not causation.

## Part E — Finish in Excel

Build a one-page management dashboard containing:

- deterministic enterprise value;
- P10/P50/P90 simulated value;
- probability above $3.5 million;
- probability below $2.5 million;
- enterprise-value histogram or cumulative distribution;
- top five risk-driver chart;
- terminal-value share warning;
- low/base/high controlled-sensitivity table; and
- concise management recommendation.

## Deliverables

- Cleaned financial dataset and exception log
- Deterministic five-year DCF in Excel
- Assumptions register
- Reproducible Python notebook
- Exported simulation and sensitivity summaries
- Management-facing Excel dashboard
- Five-sentence interpretation

## Quality-Control Checks

- Revenue, margins, capex, and working-capital conventions are consistent.
- WACC exceeds terminal growth in every accepted trial.
- Discount-period exponents are correct.
- Terminal value is discounted from the end of Year 5.
- Enterprise value is not mislabeled as equity value.
- With uncertainty disabled, Python reproduces the Excel valuation within a stated tolerance.
- One complete trial is manually recalculated.
- P10/P50/P90 remain reasonably stable between 5,000 and 20,000 trials.
- Sensitivity signs make economic sense.
- Terminal-value dependence is explicitly reported.

## Interpretation Questions

1. Which driver has the strongest effect on value, and is it controllable?
2. Why might WACC dominate even if its numerical range appears small?
3. What does a high terminal-value share imply about confidence in the result?
4. Why is P50 not necessarily equal to the deterministic valuation?
5. What management action could reduce valuation uncertainty?

## Brief Solution Checkpoints

- Revenue growth affects several forecast years, so small changes compound.
- WACC affects both explicit cash flows and terminal value.
- The model must never accept `g ≥ WACC`.
- A valuation distribution supports a decision range; it does not prove what a buyer will pay.

---

# Drill 2 — Municipal Engineering: Wastewater-Upgrade Cost Contingency

## Scenario

A municipality is preparing a budget for a lift-station replacement and approximately 9,000 linear feet of force main. The deterministic estimate includes civil, mechanical, electrical, controls, bypass pumping, restoration, mobilization, and allowances. Management wants a P80 funding recommendation rather than a conventional blanket percentage.

This advances Week 2's unit-cost exercise by incorporating an integrated estimate, escalation, risk-register events, and explicit sensitivity analysis.

## Decision Question

What total budget provides 80% modeled confidence, and which cost risks should the project team reduce before finalizing the capital request?

## Part A — Messy Synthetic Data

Create four source tables:

1. `bid_items_dirty.csv`
2. `historical_unit_prices_dirty.csv`
3. `escalation_indices_dirty.csv`
4. `risk_register_dirty.csv`

The bid-item estimate should total roughly $8–12 million before contingency and contain 25–35 items. Include:

- pipe, fittings, valves, lift-station equipment, electrical gear, generator, controls, bypass pumping, pavement restoration, mobilization, bonds, and testing;
- inconsistent units such as `LF`, `L.F.`, and `linear feet`;
- one duplicated bid item;
- currency and quantities stored as text;
- one percentage item treated incorrectly as quantity × unit price;
- a stale vendor quote;
- one allowance with no basis;
- inconsistent price dates; and
- one risk that is already included in a bid item.

The risk register should include probability, low/mode/high consequence, category, owner, response, and whether the risk is included elsewhere.

## Part B — Cleaning and Baseline

1. Standardize units and price dates.
2. Remove formatting characters from numeric fields.
3. Resolve the duplicate item.
4. Separate percentage-based costs from direct bid items.
5. Escalate historical prices to the estimate date.
6. Flag stale quotes for broader uncertainty.
7. Identify risk-register double counting.
8. Document allowance treatment.

Calculate:

```text
Direct cost = Sum(quantity × unit price)
Percentage items = Applicable percentage × stated cost base
Deterministic base estimate = Direct cost + percentage items + defined allowances
```

Do not add a general contingency to the baseline.

## Part C — Simulation Assumptions

Run 20,000 trials. Use item-specific or category-level assumptions rather than one multiplier on the entire project.

Suggested continuous inputs:

| Driver | Distribution |
|---|---|
| Force-main installed unit price | Beta-PERT from estimate bounds |
| Lift-station equipment cost | Triangular around vendor quote |
| Electrical equipment cost | Lognormal or bounded PERT with positive skew |
| Pavement-restoration quantity | Triangular |
| Bypass-pumping duration | Discrete weeks or bounded PERT |
| Annual escalation | Triangular or empirical resampling |
| Bid date | Discrete month or schedule scenario |

Suggested discrete risks:

- undocumented utility conflict;
- groundwater/dewatering severity;
- electrical-equipment lead-time premium;
- contaminated-soil handling;
- additional bypass-pumping period; and
- permitting condition requiring added mitigation.

Apply each discrete consequence only when its Bernoulli event occurs. Do not include a risk twice through both a bid-item range and a risk-register event unless the two components are explicitly separated.

## Part D — Required Results

Calculate:

- deterministic estimate;
- mean and median cost;
- P50, P80, and P90 cost;
- P80 contingency in dollars;
- P80 contingency as a percentage of deterministic base cost;
- probability of exceeding the currently authorized budget;
- expected cost contribution by discrete risk; and
- percent of upper-tail trials containing each discrete risk.

## Sensitivity Analysis

Use:

1. Spearman rank correlation for continuous sampled inputs.
2. Difference in mean total cost between event and no-event trials for discrete risks.
3. Difference in P80 cost between event and no-event groups for the three most important discrete risks.

Do not rank a rare binary event solely with ordinary correlation. A rare event can have a weak correlation across all trials yet dominate the extreme tail.

## Required Visuals

- Histogram with deterministic, P50, P80, and budget markers
- Cumulative distribution curve
- Continuous-input sensitivity bar chart
- Discrete-event impact table
- Optional stacked view of expected cost contribution by category

## Deliverables

- Four cleaned source tables
- Cleaning and double-counting log
- Deterministic estimate
- Python notebook and exported summary tables
- Required visuals
- Five-sentence contingency recommendation

## Quality-Control Checks

- All quantities and unit prices are nonnegative and consistently dated.
- Percentage items are applied once to the correct base.
- Duplicate bid items are not counted twice.
- Risk-event probabilities remain between zero and one.
- Risks already captured in item ranges are not counted again.
- When uncertainty and risk events are disabled, Python reproduces the baseline.
- One selected trial is fully recalculated.
- P80 is stable enough between 5,000 and 20,000 trials for the stated recommendation.
- Sensitivity results use the correct method for continuous versus binary inputs.

## Interpretation Questions

1. What does a P80 budget mean in plain language?
2. Which input drives expected cost, and which event drives the upper tail?
3. What investigation would most reduce the P80 requirement?
4. Is the largest uncertainty also the best mitigation target?
5. What risks remain outside the model?

## Brief Solution Checkpoints

- `P80 contingency = P80 total cost − deterministic base estimate`.
- P80 is a modeled confidence level, not a guarantee.
- A rare event may be invisible in a simple correlation ranking but prominent in high-cost trials.
- The recommended action should address the driver, not merely increase the contingency.

---

# Drill 3 — Municipal Engineering: Value of Utility-Conflict Information

## Scenario

A pipeline project has limited utility records along a congested corridor. A Quality Level B/A subsurface utility engineering program would cost money now but could reduce redesign, delay, and construction-conflict exposure.

## Decision Question

Should the project authorize the investigation before final design, and at what investigation cost or effectiveness would the recommendation change?

## Part A — Data and Cleaning

Generate 30–50 synthetic historical conflict records containing:

- project or corridor ID;
- utility type;
- record quality;
- conflict discovered during design or construction;
- redesign cost;
- construction change cost;
- delay days;
- daily delay cost; and
- investigation performed.

Include duplicate conflicts, inconsistent utility names, blank record-quality codes, costs stored as text, delay recorded once in weeks instead of days, and one extreme event requiring review.

## Deterministic Baseline

Compare:

```text
No Investigation expected cost
    = probability of conflict × expected conflict consequence

SUE expected cost
    = investigation cost
    + residual conflict probability × expected residual consequence
```

Use a starting SUE cost of $120,000 and document the assumed reduction in conflict probability and severity.

## Monte Carlo Model

Run 15,000 paired trials for both strategies using common underlying conflict scenarios.

Suggested inputs:

| Input | Preliminary model |
|---|---|
| Major-conflict occurrence | Bernoulli, 22% without investigation |
| Conflict construction cost | Lognormal fitted or judgment-based |
| Redesign cost | Beta-PERT |
| Delay days | Discrete or negative-binomial-style empirical sample |
| Daily delay cost | Triangular |
| Investigation effectiveness | Triangular, 45%/70%/90% reduction |
| Investigation cost | Triangular, $90k/$120k/$170k |

For the SUE strategy, reduce conflict probability and, if a conflict remains, reduce consequence severity using the sampled effectiveness assumption. Clearly document whether one effectiveness factor affects probability, severity, or both.

## Required Results

- mean and P80 total cost for both strategies;
- probability SUE has the lower cost in a paired trial;
- expected net savings after investigation cost;
- P80 risk reduction;
- break-even investigation cost;
- break-even effectiveness; and
- expected regret of selecting each strategy.

## Sensitivity Tasks

1. Sweep investigation cost from $50,000 to $250,000.
2. Sweep effectiveness from 30% to 95%.
3. Build a two-dimensional break-even table.
4. Identify where the recommendation switches.

## Deliverables

- Cleaned conflict dataset and exception log
- Deterministic expected-cost comparison
- Paired Python simulation
- Break-even chart or table
- One-page recommendation

## Quality-Control Checks

- Delay units are consistent.
- Conflict costs are not counted twice.
- Both strategies use the same underlying paired conflict draw.
- SUE cost is incurred in every SUE trial.
- Effectiveness remains between 0% and 100%.
- Setting effectiveness to zero leaves only the added investigation cost.
- Setting investigation cost to zero cannot make SUE financially worse under otherwise identical assumptions.

## Interpretation Questions

1. Does SUE need to save money on average to be justified?
2. How should schedule reliability and public disruption influence the decision?
3. Which is more uncertain: conflict probability or consequence?
4. What evidence would improve the effectiveness assumption?

## Brief Solution Checkpoints

- Information has value only if it can change design, construction planning, or the decision.
- Expected savings and tail-risk reduction answer different questions.
- Common random numbers make the strategy comparison less noisy.
- A break-even result is often more useful than one assumed point estimate.

---

# Drill 4 — Director/Management: Municipal Pursuit Go/No-Go

## Scenario

A municipal engineering office is considering a competitive general-engineering-services pursuit. The contract could strengthen a strategic client relationship and generate future task orders, but proposal effort will consume scarce senior staff time during an already busy delivery period.

The director must recommend no-go, focused pursuit, or full pursuit.

## Decision Question

Which pursuit strategy provides the best risk-adjusted contribution, and what win probability, fee, or margin assumptions would reverse the recommendation?

## Part A — Messy Pursuit History

Create a synthetic dataset of 25–40 prior public-sector pursuits containing:

- client and market;
- pursuit type;
- estimated and actual proposal hours;
- direct pursuit expense;
- shortlisted status;
- win/loss;
- anticipated fee;
- realized fee;
- planned margin;
- realized margin;
- strategic-client score; and
- delivery-overrun indicator.

Include inconsistent win/loss labels, missing actual hours, fee stored as text, duplicated pursuit ID, mixed margin formats, an abandoned pursuit labeled as a loss, and one very large contract that should not be deleted automatically.

## Part B — Deterministic Strategies

Develop three strategies:

| Strategy | Proposal effort | Preliminary win probability | Purpose |
|---|---:|---:|---|
| No-go | 0 hours | 0% | Protect delivery capacity |
| Focused pursuit | 120 hours | 22% | Targeted team and interview preparation |
| Full pursuit | 240 hours | 32% | Expanded capture, proposal, and interview effort |

Use a preliminary anticipated fee of $450,000, target operating margin of 18%, and loaded internal pursuit cost of $125/hour. Add a documented opportunity cost for senior hours displaced from billable work.

Calculate deterministic expected net contribution:

```text
Expected contribution
    = Win probability × expected delivery contribution
    − pursuit labor cost
    − direct pursuit expense
    − opportunity cost
```

Keep strategic value visible but separate from the financial calculation unless a transparent scoring method is used.

## Part C — Simulation

Run 20,000 trials per strategy.

Suggested inputs:

| Driver | Distribution |
|---|---|
| Win/loss | Bernoulli by strategy |
| Proposal hours | Triangular around strategy estimate |
| Contract fee if won | Beta-PERT, $300k/$450k/$750k |
| Realized margin | Triangular, 8%/18%/24% |
| Delivery overrun event | Bernoulli |
| Overrun consequence | Discrete margin reduction |
| Follow-on task-order value | Zero-inflated discrete outcome |
| Opportunity cost per hour | Triangular |

Conditional logic:

1. Delivery contribution and follow-on work occur only if the pursuit is won.
2. Proposal cost occurs whether the pursuit is won or lost.
3. Delivery overrun can occur only after a win.
4. Follow-on value should be discounted and probability-weighted.
5. No-go has zero pursuit cost and zero direct award contribution but may include a separately stated strategic cost.

## Required Results

- expected net contribution by strategy;
- P10, P50, and P90 contribution;
- probability of negative contribution;
- expected proposal hours and opportunity cost;
- probability of winning but still producing a negative contribution;
- break-even win probability;
- break-even target margin; and
- top three decision drivers.

## Sensitivity Analysis

1. Calculate rank correlations within awarded trials for fee, margin, and overrun variables.
2. Sweep win probability from 5% to 60%.
3. Sweep target margin from 5% to 25%.
4. Compare focused and full pursuit on a win-probability-versus-effort grid.

## Director Memo

Prepare a one-page memo stating:

1. recommendation;
2. expected benefit and downside exposure;
3. assumptions that must be true for approval;
4. delivery-capacity safeguards;
5. client/strategic considerations not captured financially; and
6. the next approval or coordination action.

## Deliverables

- Cleaned pursuit-history data and exception log
- Deterministic expected-value comparison
- Python strategy simulation
- Sensitivity and break-even tables
- One-page director go/no-go memo

## Quality-Control Checks

- Proposal costs occur in win and loss trials.
- Delivery contribution occurs only in win trials.
- Margin is applied to fee, not added as a separate dollar value.
- Abandoned pursuits are classified separately from competitive losses.
- No-go remains a valid comparison, not a missing value.
- Break-even win probability is checked analytically against the simulation.
- Staff-hour assumptions do not exceed stated capacity without an explicit consequence.
- Strategic value is not disguised as precise financial value.

## Interpretation Questions

1. When is a positive expected value insufficient to justify a pursuit?
2. How should current project-delivery risk affect the go/no-go decision?
3. Does full pursuit create enough additional win probability to justify its effort?
4. Which assumption would you challenge most in a leadership meeting?
5. What nonfinancial strategic benefit belongs in the final recommendation?

## Brief Solution Checkpoints

- A high-fee opportunity can still have poor expected value if win probability or margin is low.
- Proposal effort is spent in every pursuit outcome.
- Winning is not the same as creating value; delivery overruns can erase contribution.
- The final recommendation should include conditions and capacity safeguards, not merely “go” or “no-go.”

---

# Week 5 Completion Checklist

- [ ] Raw source data retained for all four drills
- [ ] Cleaning and exclusion decisions documented
- [ ] Deterministic baselines completed before simulation
- [ ] Distribution choices and bounds justified
- [ ] Random seed and trial count recorded
- [ ] One trial from each model manually reconciled
- [ ] Trial-count stability checked
- [ ] Continuous drivers assessed with rank correlation
- [ ] Discrete events assessed with event/no-event comparisons
- [ ] At least one controlled sensitivity or break-even analysis completed per drill
- [ ] Finance results returned to an Excel dashboard
- [ ] Engineering contingency stated at P50/P80/P90
- [ ] Recommendations name specific risk-reduction actions
- [ ] Limitations and excluded uncertainties stated

# End-of-Week Reflection

Answer briefly:

1. Which model had the most stable sensitivity ranking?
2. Which rare event mattered more than its correlation suggested?
3. Which leading driver was controllable?
4. Where did a break-even analysis communicate more than a single forecast?
5. What additional data would most improve next week's decision?

