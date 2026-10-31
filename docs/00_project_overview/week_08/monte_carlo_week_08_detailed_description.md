# Week 8 Monte Carlo Modeling Drills — Detailed Description

## Main concept: event timing and survival

Earlier weeks focused on uncertain magnitudes, percentiles, conditional events, and correlation. Week 8 adds time: when will refinancing fail to close, when will an asset fail, how long will it remain unavailable, and when should management intervene?

For an event time \(T\):

\[
S(t)=P(T>t)
\]

is the survival function, while:

\[
F(t)=P(T\le t)=1-S(t)
\]

is the cumulative probability that the event has occurred by time \(t\). The hazard describes the instantaneous event rate among items that have survived to that time. It is not the same thing as cumulative failure probability.

An observation is **right-censored** when the event has not occurred by the end of the observation period. A loan that has not breached a covenant and a pipe that has not failed still provide useful survival information; they must not be discarded or coded as events.

Use `numpy.random.default_rng(20261031)` for the primary simulations.

## Suggested work plan

| Session | Work | Time budget |
|---|---|---:|
| 1 | Finance Excel cleaning and deterministic schedule | 35 minutes |
| 2 | Finance Python simulation and Excel dashboard | 55 minutes |
| 3 | Water-main survival exercise | 75 minutes |
| 4 | Pump-fleet reliability exercise | 60 minutes |
| 5 | Director renewal-budget decision | 75 minutes |
| Buffer | Weekly synthesis and corrections | 20–30 minutes |

---

# Drill 1 — Debt maturity and refinancing risk

## Decision scenario

Blue Ridge Digital has a five-year term loan with a balloon balance of approximately **$650,000** due in 24 months. The loan carries a floating rate equal to a reference rate plus a contractual spread. Management expects to refinance, but lender review and closing duration vary, and approval depends on leverage, debt-service coverage, and operating performance.

Compare three policies:

- **Policy A:** begin refinancing 12 months before maturity;
- **Policy B:** begin 9 months before maturity; and
- **Policy C:** begin 6 months before maturity.

The decision is not simply which policy has the lowest expected cost. It is which policy balances financing cost, management effort, and the probability of closing before maturity without a liquidity crisis.

## Synthetic source files

Use three synthetic files:

1. `monthly_financial_history_dirty.csv` — revenue, EBITDA, cash, receivables, capital spending, and owner distributions.
2. `loan_schedule_dirty.xlsx` — payment dates, beginning balance, principal, interest, rate, and maturity.
3. `refinancing_cases_dirty.csv` — historical application, approval, diligence, documentation, and closing dates.

### Required data defects

Include or expect:

- month fields stored as both dates and text;
- duplicate month-end records;
- revenue and cash stored with currency symbols;
- expenses represented with inconsistent signs;
- one missing EBITDA value;
- percentages stored as `7.5%`, `0.075`, and `7.5`;
- payment dates shifted to weekends;
- a loan balance that fails to roll forward because of one incorrect principal sign;
- withdrawn refinancing cases mixed with completed cases;
- open cases with blank closing dates;
- lender-stage names with inconsistent capitalization;
- one impossible closing date before the application date.

Open refinancing cases are censored at the data-extract date. Withdrawn cases should be analyzed separately rather than silently treated as completed or censored.

## Excel starting model

Create the following sheets:

- `Raw_Financials`
- `Raw_Loan`
- `Raw_Refi_Cases`
- `Clean_Financials`
- `Debt_Schedule`
- `Assumptions`
- `Baseline`
- `Simulation_Summary`
- `Strategy_Comparison`
- `Dashboard`

Use Power Query or documented formulas to clean the source data. Preserve a raw snapshot and record the refresh date.

## Deterministic baseline

Build a 24-month schedule for:

- beginning and ending debt balance;
- monthly interest and principal;
- operating cash flow;
- debt-service coverage ratio;
- leverage ratio;
- unrestricted cash;
- balloon payment or refinancing proceeds.

Define every covenant exactly. For example:

\[
DSCR=\frac{EBITDA-Cash\ Taxes-Maintenance\ Capex}{Required\ Principal+Interest}
\]

If the source loan agreement uses a different definition, the model must follow that definition. Do not mix monthly EBITDA with annual debt service without a deliberate annualization convention.

