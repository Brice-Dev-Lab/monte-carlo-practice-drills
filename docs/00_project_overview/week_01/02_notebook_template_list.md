# Notebook Templates and Responsibilities

## Notebook Template List

* `00_data_ingestion.ipynb`
* `01_baseline_analysis.ipynb`
* `02_eda.ipynb`
* `03_feature_engineering.ipynb`
* `04_modeling.ipynb`
* `05_evaluation.ipynb`
* `06_conclusion.ipynb`

---

## Notebook Responsibilities

### 00 - Data Ingestion

**Purpose:** Load the raw data, verify that it was imported correctly, assess basic data quality, perform necessary cleaning, and save a clean dataset for downstream analysis.

Typical workflow:

1. Load the raw data.
2. Inspect the structure.
3. Identify data-quality problems.
4. Correct identified data-quality problems.
5. Validate the cleaned data.
6. Save the cleaned dataset.

| Check / Operation               | Purpose                                                     |
| ------------------------------- | ----------------------------------------------------------- |
| `df.head()`                     | Confirm the file loaded correctly and inspect its structure |
| `df.shape`                      | Record the number of rows and columns received              |
| `df.columns`                    | Inspect and standardize column names                        |
| `df.dtypes` / `df.info()`       | Detect incorrect data types                                 |
| `df.isna().sum()`               | Identify missing values that must be handled or flagged     |
| `df.duplicated().sum()`         | Count duplicate records                                     |
| `df[df.duplicated(keep=False)]` | Inspect the original and duplicated records                 |
| `df.describe()`                 | Perform a basic reasonableness check on numerical values    |
| Cleaning operations             | Correct identified data-quality problems                    |
| Validation checks               | Confirm that cleaning worked as intended                    |
| Save processed data             | Create the clean dataset used by downstream notebooks       |

#### Data-Quality Workflow

Data-quality problems should be **identified before they are corrected**.

For example:

```python
# Identify duplicates
df.duplicated().sum()
df[df.duplicated(keep=False)]

# Remove duplicates after confirming they are unwanted
df = df.drop_duplicates()

# Validate
df.duplicated().sum()
```

The ingestion notebook therefore documents both **what arrived in the raw dataset** and **what was done to make it usable**.

---

### 01 - Baseline Analysis

**Purpose:** Establish a simple, understandable reference point that describes the current or historical condition before performing detailed exploratory analysis or building a more sophisticated model.

The baseline answers:

> **What does the data tell us using simple, established methods before we introduce more advanced analysis?**

The baseline becomes the reference against which later EDA, simulations, forecasts, or predictive models can be compared.

#### Primary Objectives

A baseline analysis should:

* Summarize the most important historical or current conditions.
* Establish representative values using simple calculations.
* Identify the range and scale of the observed data.
* Calculate domain-specific metrics that are already understood and accepted.
* Establish a benchmark for evaluating later modeling results.
* Remain simple enough that the results can be easily explained and reproduced.

#### Typical Baseline Metrics

The appropriate metrics depend on the problem, but may include:

**General**

* Count of usable observations
* Minimum and maximum
* Mean and median
* Range
* Historical totals or averages
* Rates or percentages
* Current-condition values

**Municipal Engineering**

* Historical average flow
* Maximum observed flow
* Minimum observed flow
* Design flow or design capacity
* Average annual demand
* Peak-to-average ratios
* Existing system capacity
* Historical exceedance counts
* Current level-of-service metrics
* Deterministic design calculations

**Finance**

* Historical revenue and expenses
* Revenue growth
* Gross or operating margins
* Historical cash flow
* Average historical return
* Current valuation
* Existing budget or forecast
* Simple DCF or deterministic projection
* Current financial ratios

#### Use Simple Methods

Baseline analysis should favor methods that are:

* Easy to calculate
* Easy to explain
* Based directly on observed data
* Commonly understood within the problem domain
* Reproducible without advanced modeling assumptions

Avoid introducing unnecessary complexity at this stage. The goal is not to build the best possible model. The goal is to establish a credible reference point.

For example, before using Monte Carlo simulation to estimate uncertain future peak flows, first establish what the historical record says using ordinary descriptive and engineering calculations.

#### Distinguish Baseline Analysis from EDA

Baseline analysis and EDA may use some of the same data, but they serve different purposes.

**Baseline analysis asks:**

> What are the basic historical or current conditions that later results should be compared against?

**EDA asks:**

> What patterns, distributions, relationships, trends, and unusual behavior exist within the data?

For example, calculating the historical mean peak flow is appropriate for the baseline. Investigating the shape of the peak-flow distribution with histograms, comparing potential probability distributions, or examining relationships over time belongs in EDA.

#### Distinguish Baseline Analysis from Modeling

The baseline should generally avoid:

* Monte Carlo simulation
* Predictive modeling
* Regression models
* Machine-learning models
* Complex probability models
* Scenario simulation
* Optimization

Those methods belong in later modeling notebooks.

The baseline should provide something against which those advanced methods can be evaluated.

#### Domain Knowledge Matters

Baseline analysis is not simply a list of statistical calculations. Use engineering, financial, or business knowledge to determine which reference values actually matter.

For an engineering problem, ask:

* What values would normally appear in a design calculation or engineering report?
* What historical conditions matter to the design decision?
* What existing standards, capacities, or thresholds provide useful reference points?

For a financial problem, ask:

