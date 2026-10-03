# Monte Carlo Modeling Drills — Week 4 Detailed Description

## Weekly Concept

**Conditional logic and discrete-event simulation**

Weeks 1–3 covered empirical sampling, bounded distributions, percentiles, correlation, and cumulative risk. Week 4 adds events whose consequences depend on the system state: invoices may be paid late, pump failures may persist for several days, emergency operating actions may activate only after storage drops below a threshold, and managers may reassign staff only when milestones begin to slip.

The central lesson is:

> A realistic risk model often needs rules about what happens next, not merely distributions for what happens now.

## Workload and Priorities

| Drill | Domain | Target time | Priority |
|---|---|---:|---|
| 1. Blue Ridge 13-week cash risk | Finance | 90–120 minutes | Required |
| 2. Pump outage and emergency storage | Municipal engineering | 60–75 minutes | Required |
| 3. Lift-station overflow response | Municipal engineering | 45–60 minutes | Standard |
| 4. Director resource-allocation decision | Municipal management | 45–60 minutes | Standard |

**Full week:** approximately 4–5 hours. If work is heavy, complete Drills 1 and 2 first, then choose Drill 4 before Drill 3. Do not split each drill into multiple notebooks. Use labeled sections for ingestion, inspection, cleaning, baseline, assumptions, simulation, validation, and interpretation.

## Suggested Week 4 Structure

```text
week_04/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── excel/
├── notebooks/
│   ├── finance_cash_risk.ipynb
│   ├── pump_outage_storage.ipynb
│   ├── lift_station_overflow.ipynb
│   └── director_resource_allocation.ipynb
├── outputs/
└── README.md
```

Use `numpy.random.default_rng(20261003)` and record the seed and trial count in every output.

---

# Drill 1 — Finance: Blue Ridge 13-Week Cash-Risk Forecast

## Scenario and Decision Question

Blue Ridge Digital is profitable on an accrual basis but must fund biweekly payroll while customers pay on different schedules. Management is considering four hires. Before expanding, it wants to know:

> What is the probability that unrestricted cash falls below $100,000 during the next 13 weeks, when does the low point occur, and how large should a temporary credit facility be?

This extends Week 2's revenue work into timing and liquidity. Revenue is not cash until it is collected.

## Starting Data

Create a synthetic workbook or CSV package containing:

- 45–60 open invoices with customer, invoice date, due date, amount, status, and customer payment class;
- 13 weeks of planned payroll and operating disbursements;
- beginning unrestricted cash of $300,000;
- a proposed hiring date in Week 5; and
- fixed weekly receipts unrelated to invoices, if any.

Inject realistic defects:

- one duplicate invoice;
- currency stored as text;
- two missing due dates;
- inconsistent customer names;
- one credit memo entered as a positive invoice;
- one invoice marked paid without a payment date;
- mixed date formats;
- an expense posted to the wrong week; and
- a stale invoice older than 120 days requiring an explicit collectability decision.

## Start in Excel

Create `excel/blue_ridge_13_week_cash_risk.xlsx` with:

- `Raw_Invoices`
- `Raw_Disbursements`
- `Clean_Invoices`
- `Clean_Disbursements`
- `Assumptions`
- `Baseline_Cash_Flow`
- `Simulation_Summary`
- `Dashboard`

Use Power Query or documented formulas to clean the inputs. Preserve the raw sheets.

### Deterministic Baseline

Build a 13-week cash forecast in Excel using stated collection dates and planned payment dates:

```text
Ending cash_t = Beginning cash_t + Collections_t − Disbursements_t
Beginning cash_(t+1) = Ending cash_t
```

Report deterministic minimum cash, ending cash, week of minimum cash, and any borrowing requirement. Add proposed-hire payroll beginning in Week 5.

## Python Simulation

Run 20,000 trials. Assign each invoice a customer payment class and sample collection delay conditionally:

| Payment class | On time | 1–14 days late | 15–30 days late | Default/after horizon |
|---|---:|---:|---:|---:|
| Strong | 75% | 20% | 4% | 1% |
| Average | 50% | 32% | 15% | 3% |
| Weak | 25% | 35% | 30% | 10% |

Within a selected late-payment category, sample an integer delay uniformly over the applicable interval. Model weekly nonpayroll operating expense with a bounded multiplier, such as triangular `(0.95, 1.00, 1.12)`. Model the hiring start as Week 5, 7, or 9 with probabilities 50%, 30%, and 20%.

Conditional rules:

