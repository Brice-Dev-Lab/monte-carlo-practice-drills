# Analysis of Financial Time Series — Companion Data

## Overview

This directory contains selected companion datasets from Ruey S. Tsay's *Analysis of Financial Time Series*, Third Edition. The datasets support the examples and exercises presented throughout the book and cover a broad range of financial and economic time-series applications.

The files are provided by Ruey S. Tsay through the University of Chicago Booth School of Business. They are retained in their original formats and filenames so they can be matched directly to the corresponding chapters, examples, and exercises in the book.

> **Source:** [Analysis of Financial Time Series, Third Edition — official companion page](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)

## Book Reference

Tsay, R. S. (2010). *Analysis of financial time series* (3rd ed.). Wiley.

- ISBN: `978-0-470-41435-4`
- Publisher: Wiley
- Edition: Third Edition
- Publication year: 2010

## Purpose of This Data Collection

The datasets are intended for educational work involving:

- data ingestion and cleaning;
- exploratory data analysis;
- return calculations and distribution analysis;
- autocorrelation and stationarity analysis;
- AR, MA, and ARIMA models;
- volatility and GARCH-family models;
- nonlinear time-series models;
- high-frequency market data;
- extreme-value analysis and Value at Risk;
- multivariate time-series analysis;
- principal component and factor models;
- state-space models and Kalman filtering; and
- Markov chain Monte Carlo methods.

Although the book primarily demonstrates the analysis in R, the datasets can also be used with Python libraries such as pandas, NumPy, SciPy, statsmodels, and arch.

## Dataset Categories

The official companion collection includes several types of data:

| Category | Examples |
|---|---|
| Equity data | IBM, Intel, 3M, Microsoft, Citigroup, GE, Cisco, Apple, and other stocks |
| Market indexes | S&P 500, value-weighted indexes, and equal-weighted indexes |
| Fixed income | Treasury rates, Treasury bill rates, bond yields, and bond-index returns |
| Foreign exchange | U.S. dollar exchange rates against the yen, pound, euro, and Canadian dollar |
| Macroeconomic data | GDP, GNP, unemployment, inflation, industrial production, and electricity demand |
| High-frequency data | Trade prices, bid and ask quotes, volume, and durations between trades |
| Risk and volatility | Excess returns, realized volatility, extreme returns, and Value-at-Risk examples |
| Multivariate data | Multiple securities, rates, indexes, factors, and pairs-trading series |

## Chapter Coverage

| Chapter | Primary subject |
|---:|---|
| 1 | Financial time series and their characteristics |
| 2 | Linear time-series analysis and applications |
| 3 | Conditional heteroscedastic models |
| 4 | Nonlinear models and applications |
| 5 | High-frequency data and market microstructure |
| 6 | Continuous-time models and applications |
| 7 | Extreme values, quantile estimation, and Value at Risk |
| 8 | Multivariate time-series analysis |
| 9 | Principal component analysis and factor models |
| 10 | Multivariate volatility models |
| 11 | State-space models and the Kalman filter |
| 12 | Markov chain Monte Carlo methods |

## File-Naming Conventions

Many filenames begin with a frequency indicator:

| Prefix | Typical meaning |
|---|---|
| `d-` | Daily data |
| `w-` | Weekly data |
| `m-` | Monthly data |
| `q-` | Quarterly data |

The remaining portion of a filename typically identifies the company, index, economic variable, or approximate date range. For example:

- `d-intc7208.txt` — daily Intel returns, approximately 1972–2008;
- `m-ibm3dx2608.txt` — monthly IBM and three-index returns, approximately 1926–2008;
- `q-gdp4708.txt` — quarterly U.S. GDP, approximately 1947–2008; and
- `w-gs1yr.txt` — weekly one-year Treasury rates.

These conventions are helpful but are not a substitute for the description on the official companion page. Always confirm the frequency, units, date range, and column definitions before analysis.

## Recommended Directory Structure

Preserve downloaded source files as immutable raw data:

```text
data/
├── raw/
│   └── tsay_afts_3e/
│       ├── chapter_01/
│       ├── chapter_02/
│       ├── chapter_03/
│       └── ...
├── interim/
│   └── tsay_afts_3e/
└── processed/
    └── tsay_afts_3e/
```

- `raw/` contains the original downloaded files without modification.
- `interim/` contains partially cleaned or reformatted working data.
- `processed/` contains analysis-ready datasets with documented schemas.

Do not overwrite the raw files during cleaning. If a file is used in multiple chapters, either maintain one canonical raw copy or document why chapter-specific copies are necessary.

## Recommended Notebook Workflow