The baseline should identify the deterministic refinancing start date, expected closing month, maturity balance, minimum cash, and covenant headroom.

## Uncertain inputs

Model at least:

- monthly revenue growth or contraction;
- EBITDA margin;
- collection delay and resulting cash conversion;
- reference interest rate;
- lender spread at closing;
- application-to-approval duration;
- approval-to-closing duration;
- probability of additional lender information requests;
- probability of initial lender rejection;
- extension availability, cost, and duration;
- emergency owner contribution or credit-line availability.

Use conditional logic. A rejected application may trigger a second lender process; an information request adds time only if it occurs; an extension fee applies only if the refinancing misses maturity and an extension is available.

## Python simulation

Run at least 20,000 monthly paths for each policy using common random numbers. Each trial should:

1. simulate 24 months of operating performance and cash flow;
2. update debt service using the sampled rate path;
3. identify the first month of covenant breach, if any;
4. simulate the refinancing stages after the selected start date;
5. test lender approval using the documented financial thresholds;
6. determine whether closing occurs before maturity;
7. apply an extension or liquidity action when required; and
8. calculate total financing cost and minimum cash.

Store `NaN` or an explicit no-event flag for paths without covenant breach. Do not assign month 24 as the breach month merely because the simulation ended.

## Required outputs

- probability of covenant breach within 12 and 24 months;
- survival curve for time without covenant breach;
- P50 and P90 application-to-closing duration;
- probability refinancing closes before maturity;
- probability an extension is required;
- probability minimum cash is below zero or a selected threshold;
- P10 minimum cash;
- expected, P50, and P90 financing cost;
- incremental expected cost of beginning earlier;
- recommended start policy and liquidity reserve.

## Excel dashboard

The dashboard should contain:

- policy comparison cards;
- probability of on-time refinancing;
- probability of covenant breach and liquidity shortfall;
- P10 minimum cash;
- refinancing completion curve or cumulative closing chart;
- financing-cost distribution;
- primary risk-driver chart;
- key assumptions and refresh date; and
- a concise recommendation.

Use labels such as “90% of trials closed by X months,” not an ambiguous “P90 closing date.”

## Quality-control checks

- Loan balances roll forward exactly in Excel and Python.
- Interest rate units and monthly/annual conversions are consistent.
- Debt-service and covenant definitions match the assumptions sheet.
- Open refinancing cases are treated as censored.
- Completion time cannot precede the application date.
- Conditional costs occur only when their triggering event occurs.
- Python reproduces the Excel baseline when uncertainty is disabled.
- Common random numbers are used across the three policies.
- On-time closing probability is nondecreasing as the start date moves earlier, unless a documented policy feature explains otherwise.
- The main probability is stable when trials increase from 10,000 to 20,000.

## Interpretation questions

1. Is the primary risk poor operating performance, lender rejection, or process duration?
2. How much does starting earlier reduce tail risk relative to its expected cost?
3. Why is average closing duration inadequate for selecting a start date?
4. What should management negotiate now to reduce refinancing risk?
5. What should a decision-maker not conclude from the simulated closing curve?

## Brief solution checkpoint

The early-start policy should generally have the highest probability of closing before maturity, but it may carry additional fees or expose the company to earlier rate-lock decisions. A sound recommendation will state the required on-time-closing probability, show the liquidity consequence of missing maturity, and select a start date based on tail duration rather than average duration alone.

---

# Drill 2 — Water-main failure timing and renewal

## Decision scenario

A utility owns approximately 80 synthetic water-main segments installed between 1948 and 2018. Materials include cast iron, ductile iron, PVC, and steel. The utility has ten years of break records and must decide which segments to replace during the next three-year capital cycle.

Compare:

- **Strategy A:** no planned replacement during the analysis period;
- **Strategy B:** replace the oldest eligible segments; and
- **Strategy C:** replace the segments with the highest modeled five-year failure consequence.

## Synthetic source files

- `water_main_inventory_dirty.csv`
- `water_main_breaks_dirty.csv`
- `soil_traffic_consequence_dirty.csv`
- `repair_cost_history_dirty.csv`

### Required data defects