1. A defaulted invoice produces no cash during the 13-week horizon.
2. A collection is recognized in the week containing its simulated receipt date.
3. If cash would fall below zero, draw on the credit facility before calculating ending cash.
4. Interest accrues only after borrowing occurs.
5. Do not count invoices already paid before Week 1.

Required results:

- probability minimum cash is below $100,000;
- probability cash becomes negative before borrowing;
- P10, P50, and P90 minimum cash;
- P50 and P90 peak borrowing requirement;
- distribution of the week of minimum cash;
- probability the proposed hires can begin in Week 5 without breaching the $100,000 reserve; and
- risk-driver ranking using Spearman correlation or grouped scenario comparison.

## Finish in Excel

Build a management dashboard with:

- deterministic versus simulated minimum cash;
- probability of breaching the reserve;
- P50/P90 borrowing need;
- most likely low-cash week;
- cash trajectory fan chart or selected percentile lines;
- top three liquidity drivers;
- immediate-hire versus delayed-hire comparison; and
- a two- or three-sentence management recommendation.

## Deliverables

- Cleaned and exception-tagged invoice/disbursement data
- Deterministic Excel cash forecast
- Python notebook and exported summary tables
- Management-facing Excel dashboard
- Five-sentence liquidity recommendation

## Quality-Control Checks

- Beginning cash plus total receipts minus total disbursements and interest must reconcile to ending cash.
- Credit draws cannot occur before a cash deficit under the defined rule.
- Credit balances and interest cannot be negative.
- Invoice collection probabilities must total 100% within each payment class.
- Duplicate invoices and paid invoices must not be collected twice.
- Force all invoices to their deterministic dates and all expense multipliers to 1.00; Python must reproduce the Excel baseline.
- Compare key metrics at 5,000 and 20,000 trials.

## Interpretation Questions

1. Why can a profitable company still experience a cash shortfall?
2. Is the expected minimum cash or the P10 minimum more useful for setting a reserve?
3. Which customers create concentration risk?
4. Does delaying the hires reduce total risk or merely shift it?
5. What data would improve the payment-delay assumptions?

## Brief Solution Checkpoints

- The invoice amount and its collection week must remain linked.
- The low point should be calculated separately for every simulated 13-week path.
- A credit facility should be sized from the distribution of peak borrowing, not average ending cash.
- If the deterministic case looks comfortable while the simulation shows meaningful risk, timing uncertainty is doing real work.

---

# Drill 2 — Municipal Engineering: Pump Outage Duration and Emergency Storage

## Scenario and Decision Question

A water system has two duty-capable high-service pumps and usable storage between 0.30 and 1.50 MG. Week 3 sampled an independent pump state each day. This week, failures persist until repair is completed.

> Over a 30-day operating horizon, what is the probability of violating minimum storage, and how much does a defined emergency operating action reduce that risk?

## Starting Data and Cleaning

Generate 180 daily records containing date, demand, temperature, pump runtime, available capacity, maintenance flag, and operator notes. Include:

- duplicated dates;
- missing runtime values;
- `gpm` embedded in numeric capacity cells;
- one impossible negative runtime;
- inconsistent maintenance labels;
- one demand value entered in gallons instead of MG; and
- two outage records with missing return-to-service dates.

Clean the data, preserve an exception log, align units, and distinguish missing from true zero.

## Deterministic Baseline

Use average demand, normal pump capacity, starting storage of 1.20 MG, and no failures. Calculate storage for 30 days with an upper bound of 1.50 MG and a minimum criterion of 0.30 MG.

## Discrete-Event Model

Run 20,000 thirty-day trials. Use preliminary assumptions:

| Event or input | Suggested model |
|---|---|
| Daily demand | Bootstrap complete cleaned rows or a weather-conditioned empirical sample |
| Failure initiation | Bernoulli event when pump is operating normally |
| Daily failure probability | 0.8% per operating pump-day |
| Repair duration | Discrete: 1 day 45%, 2 days 30%, 3 days 15%, 5 days 10% |
| Reduced-capacity factor during one-pump operation | Triangular `(0.48, 0.55, 0.62)` |
| Starting storage | Triangular `(1.00, 1.20, 1.40)` MG |

State logic:

1. A pump that fails remains unavailable for the sampled repair duration.
2. Do not initiate another failure for the same unavailable pump.
3. If both pumps are unavailable, normal supply is zero.
4. Record unmet demand before clamping displayed storage at zero.
5. In the mitigation case, activate emergency supply of 0.25 MG/day on the day after storage first falls below 0.55 MG; it remains available for up to four days.

Compare **Base Operations** with **Emergency Response** using identical random-number streams where practical.

Required results:

