# Monte Carlo Modeling Drills — Week 5 Assignment Scope

## Weekly Focus

**Sensitivity analysis and risk drivers**

Week 5 shifts the emphasis from calculating an outcome distribution to explaining **why the distribution has its shape**. The goal is to identify which uncertain inputs materially affect the decision, distinguish influential assumptions from merely uncertain assumptions, and recommend where better information or mitigation would create the most value.

## Weekly Objective

Develop the ability to:

- compare deterministic and probabilistic outcomes;
- rank input importance using Spearman rank correlation and grouped comparisons;
- distinguish uncertainty magnitude from decision impact;
- identify nonlinear and event-driven risk drivers;
- test whether sensitivity rankings remain stable;
- connect the leading drivers to a practical management action; and
- communicate sensitivity without implying causation.

## Estimated Workload

| Drill | Domain | Estimated time | Priority |
|---|---|---:|---|
| 1. Blue Ridge DCF valuation risk | Finance | 90–120 minutes | Required |
| 2. Wastewater-upgrade cost contingency | Municipal engineering | 75–90 minutes | Required |
| 3. Utility-conflict information value | Municipal engineering | 45–60 minutes | Standard |
| 4. Municipal pursuit go/no-go decision | Director/management | 45–60 minutes | Standard |

Total estimated workload is approximately **4–5.5 hours**. If time is limited, complete Drills 1 and 2 first, followed by Drill 4.

---

## Drill 1 — Finance: Blue Ridge DCF Valuation Risk

### Assignment

Develop a five-year discounted-cash-flow valuation for Blue Ridge Digital and quantify the probability that enterprise value exceeds a $3.5 million decision threshold.

### Required Workflow

1. Start in Excel with messy historical financial statements and forecast assumptions.
2. Clean inconsistent account names, mixed signs, missing periods, text-formatted amounts, and duplicated accounts.
3. Build a deterministic five-year DCF in Excel.
4. Define bounded distributions for revenue growth, EBITDA margin, working-capital investment, capital expenditures, discount rate, and terminal growth.
5. Run 20,000 reproducible Python trials.
6. Calculate valuation percentiles and probability of exceeding or falling below decision thresholds.
7. Rank value drivers using Spearman correlation and controlled input shocks.
8. Export results to a management-facing Excel dashboard.

### Required Outputs

- Deterministic enterprise value
- Mean and median simulated enterprise value
- P10, P50, and P90 enterprise value
- Probability value exceeds $3.5 million
- Probability value is below $2.5 million
- Top three valuation drivers
- Base, downside, and upside interpretation

### Deliverables

- Cleaned historical financial data and exception log
- Deterministic Excel DCF
- Assumptions register
- Python simulation notebook
- Simulation-results export
- Excel valuation-risk dashboard
- Short investment or management recommendation

---

## Drill 2 — Municipal Engineering: Wastewater-Upgrade Cost Contingency

### Assignment

Estimate the P50, P80, and P90 construction costs for a wastewater lift-station and force-main upgrade. Recommend a risk-based contingency and identify the uncertainties that should receive the most prebid attention.

### Required Workflow

1. Clean a messy bid-item estimate, historical unit-price table, escalation table, and project risk register.
2. Reconcile duplicate items, inconsistent units, allowances, percentage items, stale quotes, and risks already included in bid items.
3. Build a deterministic engineer’s estimate without an arbitrary contingency.
4. Simulate quantities, unit prices, escalation, selected change-order events, and risk-register events.
5. Run 20,000 reproducible trials.
6. Calculate cost percentiles and contingency amounts.
7. Rank drivers using Spearman correlation plus event/no-event comparisons.
8. Prepare a concise engineering decision summary.

### Required Outputs

- Deterministic base estimate
- Mean and median cost
- P50, P80, and P90 cost
- P80 contingency in dollars and percent
- Probability of exceeding the current authorized budget
- Top continuous and discrete cost drivers
- Recommended risk-reduction actions

### Deliverables