- asset IDs with spaces, hyphens, and inconsistent case;
- duplicate break records;
- missing installation years;
- material abbreviations such as `CI`, `Cast Iron`, and `C.I.`;
- diameters recorded as text and in mixed units;
- break dates before the recorded installation date;
- replacement dates not reflected in the inventory;
- zero-length segments;
- consequence ratings outside the valid scale;
- repair costs containing commas and dollar signs;
- active assets with no break record;
- retired assets incorrectly shown as still exposed.

Document whether each record is corrected, excluded, or retained with an uncertainty flag.

## Event definition and time origin

Define the event as a **reportable main break requiring repair**. Define whether time begins at installation, latest replacement, or latest major rehabilitation. For recurrent failures, decide whether you will model:

- time to first recorded failure only;
- time between failures; or
- a renewal process in which repair partially or fully resets condition.

For this drill, use time to first failure for the survival fit and a documented recurrence assumption for portfolio simulation. Assets still operating at the extract date are right-censored.

## Deterministic baseline

Calculate:

- asset age;
- breaks per mile-year;
- historical repair cost per break;
- age/material risk score;
- consequence score; and
- deterministic priority score.

The deterministic ranking is a control and comparison—not the final recommendation.

## Survival model

Fit or specify a Weibull model by material group where data support it:

\[
S(t)=\exp\left[-\left(\frac{t}{\eta}\right)^\beta\right]
\]

where \(\eta\) is the scale and \(\beta\) is the shape. Interpret \(\beta\):

- \(\beta<1\): decreasing hazard;
- \(\beta=1\): constant hazard; and
- \(\beta>1\): increasing hazard.

If the synthetic sample is too small for a defensible material-specific fit, pool groups or use judgmental parameters and state that choice. Optionally compare the parametric curve with a Kaplan–Meier estimate.

## Python simulation

Run at least 20,000 portfolio trials over ten years. For each asset:

1. condition the failure distribution on survival to its current age;
2. sample the remaining time to failure;
3. sample repair duration and cost if a failure occurs;
4. apply consequence based on criticality and service population;
5. apply the selected replacement strategy and reset assumptions; and
6. record failures, emergency cost, and consequence by year.

Do not sample a new lifetime from age zero for an asset that has already survived 60 years. Use conditional survival or an equivalent residual-life method.

## Required outputs

- one-, five-, and ten-year segment failure probabilities;
- P10, P50, and P90 time to next portfolio failure;
- expected failures by year;
- expected and P90 emergency-repair cost;
- probability of at least one critical-segment failure;
- expected customer interruption consequences;
- risk reduction and cost per avoided critical failure;
- prioritized renewal list.

## Quality-control checks

- Exposure begins after installation or replacement.
- Retired assets stop accumulating exposure.
- Active assets without a break remain in the censored dataset.
- Sampled residual life is nonnegative.
- Simulated survival matches the selected Weibull curve within Monte Carlo error.
- Portfolio totals reconcile to the cleaned asset inventory.
- Replacement occurs before the avoided failure to receive credit.
- The same underlying failure scenarios are used for strategy comparisons where feasible.
- A one-year probability is not multiplied by ten and labeled a ten-year probability.

## Interpretation questions

1. How does conditioning on current age change remaining life?
2. Does the highest failure probability identify the highest-priority segment?
3. Which uncertainty matters more: failure timing, repair cost, or consequence?
4. What additional data would most improve the survival model?
5. How should repeat-break history affect the renewal recommendation?

## Brief solution checkpoint

The model should retain no-break assets as censored observations and condition future life on current age. A strong result will distinguish high failure probability from high consequence and will not automatically replace the oldest pipe. Strategy C should demonstrate whether targeted renewal reduces critical risk more efficiently than age-first replacement.

---

# Drill 3 — Lift-station pump-fleet reliability

## Decision scenario

A lift station has three nominally identical pumps. Two can meet peak firm-capacity requirements; the third is installed standby. Failures, preventive maintenance, repair logistics, wet-weather demand, and selected common-cause events can make the standby unavailable when needed.

Compare:

- **Strategy A:** reactive maintenance with standard repair response;
- **Strategy B:** enhanced preventive maintenance that lengthens typical time to failure but adds planned downtime; and
- **Strategy C:** standard maintenance with expedited parts and repair response.

## Synthetic source files

- `pump_runtime_dirty.csv`
- `pump_work_orders_dirty.csv`
- `pump_capacity_tests_dirty.csv`
- `wet_weather_events_dirty.csv`

