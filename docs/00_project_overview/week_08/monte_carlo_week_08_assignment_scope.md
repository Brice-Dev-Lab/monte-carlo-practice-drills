# Week 8 Monte Carlo Modeling Drills — Assignment Scope

## Weekly theme

**Event timing and survival concepts**

Week 8 shifts the simulation question from “what value will occur?” to “when will an event occur?” You will model time to refinancing stress, asset failure, service interruption, and capital intervention. The emphasis is on survival probability, hazard, censoring, conditional events, and the distinction between annual risk and cumulative risk over a planning horizon.

**Recommended workload:** 4.5–5.5 hours  
**Primary random seed:** `20261031`

## Learning objectives

By the end of the week, you should be able to:

- distinguish survival probability, cumulative failure probability, and hazard;
- recognize right-censored observations in finance and engineering records;
- estimate or justify time-to-event distributions;
- simulate event timing and conditional consequences;
- compare deterministic planning dates with probabilistic timing;
- validate simulated event rates against observed or assumed behavior; and
- communicate when intervention is needed, not merely whether risk exists.

## Drill schedule

| Drill | Application | Suggested time | Decision question |
|---|---|---:|---|
| 1 | Finance — debt and refinancing risk | 90 minutes | How early should management begin refinancing, and how much liquidity is needed? |
| 2 | Municipal engineering — water-main failure timing | 75 minutes | Which assets should be renewed before the next failure? |
| 3 | Municipal engineering — pump-fleet reliability | 60 minutes | Are the spare-pump and maintenance strategies sufficient? |
| 4 | Director/management — renewal budget and service risk | 75 minutes | Which capital strategy best limits failures within the available budget? |

---

## Drill 1 — Debt maturity and refinancing risk

### Assignment

Evaluate a small engineering firm's five-year term loan with a balloon balance due in 24 months. Model the timing of covenant stress, the refinancing process, interest-rate conditions, operating cash flow, lender approval, and closing delays. Start in Excel, simulate in Python, and finish with a management-facing Excel dashboard.

### Required workflow

1. Clean monthly financial history and the loan schedule in Excel.
2. Build a deterministic 24-month debt-service and covenant baseline.
3. In Python, run at least **20,000 monthly paths** using seed `20261031`.
4. Model refinancing as a staged event with application, approval, and closing times.
5. Compare refinance processes beginning 12, 9, and 6 months before maturity.
6. Export summarized results to an Excel dashboard.

### Required outputs

- probability and timing of covenant breach;
- probability refinancing closes before maturity;
- probability of a liquidity shortfall;
- P50 and P90 refinancing completion time;
- P10 minimum cash balance;
- expected and P90 borrowing cost;
- recommended start date and minimum liquidity reserve.

### Deliverables

- `week_08_debt_refinancing.xlsx`
- `week_08_debt_refinancing.ipynb`
- cleaned monthly financial dataset
- simulation-summary CSV
- management recommendation on timing and liquidity

---

## Drill 2 — Water-main failure timing and renewal

### Assignment

Use a messy synthetic break-history and asset inventory to estimate the probability and timing of future failures for cast-iron and ductile-iron water mains. Compare continued operation with targeted replacement of the highest-risk segments.

### Required workflow

1. Clean and reconcile asset, installation, break, and observation dates.
2. Identify failures, repeat failures, and right-censored assets.
3. Calculate a deterministic age- or break-rate ranking.
4. Fit or define a survival model and run at least **20,000 portfolio trials**.
5. Compare no action with a targeted renewal strategy.

### Required outputs

- one-, five-, and ten-year failure probabilities;
- P10, P50, and P90 time to next portfolio failure;
- expected failures and emergency-repair cost by year;
- probability of at least one critical-segment failure;
- risk reduction per renewal dollar;
- prioritized renewal list.

### Deliverables

- `week_08_water_main_survival.ipynb`
- cleaned asset-event table
- segment-level risk summary
- one-page engineering recommendation

---

## Drill 3 — Lift-station pump-fleet reliability

### Assignment

Evaluate a three-pump lift station with two duty pumps and one installed standby. Model pump failure time, repair duration, preventive-maintenance downtime, common-cause events, and wet-weather demand. Determine the probability that available pumping capacity falls below required capacity.

### Required workflow

1. Clean work-order, runtime, failure, and repair records.
2. Build a deterministic availability calculation.
3. Simulate at least **15,000 one-year event histories**.
4. Compare reactive maintenance, enhanced preventive maintenance, and expedited repair support.

### Required outputs

- probability of one or more capacity-deficit events;
- expected deficit-event count and duration;
- P50 and P90 unavailability hours;
- probability the standby pump is unavailable when demanded;
- effect of common-cause failures;
- recommended maintenance or repair strategy.

### Deliverables

- `week_08_pump_fleet_reliability.ipynb`
- cleaned event-history file
- strategy-comparison table
- planning-level reliability memo

---

## Drill 4 — Director decision: renewal budget and service risk

### Assignment

Allocate a constrained annual renewal budget across water mains, lift-station pumps, and electrical assets. Model first-failure timing, emergency cost, service consequence, planned replacement timing, and annual budget limits. Recommend a three-year capital strategy.

### Required workflow

1. Clean the portfolio register, cost history, condition ratings, and consequence categories.
2. Build a deterministic risk-score and budget-allocation baseline.
3. Run at least **20,000 three-year portfolio simulations**.
4. Compare age-first, risk-score, and survival-risk allocation strategies.
5. Apply identical random scenarios to all strategies.

### Required outputs

- expected and P90 three-year cost;
- expected critical failures;
- probability annual emergency spending exceeds reserve;
- probability service-risk tolerance is exceeded;
- planned versus emergency spending by year;
- recommended strategy and reserve.

### Deliverables

- `week_08_renewal_portfolio.ipynb`
- cleaned portfolio dataset
- strategy-comparison table
- one-page director decision memo

---

## Quality-control requirements

Apply these checks to every drill:

- Set and record the random seed.
- Preserve raw data and log cleaning decisions.
- Treat active loans and assets without an event as censored, not failed or missing.
- Define the time origin, event, horizon, and time units explicitly.
- Reproduce the deterministic baseline before simulating.
- Verify that sampled event times are nonnegative and within justified bounds.
- Distinguish annual probability from cumulative multi-year probability.
- Validate simulated survival or event counts against the source assumptions.
- Inspect at least one event history manually.
- Test convergence for the primary decision metric.
- Use common random scenarios for strategy comparisons.
- State limitations and avoid implying that a survival curve identifies an exact failure date.

## Completion checklist

- [ ] Four drills completed
- [ ] Data defects and censoring documented
- [ ] Deterministic baselines reproduced in Python
- [ ] Simulations use seed `20261031`
- [ ] Event definitions and time origins are explicit
- [ ] Survival and cumulative risk are reported correctly
- [ ] Strategy comparisons use common scenarios
- [ ] Finance workflow starts and ends in Excel
- [ ] Validation and interpretation are complete
- [ ] Each drill ends with a decision recommendation

