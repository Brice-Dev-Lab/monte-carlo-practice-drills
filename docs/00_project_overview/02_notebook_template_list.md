# Notebook Templates and Responsibilities

## Notebook Template List

* 00_data_ingestion.ipynb
* 01_baseline_analysis.ipynb
* 02_eda.ipynb
* 03_feature_engineering.ipynb
* 04_modeling.ipynb
* 05_evaluation.ipynb
* 06_conclusion.ipynb

## Notebook Responsibilities

### Ingestion and EDA Notebook
| Check                     | Notebook  | Purpose                                                               |
| ------------------------- | --------- | --------------------------------------------------------------------- |
| `df.head()`               | Ingestion | Confirm the file loaded correctly and inspect its structure           |
| `df.shape`                | Ingestion | Record the number of rows and columns received                        |
| `df.columns`              | Ingestion | Inspect and standardize column names                                  |
| `df.dtypes` / `df.info()` | Ingestion | Detect incorrect data types                                           |
| `df.isna().sum()`         | Ingestion | Identify missing values that must be handled or flagged               |
| `df.duplicated()`         | Ingestion | Identify duplicate records                                            |
| `df.describe()`           | Both      | Validate values during ingestion; understand distributions during EDA |
| Histograms/boxplots       | EDA       | Understand distributions and investigate outliers                     |
| Correlations              | EDA       | Explore relationships between variables                               |
| Trends/time-series plots  | EDA       | Understand changes over time                                          |