### Required data defects

- runtime meters that reset after replacement;
- duplicate work-order numbers;
- failure and preventive work mixed under `maintenance`;
- open work orders with blank return-to-service dates;
- negative repair durations from date-entry errors;
- pump names changing after motor replacement;
- capacities recorded in gpm and MGD;
- overlapping outage intervals;
- zero runtime during telemetry outages;
- failures recorded by calendar date but exposure recorded in runtime hours.

## Deterministic baseline

Calculate:

- mean time between failures;
- mean time to repair;
- simple component availability;
- expected available pumps; and
- firm capacity with the largest unit unavailable.

For a basic repairable component:

\[
A=\frac{MTBF}{MTBF+MTTR}
\]

This formula is a baseline only. It does not capture common-cause events, planned maintenance, weather-dependent demand, or the timing overlap of outages.

## Event model

Use an event-driven simulation or sufficiently fine daily time steps. Model:

- pump operating-hour accumulation;
- pump-specific time to failure;
- repair duration;
- planned maintenance windows;
- wet-weather demand events;
- reduced capacity from degradation; and
- a low-frequency common-cause event affecting multiple pumps.

Open work orders are censored repair durations at the extract date. Active pumps without failure are censored time-to-failure observations.

## Python simulation

Run at least 15,000 one-year histories for each strategy with common random scenarios. Record every change in state: available, running, standby, planned outage, failed, and under repair.

A capacity-deficit event occurs when available tested capacity is below required demand. Merge consecutive deficit time steps into one event before counting events.

## Required outputs

- probability of at least one capacity-deficit event;
- expected deficit-event count;
- expected, P50, and P90 deficit duration;
- P50 and P90 pump-unavailability hours;
- probability the standby is unavailable when demanded;
- percentage of risk attributable to common-cause events;
- strategy cost and risk reduction.

## Quality-control checks

- Runtime-meter resets do not create negative exposure.
- Failure and preventive-maintenance events are separated.
- Overlapping outages are not double-counted.
- A failed pump cannot run or accumulate normal operating hours.
- Repair completion occurs after failure.
- Available capacity equals the sum of available tested pump capacities.
- Consecutive deficit periods are counted consistently.
- The deterministic availability is approximately reproduced when weather and common-cause logic are disabled.
- Common random scenarios are used across strategies.

## Interpretation questions

1. Does enhanced preventive maintenance reduce failures enough to offset planned downtime?
2. Is failure frequency or repair duration the more actionable driver?
3. How much risk comes from common-cause events that an additional identical standby may not solve?
4. When would a rental-pump contract be more valuable than additional preventive work?
5. What level of reliability is operationally acceptable?

## Brief solution checkpoint

The simple availability calculation should be close to the stripped-down simulation but will understate interactions among demand, planned downtime, and common-cause events. Expedited repair should primarily reduce event duration; preventive maintenance should primarily alter failure timing. The recommendation must identify which aspect of risk management values most.

---

# Drill 4 — Director decision: renewal budget and service risk

## Decision scenario

A municipal engineering director must recommend a three-year renewal program across:

- water-main segments;
- lift-station pumps;
- standby generators and transfer switches; and
- selected control panels.

The annual planned-renewal budget is constrained, and an emergency reserve is available but limited. The director must choose among three allocation strategies:

- **Strategy A — Age first:** fund the oldest eligible assets.
- **Strategy B — Deterministic risk score:** fund the highest probability-times-consequence score.
- **Strategy C — Survival-risk optimization:** prioritize assets based on simulated near-term failure timing, consequence, cost, and budget fit.

This is a planning drill, not a full mathematical optimization requirement. A ranked selection heuristic is acceptable if constraints and tie-breaking rules are explicit.

## Synthetic source files

- `asset_portfolio_dirty.csv`
- `condition_inspections_dirty.csv`
- `failure_cost_history_dirty.csv`
- `renewal_cost_estimates_dirty.csv`
- `service_consequence_dirty.csv`

### Required data defects

- duplicate asset records across departmental exports;
- missing commissioning dates;
- condition scores using both 1–5 and 1–10 scales;
- inconsistent consequence categories;
- replacement costs from different estimate years;
- emergency costs with and without internal labor;
- assets already replaced but still marked active;
- parent and child assets that could be double-counted;
- blank failure dates for active assets;
- projects that bundle multiple assets under one cost.