```text
00_data_ingestion.ipynb
01_exploratory_data_analysis.ipynb
02_baseline_analysis.ipynb
03_model_development.ipynb
04_model_diagnostics.ipynb
05_results_and_interpretation.ipynb
```

### Data Ingestion

The ingestion notebook should establish that the file can be reliably converted into a documented tabular dataset. Typical tasks include:

- locating and loading the source file;
- inspecting `head`, `shape`, columns, and data types;
- identifying the delimiter and presence of a header;
- parsing nonstandard dates;
- converting numeric fields stored as text;
- identifying missing values and duplicate records;
- confirming units and return conventions;
- recording rejected or questionable rows; and
- saving an analysis-ready version without altering the raw file.

### Exploratory Data Analysis

EDA should begin with the cleaned dataset and focus on understanding its behavior. Typical tasks include:

- summary statistics;
- time-series plots;
- histograms, boxplots, and empirical distributions;
- outlier and extreme-return investigation;
- autocorrelation analysis;
- rolling means and volatility;
- stationarity considerations;
- structural breaks; and
- relationships among multiple series.

In short: **ingestion makes the data usable; EDA makes the data understandable.**

## Important Data Considerations

These files were created for textbook analysis rather than as modern, standardized datasets. Before modeling, verify:

1. **File format** — Files may use whitespace, commas, or other delimiters and may have `.txt` or `.dat` extensions.
2. **Headers** — Some files contain headers; others require column names to be assigned from the book or companion-page description.
3. **Date encoding** — Dates may be stored as integers or compact year/month/day fields.
4. **Return definition** — Determine whether values are simple returns, log returns, excess returns, prices, rates, or percentages.
5. **Scale** — A value may be expressed as a decimal return or a percentage return. Confusing the two creates a 100-fold error.
6. **Frequency** — Confirm whether observations are daily, weekly, monthly, or quarterly.
7. **Missing values** — Missing or sentinel values may not follow modern conventions such as `NaN`.
8. **Market history** — Company names, ticker symbols, index construction, and market structure may differ from current practice.
9. **Date range** — Most datasets end around 2008 or 2009 and should not be treated as current market data.
10. **Model reproducibility** — Results may differ from the book because of software versions, package defaults, numerical methods, or cleaning decisions.

## Python Loading Examples

Many whitespace-delimited files can be inspected with:

```python
from pathlib import Path

import pandas as pd

file_path = Path("data/raw/tsay_afts_3e/chapter_01/d-intc7208.txt")

df = pd.read_csv(file_path, sep=r"\s+")

print(df.shape)
print(df.dtypes)
print(df.head())
```

If the file has no header:

```python
df = pd.read_csv(
    file_path,
    sep=r"\s+",
    header=None,
    names=["date", "return"],
)
```

Do not assume that these examples fit every file. Inspect the source and the official description before assigning column names or parsing dates.

## Data Provenance

For each downloaded file, record at least:

| Field | Description |
|---|---|
| Original filename | Filename used by the author |
| Source URL | Direct file URL or official companion-page URL |
| Download date | Date the local copy was retrieved |
| Book chapter | Chapter in which the file is used |
| Book example/exercise | Relevant example or exercise number, when known |
| Frequency | Daily, weekly, monthly, or quarterly |
| Variables | Documented column names and meanings |
| Units | Prices, decimal returns, percentage returns, rates, or other units |
| Local transformations | Cleaning, parsing, filtering, or scaling applied |

A checksum may also be stored to confirm that the raw file has not changed.

## Use in This Repository

The data may be used to reproduce selected textbook analyses and to develop Python-based exercises in financial time-series analysis. Code developed here may differ from the book's R examples, but the financial meaning of the variables and the statistical assumptions should remain explicit.

When extending an example:

- first reproduce or approximate the textbook result;
- document any changes to the sample period or calculation method;
- separate observed facts from modeling assumptions;
- compare results with a simple baseline;
- evaluate model diagnostics before forecasting; and
- state limitations before drawing investment or risk-management conclusions.

## Licensing and Attribution

The datasets were not created by this repository. They remain associated with the author, publisher, and any underlying data providers. Their availability on the official companion page does not automatically establish unrestricted redistribution rights.

For a public repository, the safer approach is to:

- provide download instructions and source links;
- retain provenance metadata;
- avoid claiming ownership of the data;
- verify applicable permissions before redistributing the complete collection; and
- cite the book and official companion page in analyses that use the files.

## Official Resources

- [Book companion page and complete dataset catalog](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)
- [Ruey S. Tsay — faculty page](https://faculty.chicagobooth.edu/ruey-s-tsay)
- [Wiley book page](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470644560)
- [Book errata](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/introts/errata.pdf)

