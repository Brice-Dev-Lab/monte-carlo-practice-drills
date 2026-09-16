# Monte Carlo Modeling Drills

## Project Overview

### Purpose

This project develops practical skill in Monte Carlo simulation through applied finance and municipal-engineering problems. The emphasis is not merely on generating random numbers; it is on building defensible models that:

- represent uncertainty with appropriate probability distributions;
- preserve realistic relationships among variables;
- produce reproducible results;
- communicate ranges, probabilities, and decision risk clearly; and
- support a recommendation rather than pretending to predict one exact future.

The normal schedule is **four drills per week**, consisting of two finance drills and two municipal-engineering drills. A lighter week may use two or three drills, while an intensive week may add a fifth integration or review drill.

### Recommended Time Commitment

| Drill type | Typical time |
|---|---:|
| Guided introductory drill | 45–60 minutes |
| Standard applied drill | 60–90 minutes |
| Integrated Excel/Python/dashboard drill | 90–150 minutes |
| Weekly review and interpretation | 20–30 minutes |

## Learning Objectives

By completing the project, the learner should be able to:

1. Distinguish deterministic, scenario, sensitivity, and Monte Carlo models.
2. Identify which inputs are genuinely uncertain and which should remain fixed.
3. Select and justify distributions using data, engineering judgment, or published assumptions.
4. Clean imperfect finance and engineering datasets before modeling.
5. Estimate distribution parameters without mistaking historical estimates for certainty.
6. Model correlation and basic dependency among uncertain inputs.
7. Run reproducible simulations in Python using a controlled random-number generator.
8. Validate simulations with reasonableness checks, convergence checks, and deterministic comparisons.
9. Interpret percentiles, confidence intervals, exceedance probabilities, and downside risk.
10. Present conclusions in Excel dashboards for decision-makers.

## Weekly Format

The recommended four-drill rotation is:

| Drill | Domain | Primary emphasis |
|---|---|---|
| 1 | Finance | Excel model setup, uncertainty definition, and input assumptions |
| 2 | Municipal engineering | Data cleaning, distribution selection, and exceedance risk |
| 3 | Finance | Python simulation, risk measures, and Excel dashboard |
| 4 | Municipal engineering | Reliability, cost/schedule risk, or lifecycle decision-making |

An optional fifth drill may be used for model review, sensitivity analysis, correlation, back-testing, or an executive-summary challenge.

## Standard Workflow

### Finance Applications: Excel to Python to Excel

1. **Start in Excel**
   - Inspect and clean the raw data.
   - Build the deterministic base-case model.
   - Separate assumptions, calculations, and outputs.
   - Identify uncertain inputs and document distribution choices.
   - Establish control totals and base-case results for later validation.

2. **Run the simulation in Python**
   - Import the cleaned Excel inputs.
   - Perform any additional validation or cleaning.
   - Fit or define probability distributions.
   - Model correlations or conditional relationships when appropriate.
   - Run the Monte Carlo simulation with a reproducible seed.
   - Calculate percentiles, probability of loss, expected value, downside measures, and sensitivity statistics.
   - Export simulation summaries and selected trial-level data to Excel.

3. **Finish in Excel**
   - Refresh the exported results.
   - Build a management-facing dashboard.
   - Compare deterministic and probabilistic results.
   - Explain the principal risk drivers.
   - State a decision or recommendation in plain language.

### Municipal-Engineering Applications: Data to Python to Decision Summary

1. Inspect and clean field, operational, cost, schedule, or asset-condition data.
2. Define the engineering decision and measurable failure or exceedance condition.
3. Establish a deterministic baseline calculation.
4. Define uncertain inputs, units, bounds, dependencies, and distributions.
5. Run and validate the simulation in Python.
6. Summarize expected results, percentiles, failure probability, and leading risk drivers.
7. Present the result in an Excel summary, technical figure, or decision memo appropriate to the drill.

## Data Standards

Each drill should begin with data that resembles real working data and requires cleaning. Problems may use supplied simulated data or market data obtained through an API.

### Expected Data-Quality Issues

Datasets should include several of the following:

- inconsistent dates or reporting periods;
- missing observations;
- duplicated records;
- numeric values stored as text;
- inconsistent units;
- incorrect signs or accounting conventions;
- category-name inconsistencies;
- impossible or physically implausible values;
- outliers requiring investigation rather than automatic deletion;
- censored values or detection limits;
- stale assumptions;
- misaligned time series;
- changes in asset IDs, account names, or ticker symbols.

### Synthetic Data Requirements

Supplied data should be realistic but clearly identified as synthetic. The generator should preserve plausible ranges, seasonality, trends, skew, correlations, operational constraints, and occasional data-quality defects. A clean reference version may be retained for checking, but it should not be the learner's starting file.

### Market Data Option

