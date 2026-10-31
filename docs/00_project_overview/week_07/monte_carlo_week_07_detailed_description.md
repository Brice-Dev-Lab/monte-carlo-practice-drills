# Week 7 Monte Carlo Modeling Drills — Detailed Description

## Main concept: correlated inputs and multivariate sampling

Many risks share a common cause. Equity sectors move together, deteriorated pumps lose both head and efficiency, heavy rainfall raises several electrical loads at once, and project complexity increases hours across multiple disciplines. Sampling those variables independently can create implausible combinations and materially misstate risk.

This week you will model **joint behavior**. The emphasis is not merely producing a correlation matrix; it is understanding what creates the relationship, preserving it during simulation, and checking that the simulated data reproduce it.

Use random seed `20261024` for the primary run. Keep alternate-seed testing separate.

## Suggested work plan

| Session | Work | Time budget |
|---|---|---:|
| 1 | Finance Excel setup, cleaning, and baseline | 35 min |
| 2 | Finance Python simulation and Excel dashboard | 55 min |
| 3 | Force-main baseline and simulation | 75 min |
| 4 | Generator adequacy | 60 min |
| 5 | Fee/margin risk and weekly comparison | 75 min |
| Buffer | Documentation and corrections | 20–30 min |

---

# Drill 1 — Multi-asset portfolio risk

## Scenario

A finance committee is considering the following long-term allocation for a $250,000 reserve portfolio:

| Asset proxy | Weight |
|---|---:|
| SPY — U.S. equities | 45% |
| BND — investment-grade bonds | 30% |
| VNQ — real estate | 15% |
| GLD — gold | 10% |

Use monthly adjusted prices for approximately ten years. Yahoo Finance is optional; a synthetic file is acceptable. If downloading prices, freeze the extracted file and record the extraction date so the analysis remains reproducible.

## Realistic data defects

Include or expect at least six of the following:

- duplicate ticker/date rows;
- mixed date formats;
- one missing adjusted price;
- numeric prices stored with currency symbols or commas;
- inconsistent ticker capitalization or trailing spaces;
- a non-month-end observation mixed into month-end data;
- an asset beginning later than the others;
- rows sorted newest-to-oldest;
- a return calculated across a missing month;
- both adjusted and unadjusted prices without a clear label.

Do not silently fill missing prices. First determine whether the issue is a true missing observation, a market-calendar alignment issue, or an invalid record.

## Excel starting workbook

Create these sheets:

1. `Raw_Prices` — unchanged source data.
2. `Clean_Prices` — one adjusted month-end price per ticker.
3. `Monthly_Returns` — aligned simple or log returns; state your choice.
4. `Assumptions` — weights, initial value, horizon, seed, model choices.
5. `Baseline` — historical means, volatilities, correlations, and deterministic result.
6. `Simulation_Summary` — values exported from Python.
7. `Sensitivity` — correlated versus independent results.
8. `Dashboard` — management-facing output.

The weights must sum to exactly 100%. Use formulas rather than pasted values for the baseline calculations.

## Deterministic baseline

Calculate:

\[
\mu_p = w^T\mu
\]

\[
\sigma_p = \sqrt{w^T\Sigma w}
\]

Show the expected one-year ending value using your stated annualization convention. The baseline is not a forecast guarantee; it is a controlled reference point for validating the Python implementation.

## Python simulation

Use at least 20,000 trials and 12 monthly steps. Implement three cases:

### Model A — Paired historical-row bootstrap

Sample complete monthly return rows. Because each selected row contains all four asset returns from the same month, cross-asset dependence is retained without explicitly fitting a distribution.

### Model B — Multivariate normal

Estimate the monthly mean vector and covariance matrix, then generate joint monthly returns. Document whether you use arithmetic or log returns and apply compounding consistently.

### Model C — Independence test

Sample each asset separately or set off-diagonal covariances to zero. This is a diagnostic comparison, not the preferred portfolio model.

For each path, calculate monthly portfolio returns, ending value, and maximum drawdown. Do not allow rebalancing assumptions to remain implicit: specify monthly rebalancing or buy-and-hold.

## Required results

- mean, P10, P50, and P90 ending value;
- probability ending value is below $250,000;
- 95% one-year value at risk;
- 95% expected shortfall;
- P50 and P90 maximum drawdown;
- historical and simulated correlation matrices;
- difference in loss probability between correlated and independent cases.

