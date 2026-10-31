# Monte Carlo Modeling Drills — Week 6 Detailed Description

## Weekly Concept

**Dependencies and correlation**

Monte Carlo models become misleading when related variables are sampled as though they were independent. They also become misleading when correlation is used as a substitute for actual process logic.

This week distinguishes:

- **Precedence dependency:** construction cannot begin before design, permitting, and procurement requirements are satisfied.
- **Conditional dependency:** delivery contribution exists only if a pursuit is won or an employee becomes productive.
- **Shared-driver dependence:** the same market condition may increase labor cost, equipment price, and delivery time.
- **Statistical correlation:** two sampled variables tend to move together across trials.

The main lesson is:

> Model the process with logic first. Add correlation only where it represents a remaining relationship that the logic does not already capture.

## Workload

| Drill | Domain | Target time | Priority |
|---|---|---:|---|
| 1. Blue Ridge hiring strategy | Finance | 90–120 minutes | Required |
| 2. Municipal project schedule risk | Municipal engineering | 75–90 minutes | Required |
| 3. HDD construction duration | Municipal engineering | 45–60 minutes | Standard |
| 4. Project delivery strategy | Director/management | 45–60 minutes | Standard |

## Suggested Repository Structure

```text
week_06/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── excel/
│   └── blue_ridge_hiring_risk.xlsx
├── notebooks/
│   ├── finance_hiring_strategy.ipynb
│   ├── engineering_schedule_risk.ipynb
│   ├── engineering_hdd_duration.ipynb
│   └── director_delivery_strategy.ipynb
├── outputs/
└── README.md
```

Use one notebook per drill with sections for ingestion, cleaning, baseline, assumptions, simulation, validation, evaluation, and interpretation.

---

# Drill 1 — Finance: Blue Ridge Hiring Strategy Under Correlated Uncertainty

## Scenario

Blue Ridge Digital wants to add four employees to support projected growth. Revenue demand, billable utilization, billing rates, compensation, and collection timing are related. Stronger demand generally raises utilization and may support higher rates, but rapid growth can also lengthen collections and increase working-capital pressure.

Management must compare three strategies over 24 months:

- hire four employees immediately;
- hire two immediately and two after six months; or
- delay all four hires for six months.

## Decision Question

Which strategy provides the best balance of incremental value, cash protection, and growth capacity when major operating drivers are correlated?

## Part A — Messy Source Data

Create an Excel source package containing 24–36 months of:

- monthly revenue;
- invoiced amount;
- cash collections;
- days sales outstanding;
- billable hours;
- available hours;
- utilization;
- average billing rate;
- payroll by employee;
- employee role and start date; and
- operating expenses.

Inject realistic defects:

- employee names written several ways;
- a duplicated payroll record;
- utilization stored as both `78%` and `0.78`;
- one month with missing available hours;
- invoice and collection months that are misaligned;
- currency stored as text;
- a terminated employee retained in a later payroll period;
- one billing-rate outlier caused by an incorrect decimal; and
- month-end dates mixed with month-start dates.

Preserve raw data and create an exception log.

## Part B — Start in Excel

Create `excel/blue_ridge_hiring_risk.xlsx` with:

- `Raw_Operations`
- `Raw_Payroll`
- `Clean_Operations`
- `Clean_Payroll`
- `Assumptions`
- `Correlation`
- `Baseline_Immediate`
- `Baseline_Staged`
- `Baseline_Delayed`
- `Simulation_Summary`
- `Dashboard`

### Deterministic Model

For each strategy, calculate 24 monthly periods:

```text
Billable hours = Available hours × Utilization

Revenue = Billable hours × Average billing rate

Gross contribution = Revenue − Direct compensation − Variable delivery cost

Operating cash contribution
    = Cash collections − Payroll − Other incremental cash costs
```

Include:

- salary and payroll burden;
- recruiting cost;
- equipment/software onboarding cost;
- a three-month utilization ramp;
- collection lag;
- beginning unrestricted cash; and
- a required cash reserve.

