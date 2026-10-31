# Monte Carlo Modeling Drills — Week 6 Assignment Scope

## Weekly Focus

**Dependencies and correlation**

Week 6 examines two relationships that are often confused:

- **Dependency:** one event or activity must occur before another can begin.
- **Correlation:** uncertain variables tend to move together, even when neither directly causes the other.

The objective is to preserve realistic relationships without counting the same risk twice or creating unjustified precision.

## Weekly Objectives

Develop the ability to:

- distinguish logical dependencies from statistical correlation;
- build and validate a precedence network;
- generate correlated random variables reproducibly;
- document the evidence or judgment supporting a correlation assumption;
- compare correlated and independent models;
- identify double counting between shared drivers and individual inputs;
- evaluate alternative strategies using common scenarios; and
- explain how relationships among inputs change the tails of an outcome distribution.

## Estimated Workload

| Drill | Domain | Estimated time | Priority |
|---|---|---:|---|
| 1. Blue Ridge hiring strategy | Finance | 90–120 minutes | Required |
| 2. Municipal project schedule risk | Municipal engineering | 75–90 minutes | Required |
| 3. HDD construction-duration risk | Municipal engineering | 45–60 minutes | Standard |
| 4. Project delivery-strategy decision | Director/management | 45–60 minutes | Standard |

Total estimated workload is approximately **4–5.5 hours**. If time is limited, complete Drills 1 and 2 first, followed by Drill 4.

---

## Drill 1 — Finance: Blue Ridge Hiring Strategy

### Assignment

Compare immediate, staged, and delayed hiring strategies for four proposed employees. Model the relationships among sales growth, billable utilization, billing rates, compensation, collections, and hiring ramp-up.

### Required Workflow

1. Start in Excel with messy historical revenue, payroll, utilization, billing-rate, and collections data.
2. Clean inconsistent employee names, duplicate payroll records, missing utilization, mixed percentages, and misaligned monthly periods.
3. Build a deterministic 24-month incremental hiring model.
4. Define three hiring strategies.
5. Specify and justify a correlation structure for major business drivers.
6. Run 20,000 reproducible Python simulations.
7. Compare correlated and independent versions of the model.
8. Export results to a management-facing Excel dashboard.

### Required Strategies

- **Immediate:** hire all four employees in Month 1.
- **Staged:** hire two in Month 1 and two in Month 7.
- **Delayed:** hire all four in Month 7.

### Required Outputs

- Expected and P10/P50/P90 incremental cash contribution
- Probability of positive incremental NPV
- Probability cash falls below the required reserve
- Peak borrowing requirement
- Probability each strategy outperforms the others
- Effect of preserving versus removing correlation
- Recommended hiring strategy and decision triggers

### Deliverables

- Cleaned operating dataset and exception log
- Deterministic Excel hiring model
- Correlation assumptions register
- Python simulation notebook
- Strategy-comparison export
- Excel hiring-risk dashboard
- Short management recommendation

---

## Drill 2 — Municipal Engineering: Project Schedule Risk

### Assignment

Develop a Monte Carlo schedule for a lift-station and force-main project from 30% design through startup. Include activity precedence, permitting dependencies, procurement, weather exposure, and selected shared delay drivers.

### Required Workflow

1. Clean a messy activity register, milestone list, and historical-duration table.
2. Resolve duplicate IDs, missing predecessors, circular logic, inconsistent duration units, and incomplete milestones.
3. Build and validate a deterministic critical-path schedule.
4. Assign bounded activity-duration distributions.
5. Add common permitting, review, procurement, and weather drivers without double counting.
6. Run 20,000 schedule trials.
7. Recalculate the critical path for every trial.
8. Estimate milestone reliability and activity criticality.

### Required Outputs

- Deterministic completion date
- P50, P80, and P90 completion dates
- Probability of meeting the contractual deadline
- Milestone-specific on-time probabilities
- Activity criticality index
- Schedule sensitivity and shared-driver effects
- Recommended schedule contingency and mitigation actions

