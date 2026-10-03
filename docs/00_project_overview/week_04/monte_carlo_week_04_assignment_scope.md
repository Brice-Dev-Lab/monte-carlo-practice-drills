# Monte Carlo Modeling Drills — Week 4 Assignment Scope

## Weekly Focus

**Conditional logic and discrete-event simulation**

Week 4 moves beyond independent random draws. Each exercise includes events that change the future state of the model—for example, a late invoice changes weekly cash, a failed pump remains unavailable until repaired, and a staffing shortage affects whether project milestones are achieved.

## Weekly Objective

Develop the ability to:

- model conditional events and state changes;
- distinguish event probability from event duration and consequence;
- build a deterministic baseline before introducing uncertainty;
- preserve reproducibility with a documented random seed;
- validate event sequences and individual simulation paths; and
- convert probabilistic results into a practical financial, engineering, or management recommendation.

## Estimated Workload

| Drill | Domain | Estimated time | Priority |
|---|---|---:|---|
| 1. Blue Ridge 13-week cash risk | Finance | 90–120 minutes | Required |
| 2. Pump outage and emergency storage | Municipal engineering | 60–75 minutes | Required |
| 3. Lift-station overflow response | Municipal engineering | 45–60 minutes | Standard |
| 4. Project staffing and deadline risk | Municipal director/management | 45–60 minutes | Standard |

Total estimated workload is approximately **4–5 hours**. If time is limited, complete Drills 1 and 2 first, followed by Drill 4.

---

## Drill 1 — Finance: Blue Ridge 13-Week Cash Risk

### Assignment

Build a probabilistic 13-week cash-flow model for Blue Ridge Digital. Evaluate whether the company can add four employees while maintaining a minimum unrestricted-cash reserve of $100,000.

### Required Workflow

1. Begin in Excel with messy invoice and disbursement data.
2. Clean and document duplicates, missing dates, inconsistent customer names, credit memos, stale invoices, and numeric values stored as text.
3. Build a deterministic 13-week cash-flow forecast.
4. Define collection-delay, default, expense, and hiring-timing assumptions.
5. Run 20,000 reproducible Python simulations.
6. Export summary and percentile results to Excel.
7. Complete a management-facing Excel dashboard.

### Required Outputs

- Probability minimum cash falls below $100,000
- Probability cash becomes negative before borrowing
- P10, P50, and P90 minimum cash
- P50 and P90 peak borrowing requirement
- Most likely week of minimum cash
- Immediate-hiring versus delayed-hiring comparison
- Management recommendation

### Deliverables

- Cleaned invoice and disbursement data
- Data-cleaning exception log
- Deterministic Excel forecast
- Python simulation notebook
- Simulation-results export
- Completed Excel dashboard

---

## Drill 2 — Municipal Engineering: Pump Outage and Emergency Storage

### Assignment

Model a two-pump water system over a 30-day operating period. Pump failures must persist for a sampled repair duration rather than being independently resampled each day. Compare base operations with an emergency-supply response.

### Required Workflow

1. Clean 180 days of synthetic demand, temperature, capacity, runtime, and maintenance data.
2. Resolve duplicate dates, inconsistent units, missing values, negative runtime, and incomplete outage records.
3. Calculate a deterministic 30-day storage balance with no failures.
4. Model pump-failure initiation, repair duration, reduced capacity, initial storage, and daily demand.
5. Add emergency supply triggered when storage falls below the defined threshold.
6. Run 20,000 trials for base operations and emergency response.
7. Compare failure frequency, failure severity, and mitigation effectiveness.

### Required Outputs

- Probability of violating minimum storage
- Probability of complete depletion
- P10, P50, and P90 minimum storage
- Expected unmet demand
- Probability of overlapping outages
- Absolute and relative risk reduction from emergency response
- Engineering recommendation

### Deliverables

- Cleaned operational dataset
- Exception log
- Deterministic storage calculation
- Python discrete-event simulation
- Base-versus-mitigation comparison
- Representative storage trajectories
- Brief technical summary

---

## Drill 3 — Municipal Engineering: Lift-Station Overflow Response

### Assignment

Estimate the probability, duration, and volume of lift-station overflow during a seven-day wet-weather period. Compare current emergency response time with an improved response procedure.

### Required Workflow

1. Clean hourly inflow, rainfall, wet-well level, pump, alarm, and response records.
2. Preserve storm persistence by sampling hourly data in blocks.
3. Build a deterministic 24-hour wet-well balance.
4. Model pump-start failure, high-level alarm, operator response delay, and portable-bypass activation.
5. Run 15,000 seven-day trials.
6. Compare current response, improved response, and an optional standby-pump alternative.

### Required Outputs

- Probability of overflow
- Expected overflow duration
- Expected and upper-percentile overflow volume
- Effect of improved response time
- Recommended operational or capital action

### Deliverables

- Clean hourly dataset
- Deterministic wet-well balance
- Python simulation notebook
- Alternative comparison table
- One-page technical summary

---

## Drill 4 — Director/Management: Project Staffing and Deadline Risk

### Assignment

Allocate 240 available staff-hours among four municipal projects. Compare three staffing strategies based on deadline reliability, client importance, rework exposure, overtime, and workload balance.

### Required Strategies

- **Strategy A — Deadline first:** prioritize the nearest contractual milestones.
- **Strategy B — Client first:** prioritize the highest client and market consequences.
- **Strategy C — Risk balanced:** protect critical milestones while reserving capacity for likely rework.

### Required Workflow

1. Clean the project and staffing register.
2. Resolve inconsistent project IDs, duplicate requests, incomplete milestones, mixed percentage formats, and inconsistent employee names.
3. Prepare a deterministic allocation for each strategy.
4. Model review-driven rework, staff absence, client-information delays, and productivity.
5. Run 20,000 trials for each allocation.
6. Compare the strategies and prepare a director-level recommendation.

### Required Outputs

- Probability all critical milestones are met
- Project-specific lateness probability
- Expected and P90 overtime
- Expected rework hours
- Probability of exceeding individual workload limits
- Client-priority exposure
- Decision score and sensitivity to alternative weights

### Deliverables

- Cleaned project/staffing register
- Three deterministic staffing plans
- Python simulation notebook
- Strategy-comparison table
- One-page director decision memo

---

## Standards Applying to All Four Drills

Each drill must include:

- a clearly stated decision question;
- raw data retained unchanged;
- documented data-cleaning decisions;
- a deterministic baseline;
- an assumptions table with units and rationale;
- `numpy.random.default_rng(20261003)` or another documented seed;
- a stated number of trials;
- at least one manually reconciled simulation path;
- comparison of results using two trial counts;
- percentile and failure/exceedance metrics;
- stated limitations; and
- a recommendation tied directly to the modeled decision.

## Completion Checklist

- [ ] Four decision questions stated
- [ ] Raw datasets preserved
- [ ] Cleaning exceptions documented
- [ ] Deterministic baselines completed
- [ ] Conditional rules documented before coding
- [ ] Event states persist for the correct duration
- [ ] Threshold actions occur only after their triggers
- [ ] Random seed and trial count recorded
- [ ] Selected paths manually reconciled
- [ ] Simulation stability checked
- [ ] Finance dashboard completed in Excel
- [ ] Engineering results report frequency and severity
- [ ] Three management strategies compared
- [ ] Final recommendations and limitations written

## Definition of Completion

Week 4 is complete when the four models can reproduce their deterministic baselines with uncertainty disabled, event sequences pass the quality-control checks, results remain reasonably stable at the selected trial count, and each model produces a defensible decision recommendation.