Calculate incremental NPV using a monthly discount rate consistent with the stated annual rate.

## Part C — Correlated Simulation Inputs

Run 20,000 trials with:

```python
rng = np.random.default_rng(20261017)
```

Use bounded marginal distributions and a latent Gaussian correlation approach. Generate correlated standard normal draws, convert them to uniform percentiles using the normal CDF, and transform the percentiles through the inverse CDFs of the selected marginal distributions.

Use a preliminary correlation matrix such as:

| Driver | Demand growth | Utilization | Billing-rate growth | Wage growth | DSO pressure |
|---|---:|---:|---:|---:|---:|
| Demand growth | 1.00 | 0.65 | 0.40 | 0.20 | 0.35 |
| Utilization | 0.65 | 1.00 | 0.25 | 0.10 | 0.20 |
| Billing-rate growth | 0.40 | 0.25 | 1.00 | 0.45 | 0.10 |
| Wage growth | 0.20 | 0.10 | 0.45 | 1.00 | 0.05 |
| DSO pressure | 0.35 | 0.20 | 0.10 | 0.05 | 1.00 |

Treat this as a learning assumption, not empirical truth. Confirm the matrix is positive semidefinite before sampling.

Suggested marginal distributions:

| Driver | Distribution |
|---|---|
| Annual demand growth | Beta-PERT: 0%, 12%, 25% |
| Mature utilization | Beta-PERT: 65%, 78%, 88% |
| Billing-rate growth | Triangular: 0%, 4%, 8% |
| Wage growth | Triangular: 2%, 5%, 9% |
| DSO increase during high growth | Triangular: 0, 7, 20 days |
| Recruiting delay per hire | Discrete: 0, 1, 2, or 3 months |
| Ramp duration | Discrete: 2, 3, 4, or 6 months |

Do not correlate recruiting delay merely because other variables are correlated. Add a relationship only when there is a defensible mechanism.

## Part D — Simulation Logic

For each trial and strategy:

1. Sample correlated business drivers.
2. Sample recruiting and ramp timing.
3. Calculate monthly capacity and billable hours.
4. Limit revenue to available demand; do not create work merely because staff capacity exists.
5. Calculate invoice revenue and cash collections separately.
6. Pay compensation after each actual start date.
7. Calculate monthly incremental cash and discounted cash flow.
8. Store minimum cash, borrowing need, incremental NPV, and unmet demand.

Use the same underlying economic scenario for all three strategies within a trial. This makes the strategy comparison paired and reduces simulation noise.

## Required Results

- expected and P10/P50/P90 incremental NPV;
- probability of positive incremental NPV;
- probability cash falls below the required reserve;
- P50 and P90 peak borrowing need;
- expected unmet demand or forgone revenue;
- probability each strategy produces the highest NPV; and
- probability immediate hiring produces both higher NPV and a cash-reserve breach.

## Independent-versus-Correlated Comparison

Rerun the model with all off-diagonal correlations set to zero. Compare:

- P10 incremental NPV;
- probability of reserve breach;
- P90 borrowing need; and
- strategy ranking.

Explain why positive correlation between demand and utilization may increase upside, while positive correlation between growth and DSO pressure can intensify cash risk.

## Finish in Excel

Build a management dashboard showing:

- deterministic NPV by strategy;
- P10/P50/P90 NPV by strategy;
- probability of positive NPV;
- probability of reserve breach;
- P90 borrowing need;
- expected forgone revenue;
- correlated-versus-independent comparison; and
- recommended strategy with hiring triggers.

## Quality-Control Checks

- Percentages and monthly periods are consistent.
- Strategy capacity changes only after actual hire dates.
- Revenue cannot exceed modeled demand.
- Payroll begins only after an employee starts.
- Collections are not treated as contemporaneous revenue.
- The correlation matrix is symmetric with ones on the diagonal and nonnegative eigenvalues within numerical tolerance.
- Achieved sample rank correlations are compared with targets.
- With uncertainty disabled, Python reproduces each Excel baseline.
- One trial is reconciled month by month.
- Results are compared at 5,000 and 20,000 trials.