- probability of any storage violation;
- probability of complete storage depletion;
- P10/P50/P90 minimum storage;
- expected unmet demand;
- probability of overlapping pump outages;
- distribution of outage duration; and
- absolute and relative risk reduction from emergency response.

## Deliverables

- Clean dataset and exception log
- Deterministic 30-day mass balance
- Python simulation with explicit pump states
- Base-versus-mitigation comparison table
- Storage trajectories for normal, near-miss, and failure cases
- Short engineering recommendation

## Quality-Control Checks

- Pump state transitions must be auditable for one selected trial.
- Repair countdown must decrease exactly once per simulated day.
- Failed pumps cannot contribute capacity.
- Emergency supply cannot begin before its trigger or exceed four days.
- Storage cannot exceed 1.50 MG; deficits must be recorded before display clamping.
- With failure probability set to zero, the simulation should approach the deterministic case.
- Compare 5,000 and 20,000 trials.

## Interpretation Questions

1. Why is persistent outage duration more realistic than independent daily outage draws?
2. Does emergency supply reduce failure frequency, severity, or both?
3. Which assumption matters more: failure probability or repair duration?
4. What maintenance records would improve the model?
5. What hydraulic limitations are omitted from this storage-only analysis?

## Brief Solution Checkpoints

- The same outage must persist across days; do not resample an operating state for a failed pump.
- Low-probability overlapping outages may dominate the severe tail.
- Compare strategies with common random numbers if possible so differences are driven by the operating rule rather than sampling noise.

---

# Drill 3 — Municipal Engineering: Lift-Station Overflow and Response Logic

## Scenario and Decision Question

A duplex wastewater lift station receives variable inflow. One pump normally meets average conditions, but wet-weather inflow, pump failure, and delayed response can cause wet-well overflow.

> What is the probability and expected volume of overflow during a seven-day wet-weather period, and which response improvement provides the most risk reduction?

## Data and Cleaning

Create hourly synthetic records for 60 days with inflow, rainfall, wet-well level, pumps available, alarm status, and response time. Add missing hours, duplicate timestamps, rainfall recorded as text, inconsistent alarm labels, one negative inflow, and one implausible wet-well elevation.

## Deterministic Baseline

Use average dry-weather inflow, both pumps available, and no rainfall. Verify by hand that the wet-well volume balance remains within operating limits for 24 hours.

## Simulation

Run 15,000 seven-day trials using hourly steps:

- bootstrap wet-weather inflow/rainfall blocks so storm persistence is retained;
- model a pump-start failure as a Bernoulli event;
- when a high-level alarm occurs, sample response delay from a discrete or triangular distribution;
- activate portable bypass pumping only after the sampled response delay;
- cap bypass capacity at its stated value; and
- record overflow occurrence, duration, and volume.

Compare:

- current response: triangular `(1.0, 2.5, 5.0)` hours;
- improved response: triangular `(0.5, 1.0, 2.0)` hours; and
- optional permanent standby pump with defined availability.

## Deliverables

- Clean hourly dataset
- Deterministic wet-well balance
- Python event simulation
- Current-versus-improved response results
- One-page technical summary with recommended operational action

## Quality-Control Checks

- Confirm all flow units are converted consistently before the volume balance.
- Confirm overflow volume is accumulated only above physical wet-well capacity.
- Confirm bypass pumping cannot begin before alarm plus response delay.
- Confirm pump and bypass discharge cannot exceed their capacities.
- Manually reproduce at least six consecutive hourly calculations.
- Confirm zero failures and zero rainfall eliminate overflow in the control case.

## Interpretation Questions

1. Is probability of overflow sufficient, or is overflow volume also necessary?
2. How does response-time uncertainty affect the result?
3. Why should storm hours be sampled in blocks instead of independently?
4. Which is more valuable: faster response or more permanent capacity?

## Brief Solution Checkpoints

- Independent hourly rainfall sampling will destroy storm duration and can materially distort results.
- Alarm, response, and bypass start are separate events.
- A low-frequency event with a large overflow volume may deserve more attention than a frequent near-miss.

---

# Drill 4 — Director/Management: Portfolio Staffing and Deadline Risk

## Scenario and Decision Question

You direct a municipal water group delivering four active projects: a force-main design, lift-station design, reclaimed-water main, and water-treatment planning study. The same senior technical staff support several projects. You have 240 staff-hours available next week and cannot satisfy every request at its preferred level.

> Which staffing allocation best balances deadline reliability, expected rework, client impact, and overtime exposure across the project portfolio?

## Starting Data and Cleaning