Define the signs for value at risk and expected shortfall clearly. For example, report both as positive dollar losses.

## Excel dashboard

Build a single-screen dashboard containing:

- portfolio allocation;
- ending-value percentile cards;
- probability of loss;
- VaR and expected shortfall;
- ending-value histogram;
- drawdown chart;
- correlated-versus-independent comparison;
- a three-sentence management conclusion.

Avoid presenting expected return without downside measures.

## Quality-control checks

- The common return table has one row per month and no duplicate ticker/date keys.
- Returns are not calculated over an unintended multi-month gap.
- The covariance matrix is symmetric and positive semidefinite.
- Python reproduces Excel's baseline mean and volatility within rounding tolerance.
- Simulated correlations are reasonably close to their targets.
- No simulated simple return is less than or equal to -100%; if this occurs, revise the modeling method.
- The primary loss probability is stable when trials increase from 10,000 to 20,000.
- Model comparisons use the same horizon, weights, and initial value.

## Interpretation questions

1. Which diversification benefit disappears when correlations increase?
2. Does the independent model understate or overstate downside risk, and why?
3. Which simulation method better reflects fat tails in the historical sample?
4. Would the recommendation change if the committee cared primarily about drawdown?

## Brief solution checkpoint

A successful result will show that both models reproduce a sensible central estimate but may produce materially different tail risk. The row bootstrap should retain observed joint market moves. The independent case will usually appear better diversified when harmful co-movement is removed. Your dashboard should state whether the allocation satisfies a clearly defined risk tolerance, not merely identify the model with the highest mean.

---

# Drill 2 — Force-main hydraulic performance

## Scenario

An existing wastewater pump station discharges through approximately 18,000 ft of 24-in force main. Operations wants to know the probability that the station can deliver at least 4,500 gpm during the planning condition while maintaining velocity between 2 and 8 ft/s.

Available synthetic records include pump-test flow, suction and discharge pressure, wet-well level, downstream hydraulic grade, pump speed, pump status, pipe segment information, and maintenance history.

## Realistic data defects

- pressure reported in both psi and feet of water;
- flow reported in gpm and MGD;
- duplicate timestamps from historian exports;
- missing pump-status values;
- pump speed stored as text such as `95 %`;
- impossible negative gauge pressure;
- stale sensor values repeated over many timestamps;
- pipe diameter recorded as nominal diameter in one table and estimated inside diameter in another;
- inconsistent asset IDs;
- daylight-saving-time duplicate timestamps.

Flag invalid observations rather than automatically clipping them.

## Deterministic baseline

Construct the system curve as static head plus friction and minor losses. A planning-level Hazen–Williams representation may be used:

\[
h_f = 4.52\frac{LQ^{1.85}}{C^{1.85}d^{4.87}}
\]

Use consistent U.S. customary units for the coefficient above. Add static head and minor losses to obtain total dynamic head. Fit or use a pump curve, then solve numerically for the pump/system intersection.

Record the baseline values for pipe inside diameter, length, Hazen–Williams coefficient, static head, minor-loss coefficient, pump-curve coefficients, and speed.

## Uncertain inputs and relationships

Create defensible bounded distributions for:

- force-main inside diameter;
- Hazen–Williams coefficient;
- static head;
- minor-loss coefficient;
- pump shutoff head and curve coefficient;
- speed or degradation factor;
- wet-weather demand condition.

Represent at least two dependencies. Examples:

- older or more deteriorated conditions produce both lower `C` and reduced effective diameter;
- pump degradation reduces shutoff head and capacity together;
- downstream level and wet-weather demand rise together.

You may generate correlated normal scores and transform them to bounded marginals, or use a shared latent-condition variable. Explain the physical reason for each dependence.

## Python simulation

Run at least 20,000 trials. For every trial:

1. sample the joint input vector;
2. build the system and pump curves;
3. solve the operating point within a physically valid flow bracket;
4. calculate total dynamic head and velocity;
5. store a solver-failure flag rather than discarding failed trials.

Repeat the model with independent inputs while leaving all marginal distributions unchanged.

## Required results

- P10, P50, and P90 operating flow;
- P10, P50, and P90 total dynamic head;
- probability operating flow is below 4,500 gpm;
- probability velocity is below 2 ft/s or above 8 ft/s;
- solver-failure rate;
- risk difference between correlated and independent cases;
- ranked influence measures for capacity shortfall.