## Interpretation Questions

1. Which correlations materially change downside risk?
2. Why can strong growth worsen cash risk?
3. Does staged hiring reduce risk by sacrificing value or by matching capacity to demand?
4. Which correlation assumption is least defensible?
5. What observable trigger should authorize the second hiring stage?

## Brief Solution Checkpoints

- Capacity is not revenue unless demand exists and staff become productive.
- Profit and cash must be modeled separately.
- Common scenarios are essential for a fair strategy comparison.
- Correlation may change tail risk without materially changing the mean.

---

# Drill 2 — Municipal Engineering: Integrated Project Schedule Risk

## Scenario

A municipality must complete a lift-station and force-main project from 30% design through startup. The schedule includes survey/SUE, geotechnical work, design, agency review, property coordination, equipment procurement, construction, testing, and startup.

The contractual in-service date is important, but the baseline schedule contains limited float. Agency comments, equipment lead times, and weather can affect several activities at once.

## Decision Question

What is the probability of meeting the in-service date, what completion date corresponds to P80 confidence, and which activities or shared drivers dominate schedule uncertainty?

## Part A — Messy Activity Data

Create 25–35 activities with:

- activity ID;
- description;
- phase;
- predecessor IDs;
- relationship type;
- deterministic duration;
- low/mode/high duration;
- responsible discipline;
- milestone flag; and
- calendar type.

Inject:

- duplicate activity IDs;
- one missing predecessor;
- one circular dependency;
- durations stored in days and weeks;
- inconsistent relationship labels;
- a milestone with nonzero duration;
- an activity marked complete but still listed as a successor constraint; and
- a summary activity incorrectly included in the calculation.

## Part B — Deterministic Baseline

Clean and validate the network before simulation. Calculate early start, early finish, late start, late finish, total float, and the deterministic critical path.

The network must include at least:

- 30% review and comment resolution;
- survey/SUE and geotechnical completion;
- 60% design;
- environmental and utility permit preparation;
- agency reviews;
- property/easement coordination;
- 90% and final design;
- bidding/award;
- long-lead equipment submittal and fabrication;
- site construction;
- force-main construction;
- electrical/I&C completion;
- testing and startup; and
- final in-service milestone.

## Part C — Uncertainty and Shared Drivers

Assign beta-PERT durations to selected activities. Use explicit shared drivers for:

- owner/agency review intensity;
- permitting complexity;
- electrical-equipment market conditions;
- wet-weather severity; and
- design rework.

Example shared-driver method:

```text
Sample one permitting-complexity percentile per trial.
Use that percentile to influence each related permit-review activity.
```

Do not independently apply a full permitting-delay distribution to three activities and then add another global permitting delay unless those represent distinct risks.

Use a small correlation structure only for remaining relationships not already captured by shared drivers—for example, site construction and force-main productivity during wet weather.

## Part D — Simulation

Run 20,000 trials. For each trial:

1. Sample shared drivers.
2. Sample activity durations conditionally or through correlated percentiles.
3. calculate the precedence network;
4. determine project completion;
5. identify the controlling path; and
6. record milestone dates and critical activities.

## Required Results

- P10/P50/P80/P90 completion dates;
- probability of meeting the contractual in-service date;
- probability of meeting each design and permit milestone;
- activity criticality index;
- correlation between activity duration and project completion;
- frequency of each major critical-path family; and
- schedule contingency between the deterministic and P80 dates.

## Alternative Comparison

Compare the baseline plan with one mitigation strategy:

- early equipment procurement;
- overlapping selected permit preparation with 60% design;
- additional survey/SUE resources; or
- owner review workshops before formal submittals.

Only overlap activities when the logic is defensible. Record the potential rework introduced by acceleration.

## Quality-Control Checks

- The network is acyclic.
- All predecessors exist.
- Milestones have zero duration.
- Summary activities are excluded from calculations.
- One deterministic forward/backward pass is manually checked.
- One simulated trial is reconciled activity by activity.
- No activity starts before its predecessors and relationship lags permit.
- Achieved correlations are checked.
- Shared risks are not double counted.
- P80 completion stabilizes between 5,000 and 20,000 trials.