- Cleaned estimate and risk register
- Exception and double-counting log
- Deterministic cost baseline
- Python simulation notebook
- Cost distribution and sensitivity charts
- Five-sentence contingency recommendation

---

## Drill 3 — Municipal Engineering: Value of Utility-Conflict Information

### Assignment

Evaluate whether a proposed subsurface utility engineering investigation is worth its cost before final design. Compare the project-cost distribution before and after reducing utility-conflict uncertainty.

### Required Workflow

1. Clean synthetic utility-conflict records and investigation-cost data.
2. Build a deterministic expected-cost comparison for “No Investigation” and “Perform SUE.”
3. Model conflict occurrence, conflict severity, redesign cost, construction delay cost, and investigation effectiveness.
4. Run 15,000 paired trials using common random numbers where practical.
5. Compare expected cost, P80 cost, probability of a major conflict, and expected regret.
6. Test sensitivity to investigation cost and effectiveness.

### Required Outputs

- Expected and P80 total cost for both strategies
- Probability SUE produces a net financial benefit
- Expected savings after investigation cost
- Break-even SUE cost
- Break-even effectiveness
- Recommendation and nonfinancial considerations

### Deliverables

- Clean conflict-history dataset
- Deterministic strategy comparison
- Python paired-strategy simulation
- Break-even chart or table
- One-page engineering recommendation

---

## Drill 4 — Director/Management: Municipal Pursuit Go/No-Go

### Assignment

Decide whether a municipal engineering office should pursue a competitive general-engineering-services opportunity when proposal effort, win probability, fee, margin, rework, and staff opportunity cost are uncertain.

### Required Workflow

1. Clean a synthetic pursuit-history dataset.
2. Build a deterministic expected-value calculation.
3. Define three strategies: no-go, focused pursuit, and full pursuit.
4. Simulate award/no-award, proposal cost, contract fee, realized margin, scope growth, and delivery overrun.
5. Run 20,000 trials per strategy.
6. Compare expected value, downside exposure, probability of positive contribution, and staff-hour demand.
7. Identify the assumptions that would reverse the recommendation.
8. Prepare a director-level go/no-go memo.

### Required Outputs

- Expected net contribution by strategy
- Probability of losing money
- P10/P50/P90 contribution
- Expected proposal hours and opportunity cost
- Break-even win probability
- Top decision drivers
- Recommended strategy and approval conditions

### Deliverables

- Cleaned pursuit-history dataset
- Deterministic expected-value model
- Python strategy simulation
- Strategy-comparison table
- One-page director go/no-go memo

---

## Standards Applying to All Four Drills

Each drill must include:

- a stated decision question;
- raw data retained unchanged;
- documented cleaning decisions and exclusions;
- a deterministic control model;
- an assumptions table with units, source, distribution, and rationale;
- `numpy.random.default_rng(20261010)` or another documented seed;
- a stated trial count;
- at least one manually reconciled trial;
- comparison of results at two trial counts;
- sensitivity analysis appropriate to continuous and discrete inputs;
- a statement explaining that association does not prove causation;
- limitations; and
- a recommendation tied to a decision or risk-reduction action.

## Completion Checklist

- [ ] Four decision questions stated
- [ ] Raw datasets preserved
- [ ] Cleaning exceptions documented
- [ ] Deterministic baselines completed
- [ ] Distributions and bounds justified
- [ ] Random seed and trial counts documented
- [ ] At least one trial per model reconciled
- [ ] Stability checked at two trial counts
- [ ] Continuous and event risks analyzed appropriately
- [ ] Finance dashboard completed in Excel
- [ ] P80 engineering contingency calculated correctly
- [ ] Information-value break-even tested
- [ ] Pursuit recommendation includes approval conditions
- [ ] Sensitivity findings connected to actions

## Definition of Completion

Week 5 is complete when each model reproduces its deterministic control case with uncertainty disabled, produces stable decision metrics, identifies the leading risk drivers with at least two complementary methods where appropriate, and converts those findings into a defensible action or recommendation.