## Quality-control checks

- Convert all pressure and flow values to one unit system before fitting.
- Confirm the baseline operating point visually on a pump/system curve plot.
- Hand-calculate friction loss and velocity for one trial.
- Reject or flag nonphysical input combinations before solving.
- Confirm that the bracketing interval contains a sign change.
- Compare sampled and target rank correlations.
- Include solver failures in the audit trail.
- Check whether the capacity result stabilizes by 20,000 trials.

## Interpretation questions

1. Which shared condition creates the most important dependency?
2. Why does a lower `C` combined with a smaller effective diameter matter more than either change alone?
3. Would an average operating point be sufficient for this decision?
4. What field measurement would most reduce decision uncertainty?

## Brief solution checkpoint

The deterministic solution should fall at the pump/system intersection and be reproducible before simulation. A credible probabilistic result will show a nonzero lower-tail capacity risk and explain whether correlated deterioration increases it. If correlation has almost no effect, verify that the chosen relationships actually reach the hydraulic calculation and are not lost during sampling.

---

# Drill 3 — Lift-station standby-generator adequacy

## Scenario

A municipal lift station has multiple pumps, ventilation, controls, lighting, heat tracing, and miscellaneous auxiliary loads supplied by a standby generator. Management wants a planning-level estimate of overload risk during wet-weather operation and a comparison of two mitigations.

The analysis must distinguish running kW, running kVA, and temporary motor-starting demand.

## Realistic data defects

- horsepower and kW mixed in the same rating column;
- missing or percent-formatted power factors;
- duplicate equipment records;
- status values such as `ON`, `1`, `Running`, and blanks;
- VFD and across-the-line starting methods inconsistently labeled;
- motor efficiency missing for selected assets;
- auxiliary loads recorded as both connected and measured values;
- overlapping timestamps with different pump combinations;
- zero readings during known communication outages.

Create an issue log that distinguishes correctable formatting problems from missing engineering assumptions.

## Deterministic baseline

For each motor, estimate running input power consistently. A simplified calculation is:

\[
kW_{in}=\frac{hp\times0.746}{\eta}
\]

and:

\[
kVA=\frac{kW}{PF}
\]

Calculate the normal running load and the largest planned starting step under the documented starting sequence. Do not add every motor's starting load simultaneously unless simultaneous starting is a credible control state.

## Uncertain inputs and relationships

Model uncertainty in:

- pump operating combination;
- motor efficiency and power factor;
- measured auxiliary load;
- starting multiplier by starting method;
- generator available capacity under ambient and maintenance conditions;
- wet-weather operating state.

Use wet-weather severity as a shared driver of pump count, ventilation demand, and miscellaneous load. If generator derating is modeled, state its basis as an assumption rather than a code requirement.

## Python simulation

Run at least 15,000 scenarios for:

1. existing controls;
2. sequential motor starting; and
3. one load-shedding option, if distinct from sequential starting.

Use common random scenarios so the mitigation comparison is not obscured by Monte Carlo noise.

## Required results

- P50 and P90 running kW and kVA;
- probability running kW exceeds 80% of available generator kW;
- probability running kVA exceeds the planning threshold;
- probability modeled starting demand exceeds the selected transient limit;
- most frequent equipment combination in exceedance trials;
- absolute and relative risk reduction from each mitigation.

## Quality-control checks

- Do not double-count connected and measured auxiliary loads.
- Keep kW and kVA in separate fields.
- Constrain efficiency and power factor to physically plausible ranges.
- Confirm that pump count agrees with the sampled operating state.
- Inspect one dry-weather and one wet-weather scenario by hand.
- Use the same random scenarios for mitigation comparisons.
- Reconcile total load to the component-level sum.

## Interpretation questions

1. Is running load or starting demand the controlling condition?
2. Which dependency would be missed by sampling equipment states independently?
3. Does a low average load prove the generator is adequate?
4. What manufacturer or electrical-study information is needed before design approval?

## Brief solution checkpoint

The existing configuration should have a traceable component-level load balance. Wet-weather trials should produce realistic coincidence among pumps and auxiliaries. Sequential starting should affect transient risk but may not reduce steady running demand; load shedding can affect both depending on the selected loads. State clearly that this is a planning screen requiring electrical-engineer and manufacturer confirmation.

---

# Drill 4 — Director decision: design fee and margin risk

## Scenario