## Interpretation Questions

1. Is the deterministic critical path also the most frequent simulated critical path?
2. Which shared driver affects the most downstream activities?
3. What is the difference between activity criticality and duration sensitivity?
4. Does acceleration reduce deadline risk or exchange it for rework risk?
5. What date should be communicated as the management commitment?

## Brief Solution Checkpoints

- The critical path can change across trials.
- A frequently critical activity is not automatically the best mitigation target.
- Schedule contingency is the difference between dates, not a percentage added to every activity.
- Logic errors cannot be cured by more simulations.

---

# Drill 3 — Municipal Engineering: HDD Construction-Duration Risk

## Scenario

A 1,200-foot HDD crossing must be completed during a 28-calendar-day environmental work window. The planned sequence includes mobilization, pilot bore, prereaming passes, pullback, testing, and demobilization.

Production depends on ground conditions. Difficult material can reduce penetration, increase reaming requirements, and increase the probability of drilling-fluid losses. Wet weather can also reduce productive work time.

## Decision Question

What is the probability of completing the crossing within 28 days, and what schedule allowance or field controls are justified?

## Part A — Messy Synthetic Data

Generate 40–60 daily records containing:

- date;
- HDD phase;
- footage advanced;
- productive hours;
- ground-condition class;
- rainfall;
- drilling-fluid loss indicator;
- reaming pass; and
- downtime reason.

Include duplicate dates, footage stored as text, missing productive hours, inconsistent ground-condition labels, rainfall in inches and millimeters, a negative production value, and a day assigned to two phases.

## Deterministic Baseline

Create a sequence using planned production rates and fixed durations:

- mobilization: 3 days;
- pilot bore: footage divided by planned pilot production;
- prereaming: required passes and production by pass;
- pullback: 1–2 days;
- testing/demobilization: 3 days.

Report deterministic duration and float to the work-window deadline.

## Monte Carlo Model

Run 15,000 trials. Model:

- ground-condition mix;
- pilot and reaming production rates;
- productive hours per workable day;
- wet-weather lost days;
- loss-of-returns event;
- additional reaming pass; and
- event-specific recovery duration.

Represent ground conditions as a shared driver that influences production and event probabilities. Do not independently sample “hard ground,” low production, and additional reaming as unrelated events if hard ground is the reason for both.

Compare:

- **Model A:** inputs sampled independently;
- **Model B:** ground-condition driver links production and event likelihood.

## Required Results

- mean and P50/P80/P90 duration;
- probability of completing within 28 days;
- expected weather downtime;
- probability and expected impact of loss of returns;
- probability of an additional reaming pass; and
- top duration drivers.

## Quality-Control Checks

- Phase footage totals reconcile to 1,200 feet where applicable.
- Units are consistent.
- Production is positive on productive days.
- Discrete-event recovery time is added only when the event occurs.
- Phase precedence is preserved.
- One full trial is manually checked.
- Dependent-model event frequencies are reviewed by ground-condition class.
- P80 duration is checked for convergence.

## Interpretation Questions

1. How does dependency change the upper duration tail?
2. Which uncertainty can field investigation reduce?
3. Is average production an adequate schedule basis?
4. What action protects the environmental work window most effectively?

## Brief Solution Checkpoints

- Adverse ground conditions should affect both productivity and event likelihood.
- The dependent model will often create a heavier upper tail than the independent model.
- Schedule allowance should reflect a stated confidence level, not an arbitrary percentage.

---

# Drill 4 — Director/Management: Municipal Project Delivery Strategy

## Scenario

A municipal utility must deliver a pump-station program by a regulatory in-service date. Leadership is considering:

- traditional design-bid-build;
- accelerated design-bid-build with early equipment procurement; or
- progressive design-build.

Each strategy changes design overlap, owner involvement, price certainty, procurement timing, change exposure, and management effort.

## Decision Question

Which strategy best balances deadline reliability, total delivery cost, owner capacity, and change risk?