### Deliverables

- Cleaned activity and milestone tables
- Network-validation log
- Deterministic schedule baseline
- Python schedule simulation
- Completion-date and criticality visuals
- Brief schedule-risk memo

---

## Drill 3 — Municipal Engineering: HDD Construction-Duration Risk

### Assignment

Estimate the probability that a 1,200-foot horizontal directional drilling crossing can be completed within a 28-calendar-day work window. Model dependencies among subsurface conditions, production rates, weather, drilling-fluid losses, and reaming requirements.

### Required Workflow

1. Clean synthetic daily production, geotechnical, weather, and drilling-event data.
2. Build a deterministic production schedule.
3. Define correlated ground-condition and production assumptions.
4. Model discrete events such as loss of returns and additional reaming passes.
5. Run 15,000 construction trials.
6. Compare independent and dependent models.

### Required Outputs

- P50/P80/P90 duration
- Probability of completing within 28 days
- Expected lost-work days
- Probability of a major drilling event
- Dominant duration drivers
- Recommended schedule allowance and field controls

### Deliverables

- Cleaned HDD dataset
- Deterministic duration model
- Python simulation notebook
- Independent-versus-dependent comparison
- One-page construction-risk summary

---

## Drill 4 — Director/Management: Project Delivery Strategy

### Assignment

Compare design-bid-build, accelerated design-bid-build, and progressive design-build for a municipal pump-station program. Evaluate completion reliability, management effort, change exposure, and cost growth.

### Required Workflow

1. Clean a synthetic history of municipal projects and delivery outcomes.
2. Build deterministic time and management-cost baselines for three strategies.
3. Model correlated design completeness, review duration, procurement time, change orders, and construction duration.
4. Run 20,000 paired trials using common market and permitting scenarios.
5. Compare schedule, cost, and management exposure.
6. Identify the assumptions that reverse the preferred strategy.
7. Prepare a director-level recommendation.

### Required Outputs

- Expected and P80 completion time
- Probability of meeting the required in-service date
- Expected and P80 total delivery cost
- Probability cost growth exceeds 10%
- Expected owner and consultant management hours
- Break-even time value for acceleration
- Recommended strategy and governance conditions

### Deliverables

- Cleaned project-history dataset
- Three deterministic strategy baselines
- Python paired-strategy simulation
- Time/cost comparison table
- One-page director decision memo

---

## Standards Applying to All Four Drills

Each drill must include:

- a clear decision question;
- raw data retained unchanged;
- documented cleaning and exclusion decisions;
- a deterministic baseline;
- an assumptions table with units, source, distribution, and rationale;
- a dependency map or precedence description;
- a documented correlation matrix or common-driver approach;
- `numpy.random.default_rng(20261017)` or another documented seed;
- a stated trial count;
- at least one manually reconciled trial;
- comparison of independent and dependent models;
- validation that the correlation matrix is positive semidefinite when applicable;
- a convergence or stability check;
- limitations; and
- a recommendation tied to a practical action.

## Completion Checklist

- [ ] Four decision questions stated
- [ ] Raw datasets preserved
- [ ] Cleaning exceptions documented
- [ ] Deterministic baselines completed
- [ ] Dependencies separated from correlations
- [ ] Correlation assumptions justified
- [ ] Double counting checked
- [ ] Random seed and trial counts recorded
- [ ] At least one trial per drill reconciled
- [ ] Independent-versus-dependent comparison completed
- [ ] Finance dashboard completed in Excel
- [ ] Schedule criticality indices calculated
- [ ] Strategy recommendation includes decision triggers
- [ ] Limitations and excluded relationships stated

## Definition of Completion

Week 6 is complete when each model reproduces its deterministic baseline with uncertainty disabled, preserves the intended logical and statistical relationships, demonstrates how those relationships change the outcome distribution, and produces a defensible decision recommendation.