Finance drills may retrieve adjusted prices, dividends, or other market fields for specified tickers through Yahoo Finance. Because external data formats and availability can change, each such drill should include:

- a defined date range and frequency;
- a saved raw-data snapshot;
- validation for missing dates and fields;
- explicit treatment of adjusted versus unadjusted prices;
- return calculations performed by the learner; and
- a synthetic fallback dataset so the drill remains reproducible.

## Model-Building Standards

Every completed simulation should include:

- a clearly stated decision question;
- a deterministic base case;
- an input dictionary with units and sources;
- a justification for every selected distribution;
- documented bounds or truncation where appropriate;
- explicit treatment of correlations and dependencies;
- a reproducible random seed;
- a stated number of trials;
- a convergence or stability check;
- validation against the deterministic model or known relationships;
- percentile and exceedance results;
- sensitivity or risk-driver analysis; and
- limitations and a management recommendation.

The model should not use a normal distribution by default merely because it is convenient. Distribution choice must reflect the variable's behavior, available evidence, and physical or financial constraints.

## Suggested Technical Stack

### Excel

- Excel Tables and structured references
- Power Query for repeatable cleaning and imports
- named assumptions or clearly labeled input cells
- PivotTables and PivotCharts where useful
- charts, slicers, conditional formatting, and KPI cards
- optional Data Model/Power Pivot for larger outputs

### Python

- Python 3.12
- `numpy`
- `pandas`
- `scipy`
- `openpyxl` or `xlsxwriter`
- `matplotlib` and/or `seaborn`
- `yfinance` for optional ticker-based exercises
- `statsmodels` when time-series diagnostics are needed

Python simulations should normally use `numpy.random.default_rng(seed)` rather than global random state.

## Core Deliverables for Each Drill

Each drill should produce:

1. `README.md` or drill instructions containing the scenario and decision question.
2. A raw CSV or Excel dataset containing realistic data-quality defects.
3. A cleaned dataset or repeatable cleaning process.
4. A deterministic baseline model.
5. A documented assumptions table.
6. A Python notebook or script that runs the simulation.
7. A simulation-results file suitable for Excel import.
8. A final dashboard, technical summary, or decision memo.
9. A short interpretation answering the decision question.
10. A model-validation checklist.

## Finance Drill Themes

### 1. Portfolio Return and Downside Risk

- Import historical prices for two to five assets or use synthetic prices.
- Clean missing dates, duplicate observations, and ticker changes.
- Calculate periodic returns in Excel and validate them in Python.
- Simulate correlated returns.
- Estimate portfolio return, volatility, probability of loss, VaR, and expected shortfall.
- Build an Excel dashboard showing allocation, simulated outcomes, downside risk, and key drivers.

### 2. Small-Business Revenue and Cash Forecast

- Begin with messy invoice, collections, payroll, and expense data.
- Build a deterministic 13-week cash-flow forecast in Excel.
- Simulate sales volume, invoice timing, collection delays, churn, and selected costs in Python.
- Estimate minimum cash, probability of a cash shortfall, and timing of peak borrowing need.
- Finish with an Excel cash-risk dashboard and recommendation.

### 3. DCF Valuation Under Uncertainty

- Build the base DCF in Excel.
- Simulate revenue growth, margins, working capital, capital expenditures, terminal growth, and discount rate.
- Include reasonable dependencies, such as weaker growth with lower margins or higher risk with a higher discount rate.
- Report valuation percentiles and probability of falling below a target value.
- Finish with a valuation distribution and risk-driver dashboard in Excel.

### 4. Hiring or Expansion Decision

- Model demand, billable utilization, price, compensation, hiring date, ramp-up time, and collections.
- Estimate probability of positive incremental NPV and probability of a cash squeeze.
- Compare immediate, staged, and delayed hiring strategies.
- Present the recommendation in Excel for a small-business owner.

### 5. Capital-Budget Cost and Schedule Risk

- Model uncertain construction cost, implementation delay, operating savings, financing cost, and useful life.
- Compare deterministic NPV/IRR with simulated outcomes.
- Identify the probability that the project misses its hurdle rate or budget.

## Municipal-Engineering Drill Themes

### 1. Peak-Flow and Capacity Exceedance

- Clean historical annual peak-flow or rainfall records.
- Compare empirical resampling with a fitted probability distribution.
- Simulate future annual peaks.
- Estimate the probability that a culvert, channel, pump station, or pipeline capacity is exceeded over a selected planning horizon.
- Discuss the difference between annual exceedance probability and cumulative project-life risk.

### 2. Water-Demand and Storage Reliability

- Clean hourly or daily demand, tank-level, and pump-operation data.
- Model base demand, peak factors, seasonal effects, fire-flow events, and pump outages.
- Estimate probability of violating minimum storage or pressure criteria.
- Compare operational or capital alternatives.

### 3. Construction Cost Contingency

