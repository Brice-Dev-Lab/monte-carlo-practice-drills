# Week 7 Monte Carlo Modeling Drills — Assignment Scope

## Weekly theme

**Correlated inputs and multivariate sampling**

Week 7 moves beyond modeling uncertain variables one at a time. Each assignment asks you to preserve realistic relationships among inputs, compare correlated and independent simulations, and explain how those relationships change a decision.

**Recommended workload:** 4.5–5.5 hours total  
**Reproducibility seed:** `20261024`

## Learning objectives

By the end of the week, you should be able to:

- clean and align multiple related variables;
- build and validate a covariance or correlation matrix;
- generate correlated samples in Python;
- compare a deterministic baseline with probabilistic results;
- test the consequence of incorrectly assuming independence;
- translate simulation output into a finance or municipal-management decision.

## Drill schedule

| Drill | Application | Suggested time | Primary decision |
|---|---|---:|---|
| 1 | Finance — multi-asset portfolio | 90 minutes | Is the proposed allocation acceptable under correlated market risk? |
| 2 | Municipal engineering — force-main performance | 75 minutes | How reliably can the system meet the target flow? |
| 3 | Municipal engineering — standby-generator adequacy | 60 minutes | Is the generator adequate under realistic coincident loads? |
| 4 | Director/management — design fee and margin risk | 75 minutes | What fee or reserve is needed to protect the target margin? |

---

## Drill 1 — Multi-asset portfolio risk

### Assignment

Evaluate a one-year, **$250,000** portfolio allocated to SPY, BND, VNQ, and GLD. Use monthly adjusted prices from Yahoo Finance when available, or a supplied synthetic price history. Begin the analysis in Excel, perform the simulation in Python, and finish with a management-facing Excel dashboard.

### Required workflow

1. In Excel, inspect and clean the price history, align common month-end dates, calculate monthly returns, document weights, and calculate the deterministic baseline.
2. In Python, run at least **20,000 one-year trials** using:
   - paired historical-row bootstrap; and
   - multivariate normal sampling from the estimated mean vector and covariance matrix.
3. Compare both models with an intentionally independent-input case.
4. Export summary tables to Excel and build the dashboard.

### Required outputs

- P10, P50, and P90 ending value;
- probability of a one-year loss;
- 95% value at risk and expected shortfall;
- distribution of maximum drawdown;
- simulated versus historical correlations;
- comparison of correlated and independent results.

### Deliverables

- `week_07_finance_portfolio.xlsx`
- `week_07_finance_portfolio.ipynb`
- cleaned return file and simulation-summary CSV
- one-paragraph management interpretation

---

## Drill 2 — Force-main hydraulic performance

### Assignment

Estimate the probability that an existing force-main and pump system can deliver a target flow of **4,500 gpm** while maintaining acceptable velocity. Model uncertainty in static head, pipe diameter, Hazen–Williams coefficient, minor losses, pump-curve performance, and system demand.

### Required workflow

1. Clean the supplied pump-test, pressure, level, and flow records.
2. Calculate a deterministic system curve and pump/system operating point.
3. Define defensible marginal distributions and dependencies.
4. Run at least **20,000 correlated trials** and an independent-input comparison.
5. Validate hydraulic units, root-solving behavior, and simulated dependence.

### Required outputs

- P10, P50, and P90 operating flow and total dynamic head;
- probability of failing to meet 4,500 gpm;
- probability that velocity falls outside 2–8 ft/s;
- difference between correlated and independent risk estimates;
- primary drivers of inadequate capacity.

### Deliverables

- `week_07_force_main.ipynb`
- cleaned hydraulic input file
- simulation-summary CSV
- one-page engineering findings note

---

## Drill 3 — Lift-station standby-generator adequacy

### Assignment

Evaluate whether a lift-station generator can support realistic running and starting loads. Treat pump operation, wet-weather conditions, auxiliary demand, power factor, motor efficiency, and starting method as related—not isolated—inputs.

### Required workflow

1. Clean the equipment schedule and SCADA operating records.
2. Calculate deterministic running kW, running kVA, and the largest planned starting step.
3. Simulate at least **15,000 operating and start-event scenarios**.
4. Evaluate the existing configuration and one mitigation, such as sequential starting or nonessential-load shedding.

### Required outputs

- P50 and P90 running kW and kVA;
- probability that running load exceeds 80% of generator nameplate;
- probability that the modeled transient kVA exceeds the planning limit;
- most consequential equipment combinations;
- risk reduction from the selected mitigation.

### Deliverables

- `week_07_generator_adequacy.ipynb`
- cleaned equipment/load table
- scenario comparison table
- planning-level recommendation

> This drill is a screening analysis, not a substitute for an electrical engineer's code review, protective-device study, or manufacturer verification.

---

## Drill 4 — Director decision: design fee and margin risk

### Assignment

Price a multidisciplinary municipal design assignment while accounting for correlated discipline hours, scope growth, rework, schedule extension, labor-rate escalation, and subcontractor cost. Recommend a fee or management reserve that gives an acceptable chance of achieving the target margin.

### Required workflow

1. Clean historical estimate-versus-actual project data.
2. Build a deterministic fee and margin baseline.
3. Run at least **20,000 correlated cost scenarios** using common random scenarios for every pricing option.
4. Compare the proposed fee, a risk-adjusted fee, and a phased-scope option.

### Required outputs

- expected and P80 delivery cost;
- expected margin and probability of margin below 10%;
- probability of a negative margin;
- recommended fee or reserve;
- top risk drivers and proposed commercial controls.

### Deliverables

- `week_07_fee_margin.ipynb`
- cleaned historical-project file
- pricing-options table
- one-page director decision memo

---

## Quality-control requirements

Apply these checks to every drill:

- Set and record the random seed.
- Separate raw, cleaned, and simulated data.
- Preserve raw values and log all cleaning decisions.
- Reproduce the deterministic baseline inside Python before simulating.
- Confirm that units and time bases are consistent.
- Verify that the correlation matrix is valid and positive semidefinite.
- Compare target, historical, and simulated correlations.
- Inspect at least one trial by hand.
- Report convergence for the primary risk metric.
- Compare correlated and independent results using the same assumptions otherwise.
- State limitations and avoid false precision.

## Completion checklist

- [ ] Four drills completed
- [ ] Messy data cleaned and documented
- [ ] Deterministic baselines reproduced
- [ ] Simulations are reproducible
- [ ] Dependence assumptions are explicit
- [ ] Correlated and independent cases are compared
- [ ] Results are validated and interpreted
- [ ] Finance workflow begins and ends in Excel
- [ ] Decisions are stated in plain language