* What metrics would management normally review?
* What historical performance provides a useful benchmark?
* What current budget, forecast, or operating target should later scenarios be compared against?

#### Keep Interpretation Limited

Briefly explain what the baseline values mean, but avoid performing the detailed investigation intended for EDA.

For example:

> Historical annual peak flows average approximately X cfs, with observed values ranging from Y to Z cfs.

That establishes context.

Investigating why certain years are unusually high, whether the distribution is skewed, whether flows exhibit a trend, or which probability distribution best represents the data belongs in EDA.

#### Expected Output

At the end of the baseline notebook, you should have:

* A small set of clearly defined benchmark metrics.
* A concise description of historical or current conditions.
* Any relevant deterministic engineering or financial calculations.
* A reference point that later modeling results can be compared against.
* A clear understanding of what the advanced model must improve upon or add to the analysis.

#### Completion Question

Before moving to EDA, you should be able to answer:

> **If I had to explain the current or historical condition using only simple, established calculations, what would I report?**

If you can answer that clearly, the baseline analysis has done its job.


The baseline provides a reference against which later modeling results can be compared.

---

### 02 - Exploratory Data Analysis (EDA)

**Purpose:** Understand the behavior, distributions, patterns, and relationships within the cleaned data.

| Analysis                   | Purpose                                              |
| -------------------------- | ---------------------------------------------------- |
| `df.describe()`            | Understand distributions and summary statistics      |
| Histograms                 | Examine distributions, skewness, and unusual values  |
| Boxplots                   | Examine spread and potential outliers                |
| Correlations               | Explore relationships between numerical variables    |
| Scatter plots              | Investigate relationships between variables          |
| Trends / time-series plots | Understand changes over time                         |
| Grouped summaries          | Compare categories, periods, assets, locations, etc. |

EDA should primarily use the **cleaned dataset produced during ingestion**.

EDA can reveal additional problems that were not obvious during ingestion. If a new data-quality issue is discovered, document and correct it before relying on the affected data for analysis.

---

### 03 - Feature Engineering

**Purpose:** Create or transform variables needed for modeling.

Typical activities include:

* Returns
* Growth rates
* Ratios
* Rolling averages
* Lagged variables
* Engineering capacity ratios
* Exceedance indicators
* Risk variables
* Encoded categorical variables
* Time-based features

Feature engineering transforms the cleaned observations into variables that are useful for the analysis or model.

---

### 04 - Modeling

**Purpose:** Apply the analytical, statistical, or simulation model.

Typical activities include:

* Monte Carlo simulation
* Regression
* Forecasting
* Probability models
* Financial valuation models
* Engineering reliability models

The modeling notebook should consume prepared data rather than repeatedly performing raw-data cleaning.

---

### 05 - Evaluation

**Purpose:** Determine how well the model performed and interpret its results.

Typical activities include:

* Error metrics
* Validation results
* Sensitivity analysis
* Monte Carlo percentiles
* Probability of exceedance
* Scenario comparisons
* Comparison against baseline results
* Model limitations

Evaluation answers the question: **How useful and reliable are the modeling results?**

---

### 06 - Conclusion

**Purpose:** Convert the analysis into useful conclusions and decision-support information.

Typical outputs include:

* Key findings
* Engineering or financial interpretation
* Important uncertainties
* Limitations
* Recommendations
* Dashboard-ready metrics
* Executive-summary figures and tables

The conclusion notebook should focus on **what the analysis means**, rather than introducing new analysis.

---

# Standard Workflow

```text
Raw Data
   │
   ▼
00_data_ingestion.ipynb
   │
   ├── Load
   ├── Inspect
   ├── Identify data-quality problems
   ├── Clean
   ├── Validate
   └── Save cleaned data
   │
   ▼
01_baseline_analysis.ipynb
   │
   ▼
02_eda.ipynb
   │
   ▼
03_feature_engineering.ipynb
   │
   ▼
04_modeling.ipynb
   │
   ▼
05_evaluation.ipynb
   │
   ▼
06_conclusion.ipynb
```

## Quick Reference

| Task                                         | Notebook            |
| -------------------------------------------- | ------------------- |
| Load files                                   | Ingestion           |
| `head()`, `shape`, `columns`, `info()`       | Ingestion           |
| Check missing values                         | Ingestion           |
| Check duplicates                             | Ingestion           |
| Remove confirmed duplicates                  | Ingestion           |
| Correct data types                           | Ingestion           |
| Handle missing values                        | Ingestion           |
| Basic reasonableness check with `describe()` | Ingestion           |
| Save cleaned dataset                         | Ingestion           |
| Establish simple benchmark                   | Baseline Analysis   |
| Detailed descriptive statistics              | EDA                 |
| Histograms and boxplots                      | EDA                 |
| Correlations and scatter plots               | EDA                 |
| Time-series/trend exploration                | EDA                 |
| Create modeling variables                    | Feature Engineering |
| Run Monte Carlo simulation/model             | Modeling            |
| Evaluate model/simulation results            | Evaluation          |
| Interpret results and communicate findings   | Conclusion          |

## Core Rule

**Ingestion:** Get the data ready.

**Baseline Analysis:** Establish a simple reference point.

**EDA:** Understand the cleaned data.

**Feature Engineering:** Create the variables needed for modeling.

**Modeling:** Apply the analytical method.

**Evaluation:** Determine how the model performed.

**Conclusion:** Explain what the results mean.
