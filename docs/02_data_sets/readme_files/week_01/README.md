# Week 1 Monte Carlo Modeling — Dataset Package

## Weekly theme

**From deterministic estimates to distributions of possible outcomes**

This package contains the source data and assumptions for all four Week 1 assignments. The records are synthetic and do not represent an actual investment, company, municipality, drainage crossing, or construction project.

Use random seed `20260914` unless a notebook clearly documents another choice.

## Included workbooks

| File | Assignment | Contents | Intentional issues or limitations |
|---|---|---|---|
| `01_spy_monthly_prices_dirty.xlsx` | Drill 1 — One-asset return and loss risk | 120 months of synthetic SPY-proxy adjusted prices, investment assumptions, and field definitions | unsorted dates, duplicate month, two missing prices, numeric text, provisional final row |
| `02_annual_peak_flows_dirty.xlsx` | Drill 2 — Culvert capacity exceedance | 30 years of annual peak flows, capacity threshold, simulation settings, and field definitions | unsorted years, duplicate year, missing flow, numeric text, inconsistent units, negative flow, provisional observation |
| `03_distribution_choice_inputs_dirty.xlsx` | Drill 3 — Distribution choice challenge | 104 weeks of synthetic new-sales history and a starter assumptions register | unsorted weeks, duplicate record, currency text, missing sales, incomplete assumption choices |
| `04_convergence_contingency_inputs.xlsx` | Drill 4 — Convergence and contingency | Four cost components, triangular multipliers, four trial counts, and five comparison seeds | clean inputs by design; the key modeling limitation is temporary independence among cost components |

Each workbook contains a `Data_Notes` sheet. The relevant fixed assumptions and trial-design inputs are included in additional sheets.

## Recommended project locations

```text
week_01/
├── data/
│   ├── raw/          # store untouched source workbooks here
│   ├── interim/      # standardized working tables
│   └── processed/    # analysis-ready tables and exception logs
├── excel/
├── notebooks/
└── outputs/
```

Preserve the raw workbooks. Perform cleaning in a notebook, Power Query, or a separate clean-data sheet and record every exclusion, correction, and conversion in an exception log.

## Assignment guidance

### Drill 1 — One-asset return and loss risk

Sort and clean the adjusted-price series before calculating simple monthly returns. Bootstrap cleaned returns for at least 10,000 trials of 12 months. Start the analysis in Excel, simulate in Python, and finish with an Excel dashboard showing ending-value percentiles and loss probabilities.

### Drill 2 — Culvert capacity exceedance

Clean the annual peak-flow record and compare valid flows with the 700-cfs planning threshold. Run one-year and ten-year empirical-bootstrap models with 100,000 trials. Validate the ten-year result against `1 - (1 - p)^10`, while clearly stating the independence assumption.

### Drill 3 — Distribution choice challenge

Use the historical weekly sales to compare a normal distribution with a positive-only skewed or bounded alternative. Complete the assumptions register for all five business inputs, including bounds, dependencies, required evidence, ownership, and review dates.

### Drill 4 — Convergence and contingency

Simulate total project cost at 100, 1,000, 10,000, and 100,000 trials. Repeat each count with five supplied seeds. Calculate P80 contingency as the difference between P80 simulated cost and the $5.65 million deterministic base estimate.

## Quality-control checklist

- Preserve raw data and maintain an exception log.
- Calculate returns only after sorting and resolving duplicates.
- Confirm adjusted prices and valid peak flows are positive.
- Exclude or explicitly handle provisional and incomplete observations.
- Hand-check at least one monthly return and one simulated trial.
- Confirm no simulated investment ending values are negative.
- Compare the simulated ten-year exceedance probability with the analytical result.
- Confirm triangular parameters satisfy `low ≤ mode ≤ high`.
- Record seed, trial count, units, horizon, and data period in outputs.
- State that the culvert analysis is planning-level—not a regulatory flood-frequency or hydraulic analysis.
- State that independent construction-cost components are a temporary teaching assumption.