Create an asset master table with one row per decision unit. Document how bundled projects and parent-child assets are handled.

## Deterministic baseline

For every asset, calculate:

- age;
- condition score on a common scale;
- deterministic probability category;
- consequence score;
- risk score;
- planned replacement cost; and
- preliminary funding year.

Apply annual budget constraints and show which assets are deferred. This baseline should be fully reproducible before Monte Carlo is added.

## Survival and consequence assumptions

Assign or estimate asset-class survival models. Condition the remaining-life distribution on current age and, when defensible, inspection condition. Model:

- first failure time;
- emergency repair or replacement cost;
- outage duration;
- service, environmental, safety, and reputational consequence;
- planned replacement time;
- cost escalation; and
- the possibility that a planned project is delayed.

Avoid counting condition twice. If condition modifies the survival distribution, do not also apply an unexplained condition multiplier to the same probability.

## Python simulation

Run at least 20,000 three-year portfolio trials. Use the same latent asset-failure scenarios for all strategies. In each trial:

1. sample residual failure time and consequence severity for every asset;
2. schedule planned projects subject to annual budget;
3. apply construction-delay uncertainty;
4. determine whether failure occurs before replacement;
5. record planned and emergency expenditures in the correct fiscal year;
6. apply emergency-reserve limits; and
7. calculate service-risk metrics.

If a failure triggers immediate replacement, avoid charging both a full emergency replacement and the unchanged planned replacement later.

## Required outputs

- expected and P90 total three-year cost;
- expected critical failures;
- probability of at least one high-consequence failure;
- probability annual emergency spending exceeds reserve;
- probability annual total spending exceeds authorized capacity;
- expected service-interruption hours or equivalent consequence units;
- planned versus emergency spending by year;
- assets most frequently involved in adverse trials;
- recommended allocation strategy and reserve.

## Quality-control checks

- Portfolio counts and costs reconcile to the cleaned asset master.
- Replacement costs use a common price basis before escalation.
- Parent-child assets are not double-counted.
- Residual-life distributions are conditioned on current survival.
- Failure after planned replacement is governed by the replacement assumption.
- An asset cannot be both fully emergency-replaced and fully planned-replaced in the same horizon.
- Annual budget and reserve constraints are enforced in every trial.
- Common random scenarios are used across strategies.
- Removing uncertainty reproduces the deterministic funding plan.
- Strategy rankings are stable under alternate seeds and a higher trial count.

## Interpretation questions

1. Which strategy best reduces high-consequence failures per dollar?
2. Does the lowest expected cost also have acceptable P90 cost and service risk?
3. Which assets repeatedly cause adverse outcomes despite a modest deterministic score?
4. How much emergency reserve is justified, and what risk tolerance supports it?
5. Which inspection or failure-history improvement would most change the capital plan?

## Brief solution checkpoint

Age-first allocation should be easy to explain but may spend money on old, low-consequence assets. A deterministic risk score should improve targeting but can conceal timing and budget interactions. The survival-risk strategy should demonstrate whether it reduces the probability of near-term, high-consequence failure within the same budget. The director memo should recommend a strategy, a reserve amount, and specific assets requiring better information before authorization.

---

# Weekly synthesis

Complete this comparison after the four drills:

| Question | Debt/refinancing | Water mains | Pump fleet | Renewal portfolio |
|---|---|---|---|---|
| Event | Breach or delayed closing | Main break | Capacity deficit | Failure before renewal |
| Time origin | Forecast start/application | Installation or replacement | Return to service/runtime | Current planning date |
| Censoring | No breach/open case | Active unfailed pipe | Active pump/open repair | Active asset without failure |
| Key tail metric | Late-close probability | Critical failure probability | P90 deficit duration | P90 cost and high-consequence risk |
| Management action | Start earlier/hold liquidity | Target renewal | Change maintenance/repair support | Reallocate capital/reserve |

Finish with a short reflection answering:

1. Which drill was most sensitive to the definition of the event?
2. Where did censoring materially affect the conclusion?
3. Where was expected value less useful than event probability or event timing?
4. What did the deterministic baseline miss that the time-to-event simulation revealed?