## Part A — Messy Project-History Data

Create 20–30 synthetic municipal projects containing:

- delivery method;
- design duration;
- procurement duration;
- construction duration;
- planned and actual cost;
- design completeness at pricing;
- change-order percentage;
- owner management hours;
- consultant management hours;
- regulatory deadline status; and
- market condition.

Include inconsistent delivery-method names, mixed duration units, missing management hours, duplicate project IDs, cost growth recorded as both dollars and percentages, and one extreme project that requires investigation rather than deletion.

## Deterministic Baselines

Create one time/cost baseline for each strategy. Explicitly show:

- which phases overlap;
- when major equipment is procured;
- when price is established;
- owner and consultant management effort; and
- assumed change allowance.

## Simulation Assumptions

Run 20,000 paired trials. Use the same market, permitting, and site scenarios for all strategies within each trial.

Model:

- permitting/review duration;
- design productivity;
- equipment lead time;
- construction duration;
- price escalation;
- design completeness at pricing;
- change-order frequency and magnitude; and
- owner/consultant management effort.

Use dependencies such as:

```text
Lower design completeness at pricing
    → higher change-order probability
    → potentially longer construction duration
```

Use correlation where a shared market condition affects equipment price, equipment lead time, and contractor pricing.

## Required Results

- expected and P80 total duration;
- probability of meeting the in-service date;
- expected and P80 total delivery cost;
- probability of cost growth exceeding 10%;
- expected owner and consultant management hours;
- probability each strategy is fastest and least costly; and
- break-even value per month of earlier service.

## Decision Analysis

Compare strategies without collapsing everything immediately into one score. Present:

1. schedule reliability;
2. cost distribution;
3. management-capacity demand;
4. change exposure;
5. procurement and governance requirements; and
6. assumptions that could reverse the recommendation.

## Director Memo

Prepare a one-page memo with:

- recommended strategy;
- time and cost evidence;
- owner-capacity implications;
- primary dependencies and correlations;
- governance conditions required for success;
- procurement/legal considerations requiring specialist review; and
- next decision milestone.

## Quality-Control Checks

- Common external scenarios are reused across strategies.
- Phase overlap follows the stated delivery method.
- Change events depend on design completeness as defined.
- Early procurement cost occurs only in applicable strategies.
- Management hours are counted once.
- Total cost components reconcile.
- No-go or baseline strategy remains a valid comparator.
- One paired trial is manually reconciled.

## Interpretation Questions

1. Which strategy is most reliable rather than merely fastest on average?
2. What owner capabilities are required for the preferred method?
3. How does early price commitment affect change risk?
4. What is the financial value of one month of schedule acceleration?
5. Which conclusion is most sensitive to uncertain correlation assumptions?

## Brief Solution Checkpoints

- Faster average delivery does not guarantee higher deadline reliability.
- Strategy selection changes the dependency structure, not just activity durations.
- Common scenarios enable a fair paired comparison.
- The recommendation should include governance conditions, not merely a delivery-method label.

---

# Week 6 Completion Checklist

- [ ] Raw data preserved for all four drills
- [ ] Cleaning and exclusion decisions documented
- [ ] Deterministic baselines completed
- [ ] Dependency logic mapped before simulation
- [ ] Correlation assumptions documented and justified
- [ ] Correlation matrices validated where used
- [ ] Shared drivers separated from residual correlation
- [ ] Double counting reviewed
- [ ] Random seed and trial counts documented
- [ ] One trial per model manually reconciled
- [ ] Independent-versus-dependent results compared
- [ ] Stability checked at two trial counts
- [ ] Finance results returned to an Excel dashboard
- [ ] Management recommendations identify decision triggers or governance conditions
- [ ] Limitations stated

# End-of-Week Reflection

Answer briefly:

1. Which relationship had the largest effect on tail risk?
2. Where was a logical dependency more appropriate than correlation?
3. Which correlation assumption was hardest to defend?
4. Where did independent sampling understate or overstate risk?
5. What additional data would most improve the dependency model?