Create a synthetic project register containing project, client, milestone, due date, percent complete, hours remaining, requested discipline, assigned staff, probability of review comments, potential rework hours, client priority, and contractual consequence.

Include:

- inconsistent project IDs;
- hours stored as text;
- one duplicate staffing request;
- missing due date;
- percent complete entered once as `75` and elsewhere as `0.75`;
- mismatched employee names;
- one milestone already complete but still requesting hours; and
- one risk marked both closed and active.

## Deterministic Baseline

Develop three candidate allocations totaling no more than 240 regular hours:

- **A — Deadline first:** prioritize the nearest contractual milestones.
- **B — Client first:** prioritize the highest client/market consequence.
- **C — Risk balanced:** protect critical milestones while reserving review capacity for likely rework.

Calculate scheduled completion and planned overtime for each allocation without uncertainty.

## Simulation

Run 20,000 trials for each allocation. Suggested uncertain events:

| Driver | Suggested model |
|---|---|
| Review comments requiring rework | Bernoulli by project |
| Rework hours if triggered | Beta-PERT from low/mode/high estimates |
| Staff absence | Discrete: 0, 8, or 16 hours unavailable |
| Client scope clarification delay | Discrete delay of 0, 2, or 5 working days |
| Productivity multiplier | Triangular `(0.85, 1.00, 1.10)` |

Conditional rules:

1. Rework hours occur only if review comments are triggered.
2. Scope-delay days affect only tasks awaiting client information.
3. Staff absence reduces available hours before overtime is calculated.
4. Overtime is allowed up to a stated cap; excess work becomes schedule delay.
5. A portfolio failure occurs if any critical milestone is late, but also report project-specific probabilities.

Use a simple decision score only after calculating the underlying metrics:

```text
Decision score =
    40% × deadline reliability
  + 30% × client-priority protection
  + 20% × normalized overtime performance
  + 10% × workload-balance performance
```

Document the normalization and test at least one alternative weighting. The score supports judgment; it does not replace it.

## Deliverables

- Clean project/staffing register and exception log
- Three deterministic allocation plans
- Python simulation and allocation comparison
- One-page director decision memo
- A short list of actions to reduce uncertainty before Monday's staffing meeting

Required comparison metrics:

- probability every critical milestone is met;
- probability each project milestone is late;
- expected and P90 overtime hours;
- expected rework hours;
- probability one employee exceeds the workload cap;
- client-priority exposure; and
- weighted decision score with sensitivity to the weights.

## Quality-Control Checks

- Regular allocated hours cannot exceed 240.
- No person can be assigned to two tasks during the same modeled hours.
- Rework cannot occur unless its trigger occurs.
- Completed milestones must consume zero future hours.
- Project-specific lateness must reconcile with portfolio failure.
- Force all event probabilities to zero and productivity to 1.00; reproduce the deterministic plans.
- Confirm the recommended allocation remains reasonable under an alternative weighting scheme.

## Interpretation Questions

1. Which allocation has the best average outcome, and which has the best downside protection?
2. Is one high-priority client's risk dominating the portfolio decision?
3. What would you communicate to project managers whose requests are not fully staffed?
4. Which risk should be mitigated through staffing, and which needs client communication?
5. When would hiring, subcontracting, or schedule renegotiation be more appropriate than overtime?

## Brief Solution Checkpoints

- The plan with the highest expected decision score may not have the highest probability of meeting every deadline.
- Portfolio failure probability will usually exceed most individual project failure probabilities because any critical miss counts.
- Rework capacity is not idle time; it is a deliberate risk reserve.
- A director recommendation should include both the allocation and the conversations required to make it workable.

---

# Week 4 Completion Checklist

- [ ] Raw data preserved and cleaning exceptions documented
- [ ] Deterministic baseline completed before each simulation
- [ ] Conditional events represented explicitly
- [ ] Event states persist for the correct duration
- [ ] Threshold-triggered actions occur only after their triggers
- [ ] Random seed and trial count documented
- [ ] At least one path from each model manually reconciled
- [ ] Stability checked at two trial counts
- [ ] Finance results returned to a management-facing Excel dashboard
- [ ] Engineering results include frequency and severity metrics
- [ ] Director drill compares at least three allocation strategies
- [ ] Recommendations identify limitations and a next action

# End-of-Week Reflection

Answer briefly:

1. Which conditional rule changed a result the most?
2. Where would an independent-draw model have been misleading?
3. Which state transition was hardest to validate?
4. Did a deterministic baseline pass while the simulation exposed material risk?
5. Which model would benefit most from better event-frequency or duration data?