- Start with a messy bid-item estimate and historical unit-price dataset.
- Simulate quantities, unit prices, escalation, change orders, and correlated market effects.
- Estimate P50, P80, and P90 project costs.
- Recommend a risk-based contingency while explaining what the selected percentile means.

### 4. Project Schedule Risk

- Use uncertain activity durations for design, permitting, procurement, construction, and startup.
- Include dependencies and selected correlated delay drivers.
- Estimate probability of meeting substantial-completion and regulatory deadlines.
- Identify activities contributing most to completion-date uncertainty.

### 5. Asset Failure and Lifecycle Planning

- Clean work-order, age, material, condition, failure, and consequence data.
- Simulate deterioration or failure events and lifecycle costs.
- Compare rehabilitation, replacement, and run-to-failure strategies.
- Produce risk-adjusted capital-prioritization results.

### 6. Force-Main or Pump-Station Performance

- Model uncertain flow, roughness, wet-well levels, minor-loss coefficients, pump-curve variation, and degradation.
- Estimate the distribution of TDH, operating point, velocity, and available capacity.
- Calculate the probability of failing to meet the design condition.
- Use engineering bounds so simulated inputs remain physically plausible.

## Twelve-Week Progression

| Week | Finance drill | Municipal-engineering drill | Monte Carlo concept |
|---:|---|---|---|
| 1 | Single-asset return | Peak-flow exceedance | Random sampling and empirical distributions |
| 2 | Revenue forecast | Construction unit-cost risk | Distribution selection and bounds |
| 3 | Two-asset portfolio | Storage reliability | Percentiles and exceedance probability |
| 4 | 13-week cash forecast | Pump outage and demand | Conditional logic and discrete events |
| 5 | DCF valuation | Project cost contingency | Sensitivity and risk drivers |
| 6 | Hiring decision | Schedule risk | Dependencies and correlation |
| 7 | Multi-asset portfolio | Force-main performance | Correlated inputs and multivariate sampling |
| 8 | Debt/refinancing risk | Asset failures | Event timing and survival concepts |
| 9 | Budget variance forecast | Lifecycle cost | Model calibration and back-testing |
| 10 | Capital investment | Climate/storm scenario | Nonstationarity and scenario mixtures |
| 11 | Integrated small-business model | CIP portfolio risk | Portfolio aggregation and constraints |
| 12 | Executive finance case | Executive engineering case | Validation, communication, and model review |

Each week should include two domain drills from the table plus two shorter companion drills—for example, a data-cleaning challenge, distribution-selection exercise, convergence test, sensitivity analysis, or executive-interpretation prompt.

## Excel Dashboard Requirements for Finance Drills

Each completed finance dashboard should include, as appropriate:

- deterministic base case versus simulated expected result;
- P10, P50, and P90 outcomes, with directionality explained;
- probability of loss, shortfall, covenant breach, or missing a target;
- histogram or cumulative distribution chart;
- sensitivity or risk-driver chart;
- scenario or strategy comparison;
- key assumptions and last-refresh date; and
- a concise management recommendation.

Trial-level output should be limited or placed on a separate sheet so the workbook remains usable. The dashboard should emphasize decisions, not thousands of simulated rows.

## Interpretation Questions

Every drill should end with several questions such as:

1. What decision does the model support?
2. Which result matters most: the mean, median, a percentile, or an exceedance probability—and why?
3. Which two assumptions drive the most uncertainty?
4. What important dependency could materially change the result?
5. What action would reduce risk or improve the decision?
6. What additional data would be most valuable?
7. What should a decision-maker **not** conclude from the simulation?

## Quality-Control Checklist

Before a drill is considered complete, confirm that:

- units and time periods are consistent;
- accounting signs and engineering conventions are correct;
- missing values and outliers were deliberately handled;
- sampled values obey financial and physical constraints;
- correlated inputs are not modeled as independent without justification;
- no input is counted twice;
- formulas reproduce the deterministic control case when uncertainty is removed;
- the simulation is reproducible;
- the chosen trial count is stable enough for the reported metrics;
- tails and failure cases have been inspected;
- the dashboard labels percentiles unambiguously; and
- the recommendation matches the results and acknowledges limitations.

## Suggested Repository Structure

See the [Project Structure](docs/01_structure/00_structure.md) document for a recommended directory layout, naming conventions, and file types.

## Definition of Completion

The project is successful when the learner can independently receive a messy dataset and a decision question, build a defensible deterministic baseline, select and explain uncertain inputs, run and validate a Monte Carlo simulation in Python, return the results to Excel where required, and communicate a useful recommendation without overstating precision.

The final portfolio should contain at least:

- three polished finance simulations with Excel dashboards;
- three polished municipal-engineering simulations;
- one integrated capital-planning or small-business case;
- documented reusable Python simulation utilities; and
- a concise model-validation checklist demonstrating professional judgment.