A consulting team is pricing a multidisciplinary municipal design assignment. The proposed scope includes project management, civil/site, process/mechanical, structural, electrical/instrumentation, permitting, and construction-cost estimating. The director must decide whether the proposed fee provides enough protection against shared complexity, rework, schedule extension, wage escalation, and subcontractor cost.

Set a target operating margin of 15%. Compare:

- Option A — current proposed fee;
- Option B — risk-adjusted fixed fee;
- Option C — phased authorization or allowance for poorly defined scope.

## Realistic data defects

- estimated and actual hours in different column structures;
- inconsistent discipline names;
- labor rates stored as currency text;
- cancelled projects mixed with completed projects;
- change-order hours included in actuals but not identified;
- duplicate employee-week records;
- missing completion dates;
- subcontractor cost entered both gross and net of markup;
- project fees stored in nominal dollars from different years;
- percentage fields stored as text.

Create a cleaned project-level table and retain a reconciliation back to source totals.

## Deterministic baseline

Build the fee model using one consistent cost basis—preferably fully loaded labor rates plus separately identified subcontractor and direct expenses. Avoid applying overhead twice.

Calculate:

- baseline discipline hours and labor cost;
- subcontractor and direct expense;
- total delivery cost;
- fee revenue;
- dollar margin and margin percentage.

Define margin explicitly:

\[
Margin\%=\frac{Fee-Delivery\ Cost}{Fee}
\]

## Uncertain inputs and relationships

Model at least these drivers:

- discipline-level hours;
- common design-complexity factor;
- rework event and rework severity;
- schedule extension;
- wage or loaded-rate escalation;
- subcontractor cost;
- scope-growth event.

Use a shared complexity factor so civil, process, structural, and electrical hours rise together on difficult projects. Link project-management hours to total technical effort or schedule duration. Make rework conditional: first sample whether it occurs, then sample severity only when it occurs.

## Python simulation

Run at least 20,000 trials. Apply the same sampled project scenarios to all three commercial options. Option C may transfer or limit a specified risk, but you must model exactly which cost is excluded, authorized later, or covered by an allowance.

## Required results

- mean and P80 delivery cost;
- mean, P10, and P50 margin percentage;
- probability margin is below 10%;
- probability margin is negative;
- fee required to achieve a stated confidence of at least 15% margin;
- management reserve for the current fee, if fee cannot change;
- leading risk drivers and proposed contractual or scope controls.

## Quality-control checks

- Reconcile cleaned historical totals to source data.
- Exclude or separately label cancelled and incomplete projects.
- Use one inflation basis and one cost basis.
- Verify that overhead and subcontractor markup are not double-counted.
- Confirm the input correlation matrix is positive semidefinite.
- Ensure conditional costs equal zero when their triggering event does not occur.
- Use common random scenarios for all options.
- Hand-calculate one simulated project.
- Test convergence of the below-10%-margin probability.

## Interpretation questions

1. Which risk is best priced into the fee, and which is better controlled through scope language?
2. How does correlation among discipline hours change required reserve?
3. Is the expected margin sufficient if the downside probability is unacceptable?
4. What is the tradeoff between a higher fixed fee and phased authorization?

## Brief solution checkpoint

A strong recommendation will not simply add a blanket contingency. It will identify the correlated cost drivers, quantify the chance of missing the margin target, and match each risk to a response: fee, allowance, phase gate, client assumption, or management reserve. Option comparisons must use identical underlying scenarios. The director memo should state a recommended commercial position and the probability-based evidence supporting it.

---

# Weekly synthesis

After all four drills, prepare a short comparison table:

| Question | Portfolio | Force main | Generator | Fee/margin |
|---|---|---|---|---|
| What creates dependence? | Market factors | Shared deterioration and wet weather | Coincident operating state | Shared project complexity |
| What decision metric matters? | Loss and drawdown | Capacity shortfall | Overload/start exceedance | Margin shortfall |
| What happens if independence is assumed? | Diversification may be overstated | Joint poor conditions may be missed | Coincident loads may be understated | Tail delivery cost may be understated |
| What action follows? | Change allocation or risk limit | Collect data or improve capacity | Change controls or generator plan | Adjust fee, reserve, or scope terms |

Finish with three sentences:

1. where correlation had the largest decision impact;
2. where the dependence assumption was most uncertain; and
3. which additional observation would create the greatest value of information.

