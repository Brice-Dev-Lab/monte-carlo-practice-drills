# Dataset Catalog: *Analysis of Financial Time Series*, Third Edition

## About This Catalog

This document describes the companion datasets used in Ruey S. Tsay's *Analysis of Financial Time Series*, Third Edition. It identifies what each file contains, its observation frequency, its approximate date range when stated by the author, and whether it is used in the chapter text or assigned exercises.

The filenames and descriptions below are based on the author's official companion page:

[Ruey S. Tsay — *Analysis of Financial Time Series*, Third Edition](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)

## Naming Conventions

The first character of many filenames indicates the observation frequency:

| Prefix | Frequency |
|---|---|
| `d-` | Daily |
| `w-` | Weekly |
| `m-` | Monthly |
| `q-` | Quarterly |

Abbreviations commonly appearing in the filenames include:

| Abbreviation | Meaning |
|---|---|
| `VW` | Value-weighted market index |
| `EW` | Equal-weighted market index |
| `SP` or `SP5` | S&P 500 index |
| `GS` | Treasury constant-maturity rate |
| `TB` | Treasury bill |
| `ln` or `log` | Natural logarithm or log return |
| `rtn` | Return |

Date ranges embedded in filenames are abbreviated. For example, `7208` generally means 1972–2008 and `2608` generally means 1926–2008. Confirm the actual dates and column definitions after loading each file.

---

## Chapter 1 — Financial Time Series and Their Characteristics

### Datasets Used in the Text

| File | Frequency | Description | Date range / format |
|---|---|---|---|
| [`d-ibm3dx7008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibm3dx7008.txt) | Daily | Simple returns for IBM, a value-weighted index, an equal-weighted index, and the S&P 500 | 1970-01-02 to 2008-12-31; date plus four return columns |
| [`d-intc7208.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-intc7208.txt) | Daily | Simple returns for Intel stock | 1972-12-15 to 2008-12-31 |
| [`d-3m7008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-3m7008.txt) | Daily | Simple returns for 3M stock | 1970-01-02 to 2008-12-31 |
| [`d-msft8608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-msft8608.txt) | Daily | Simple returns for Microsoft stock | 1986-03-04 to 2008-12-13 |
| [`d-c8608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-c8608.txt) | Daily | Simple returns for Citigroup stock | 1986-03-14 to 2008-12-31 |
| [`m-ibm3dx2608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibm3dx2608.txt) | Monthly | Simple returns for IBM, the value-weighted index, equal-weighted index, and S&P 500 | 1926-01 to 2008-12; date plus four return columns |
| [`m-intc7308.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-intc7308.txt) | Monthly | Simple returns for Intel stock | Approximately 1973–2008 |
| [`m-3m4608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-3m4608.txt) | Monthly | Simple returns for 3M stock | 1946-02 to 2008-12 |
| [`m-msft8608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-msft8608.txt) | Monthly | Simple returns for Microsoft stock | Approximately 1986–2008 |
| [`m-c8608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-c8608.txt) | Monthly | Simple returns for Citigroup stock | Approximately 1986–2008 |
| [`m-gs10.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs10.txt) | Monthly | Ten-year Treasury constant-maturity rate | 1953-04 to 2009-02; year, month, date, and rate |
| [`m-gs1.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs1.txt) | Monthly | One-year Treasury constant-maturity rate | 1953-04 to 2009-02; year, month, date, and rate |
| [`d-jpus.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-jpus.txt) | Daily | U.S. dollar/Japanese yen exchange rate | 2000-01-04 to 2009-03-27 |
| [`m-fama-bonds.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-fama-bonds.txt) | Monthly | Returns for bond maturity groups of 1–12, 24–36, 48–60, and 61–120 months | Date plus bond-return columns |
| [`m-gs3.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs3.txt) | Monthly | Three-year Treasury constant-maturity rate | Not specified |
| [`m-gs5.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs5.txt) | Monthly | Five-year Treasury constant-maturity rate | Not specified |
| [`w-tb3ms.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-tb3ms.txt) | Weekly | Three-month Treasury bill rate | Not specified |
| [`w-tb6ms.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-tb6ms.txt) | Weekly | Six-month Treasury bill rate | Not specified |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`d-3stocks9908.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-3stocks9908.txt) | Daily | Simple returns for American Express, Caterpillar, and Starbucks | 1 and 4 |
| [`m-gm3dx7508.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gm3dx7508.txt) | Monthly | Simple returns for GM, the value-weighted index, equal-weighted index, and S&P 500 | 2 and 3 |
| [`d-caus.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-caus.txt) | Daily | Canadian dollar/U.S. dollar exchange rate | 5 |
| [`d-usuk.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-usuk.txt) | Daily | U.S. dollar/U.K. pound exchange rate | 5 |
| [`d-jpus.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-jpus.txt) | Daily | U.S. dollar/Japanese yen exchange rate | 5 |
| [`d-useu.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-useu.txt) | Daily | U.S. dollar/euro exchange rate | 5 |

---

## Chapter 2 — Linear Time-Series Analysis and Applications

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| `m-ibm3dx2608.txt` | Monthly | IBM, value-weighted, equal-weighted, and S&P 500 simple returns |
| [`dgnp82.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/dgnp82.txt) | Quarterly | Growth rate of real U.S. GNP; equivalent to `q-gnp4791.txt` |
| `m-3m4608.txt` | Monthly | Simple returns for 3M stock |
| [`q-gdp4708.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/q-gdp4708.txt) | Quarterly | U.S. GDP from 1947 through 2008 |
| [`d-sp55008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-sp55008.txt) | Daily | Values of the S&P 500 index, approximately 1950–2008 |
| [`q-jnj.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/q-jnj.txt) | Quarterly | Johnson & Johnson earnings from 1960 through 1980 |
| [`m-deciles08.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-deciles08.txt) | Monthly | Simple returns for market-capitalization deciles 1, 2, 9, and 10 |
| [`w-gs1yr.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-gs1yr.txt) | Weekly | One-year Treasury rate |
| [`w-gs3yr.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-gs3yr.txt) | Weekly | Three-year Treasury rate |
| `d-ibm3dx7008.txt` | Daily | IBM, value-weighted, equal-weighted, and S&P 500 simple returns |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`m-unrate.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-unrate.txt) | Monthly | U.S. civilian unemployment rate | 3 |
| `m-deciles08.txt` | Monthly | Returns for market-capitalization deciles 1, 2, 9, and 10 | 4 |
| `d-ibm3dx7008.txt` | Daily | IBM and three market-index returns | 5 |
| [`power6.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/power6.txt) | Not stated | Electricity demand expressed in logarithms | 6 |
| [`d-ibm3dxwkdays8008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibm3dxwkdays8008.txt) | Daily | IBM, value-weighted, equal-weighted, and S&P 500 returns with weekday information | 7–9 |
| [`w-Aaa.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-aaa.txt) | Weekly | Moody's seasoned Aaa corporate-bond yield | 10–12 |
| [`w-Baa.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-baa.txt) | Weekly | Moody's seasoned Baa corporate-bond yield | 10–12 |
| [`m-ew6299.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ew6299.txt) | Monthly | Equal-weighted index returns, approximately 1962–1999 | 13 |
| [`sp5may.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/sp5may.dat) | Not stated | Log prices of S&P 500 futures and spot index | 14 |
| [`q-gdpdef.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/q-gdpdef.txt) | Quarterly | U.S. GDP implicit price deflator | 15 |

---

## Chapter 3 — Conditional Heteroscedastic Models

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| `m-intc7308.txt` | Monthly | Intel simple returns |
| [`exch-perc.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/exch-perc.txt) | 10-minute | Deutsche mark/U.S. dollar foreign-exchange log returns |
| [`sp500.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/sp500.dat) | Monthly | Excess returns for the S&P 500 index |
| [`m-ibmvwew2697.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmvwew2697.txt) | Monthly | IBM, value-weighted, and equal-weighted simple returns, approximately 1926–1997 |
| [`m-ibmvwewsp2603.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmvwewsp2603.txt) | Monthly | IBM, value-weighted, equal-weighted, and S&P 500 simple returns, approximately 1926–2003 |
| [`d-ibmvwewsp6203.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibmvwewsp6203.txt) | Daily | IBM, value-weighted, equal-weighted, and S&P 500 simple returns, approximately 1962–2003 |
| [`m-ibmspln.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmspln.dat) | Monthly | Log returns for IBM and the S&P 500 |
| [`m-ibmsplnsu.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmsplnsu.dat) | Monthly | Supporting IBM and S&P 500 log-return data for Example 3.4 |
| [`d-sp8099.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-sp8099.txt) | Daily | S&P 500 returns, approximately 1980–1999 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| `m-intc7308.txt` | Monthly | Intel simple returns | 5 |
| [`m-mrk4608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-mrk4608.txt) | Monthly | Merck simple returns, approximately 1946–2008 | 6 |
| `m-3m4608.txt` | Monthly | 3M simple returns | 7 |
| [`m-gmsp5008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gmsp5008.txt) | Monthly | GM and S&P 500 simple returns, approximately 1950–2008 | 8–10 |
| [`d-gmsp9908.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-gmsp9908.txt) | Daily | GM and S&P 500 simple returns, approximately 1999–2008 | 11–15 |

---

## Chapter 4 — Nonlinear Models and Their Applications

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| `m-unrate.txt` | Monthly | U.S. civilian unemployment rate, approximately 1948–2009 |
| `d-ibmvwewsp6203.txt` | Daily | IBM and three market-index returns |
| `m-3m4608.txt` | Monthly | 3M simple returns |
| [`q-gnp4791.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/q-gnp4791.txt) | Quarterly | Growth rates of U.S. GNP, approximately 1947–1991 |
| [`w-tb3ms7097.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-tb3ms7097.txt) | Weekly | Three-month Treasury bill rate, approximately 1970–1997 |
| [`m-ibmln2699.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmln2699.txt) | Monthly | IBM log returns expressed as percentages, approximately 1926–1999 |
| `m-ibmvwew2697.txt` | Monthly | IBM, equal-weighted, and value-weighted returns |
| [`q-unemrate.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/q-unemrate.txt) | Quarterly | U.S. unemployment rate |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`d-jnj9808.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-jnj9808.txt) | Daily | Johnson & Johnson stock returns, approximately 1998–2008 | 1 |
| [`m-ge2608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ge2608.txt) | Monthly | GE stock returns, approximately 1926–2008 | 2, 3, and 5 |
| `w-gs1yr.txt` | Weekly | One-year Treasury constant-maturity rate | 6 |
| `w-gs3yr.txt` | Weekly | Three-year Treasury constant-maturity rate | 6 |

---

## Chapter 5 — High-Frequency Data Analysis and Market Microstructure

### Datasets Used in the Text

| File | Frequency | Description | Date range / columns |
|---|---|---|---|
| [`ibm.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm.txt) | Transaction-level | IBM trades and quotes | 1990-11-01 to 1991-01-31; date/time, volume, bid, ask, transaction price |
| [`ibm9912-tp.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm9912-tp.dat) | Transaction-level | IBM transaction prices | December 1999; day, time, price |
| [`taq-td-ba12012008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/taq-td-ba12012008.txt) | Transaction-level | Boeing trade data | 2008-12-01 |
| [`ibmdurad.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibmdurad.dat) | Transaction-duration | Adjusted durations between IBM trades | 1990-11-01 to 1991-01-31 |
| [`ibm1to5-dur.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm1to5-dur.txt) | Transaction-duration | Positive adjusted IBM trade durations for the first five trading days | First five days of the IBM sample |
| [`ibm91-ads.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm91-ads.dat) | Transaction-duration | Autoregressive conditional-duration response data for Example 5.2 | Not specified |
| [`ibm91-adsx.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm91-adsx.dat) | Transaction-duration | Explanatory variables corresponding to `ibm91-ads.dat` | Not specified |
| [`day15-ori.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/day15-ori.dat) | Transaction-level | Original IBM transaction data | 1990-11-21 |
| [`day15.dat`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/day15v.dat) | Transaction-level | Processed IBM data for price-change-duration models | 1990-11-21 |
| [`day15.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/day15.txt) | Documentation | Description of the `day15` data | 1990-11-21 |
| [`d-aapl9907.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-aapl9907.txt) | Daily | Adjusted Apple stock prices | 1999-01-04 to 2007-11-20 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`ibm-d2-dur.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/ibm-d2-dur.txt) | Transaction-duration | Adjusted IBM trade durations for 1990-11-02 | 3 |
| [`mmm9912-dtp.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/mmm9912-dtp.txt) | Transaction-level | 3M transaction data from December 1999 | 4 and 5 |
| [`mmm9912-adur.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/mmm9912-adur.txt) | Transaction-duration | Adjusted durations between 3M trades during December 1999 | 6 |
| `taq-td-ba12012008.txt` through `taq-td-ba12052008.txt` | Transaction-level | Boeing trade data for five trading days, 2008-12-01 through 2008-12-05 | 7–10 |

---

## Chapter 6 — Continuous-Time Models and Their Applications

| File | Frequency | Description | Date range |
|---|---|---|---|
| [`d-ibmy98.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibmy98.txt) | Daily | IBM simple returns | 1998 |
| [`d-csco2007.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-csco2007.txt) | Daily | Cisco log returns | The companion page describes these as 1999 data; verify the file despite its name |

The chapter also provides `kou.f`, a Fortran implementation of European call and put valuation under the simple jump-diffusion model. It is source code rather than a dataset.

---

## Chapter 7 — Extreme Values, Quantile Estimation, and Value at Risk

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`d-ibm6298.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibm6298.txt) | Daily | IBM stock returns, approximately 1962–1998; 9,190 observations |
| `d-intc7208.txt` | Daily | Intel log returns used in Example 7.4 |
| [`d-ibmln98wm.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibmln98wm.txt) | Daily | Mean-corrected IBM log returns used in Subsection 7.7.8 |
| [`d-ibml25x.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ibml25x.txt) | Daily | Explanatory variables associated with the IBM analysis in Subsection 7.7.8 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`d-ge9808.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-ge9808.txt) | Daily | GE stock returns, approximately 1998–2008 | 1 and 8 |
| [`d-csco9808.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-csco9808.txt) | Daily | Cisco stock returns, approximately 1998–2008 | 2 and 3 |
| [`d-hpq3dx9808.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-hpq3dx9808.txt) | Daily | HP stock returns and three market-index returns | 4 |
| [`d-aaspx9808.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-aaspx9808.txt) | Daily | Alcoa and S&P 500 returns, approximately 1998–2008 | 5–7 |

---

## Chapter 8 — Multivariate Time-Series Analysis and Applications

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`m-ibmsp2608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmsp2608.txt) | Monthly | IBM and S&P 500 returns, approximately 1926–2008 |
| [`m-bnd.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-bnd.txt) | Monthly | Simple returns for U.S. bond indexes |
| [`m-gs1n3-5301.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs1n3-5301.txt) | Monthly | One-year and three-year U.S. Treasury rates, approximately 1953–2001 |
| [`w-tb3n6ms.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-tb3n6ms.txt) | Weekly | Three-month and six-month Treasury bill rates |
| `sp5may.dat` | Not stated | Log prices of S&P 500 futures and the spot index |
| [`d-bhp0206.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-bhp0206.txt) | Daily | BHP stock series for a pairs-trading example, approximately 2002–2006 |
| [`d-vale0206.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-vale0206.txt) | Daily | Vale stock series paired with BHP, approximately 2002–2006 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`m-mrk2vw.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-mrk2vw.txt) | Monthly | Returns for Merck and additional equities together with the value-weighted index | 1 |
| [`m-gs1n10.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs1n10.txt) | Monthly | One-year and ten-year U.S. Treasury rates | 2–4 |
| [`m-gs1n3-5304.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-gs1n3-5304.txt) | Monthly | One-year and three-year U.S. Treasury rates, approximately 1953–2004 | 7 |

---

## Chapter 9 — Principal Component Analysis and Factor Models

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`m-fac9003.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-fac9003.txt) | Monthly | Stock returns used in Table 9.1, approximately 1990–2003 |
| [`m-cpice16-dp7503.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-cpice16-dp7503.txt) | Monthly | Macroeconomic variables including CPI and CE16, approximately 1975–2003 |
| [`m-barra-9003.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-barra-9003.txt) | Monthly | Excess returns used in Table 9.2, approximately 1990–2003 |
| [`m-5clog-9008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-5clog-9008.txt) | Monthly | Percentage log returns for IBM, HPQ, Intel, JPMorgan, and Bank of America, approximately 1990–2008 |
| `m-bnd.txt` | Monthly | Returns for U.S. bond indexes |
| [`m-apca0103.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-apca0103.txt) | Monthly/long format | Returns for 40 stocks used in Table 9.6; company ID, date, and return |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`m-fac-ex-9008.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-fac-ex-9008.txt) | Monthly | Returns for multiple stocks and the S&P 500, approximately 1990–2008 | 1 |
| `m-mrk2vw.txt` | Monthly | Merck, Johnson & Johnson, GE, other stocks, and the value-weighted index | 2 |
| [`m-excess-c10sp-9003.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-excess-c10sp-9003.txt) | Monthly | Simple excess returns for a group of stocks and the S&P 500, approximately 1990–2003 | 3–6 |
| [`m-fedip.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-fedip.txt) | Monthly | Federal funds rate and industrial-production index | 7 |

---

## Chapter 10 — Multivariate Volatility Models and Applications

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`d-hkjp0608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-hkjp0608.txt) | Daily | Hong Kong and Japanese market indexes for Example 10.1; 714 observations, approximately 2006–2008 |
| [`m-pfemrk6508.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-pfemrk6508.txt) | Monthly | Pfizer and Merck returns, approximately 1965–2008 |
| [`m-ibmsp2699.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmsp2699.txt) | Monthly | IBM and S&P 500 returns, approximately 1926–1999 |
| [`d-spcscointc.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-spcscointc.txt) | Daily | Three-column dataset of log returns for the S&P 500, Cisco, and Intel |
| [`d-fxsk9904.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-fxsk9904.txt) | Daily | Exchange-rate and stock-return series, approximately 1999–2004 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`m-ibmhpqsp6208.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmhpqsp6208.txt) | Monthly | Log returns for IBM, HPQ, and S&P 500, approximately 1962–2008 | 1–4 |
| [`m-geibmsp2608.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-geibmsp2608.txt) | Monthly | Simple returns for GE, IBM, and S&P 500, approximately 1926–2008 | 5 and 6 |
| [`m-spibmge.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-spibmge.txt) | Monthly | Percentage log returns for S&P 500, IBM, and GE | 7–9 |
| [`d-dellcsco9099.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-dellcsco9099.txt) | Daily | Log returns for Dell and Cisco, approximately 1990–1999 | 10 |

---

## Chapter 11 — State-Space Models and the Kalman Filter

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`aa-3rv.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/aa-3rv.txt) | Daily | Alcoa realized-volatility estimates constructed from 5-, 10-, and 20-minute intervals |
| `m-fac9003.txt` | Monthly | GM excess returns from the Chapter 9 Table 9.1 dataset |
| `q-jnj.txt` | Quarterly | Johnson & Johnson earnings reused from Chapter 2 |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`aa-rv-20m.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/aa-rv-20m.txt) | Daily | Alcoa realized volatility based on 20-minute intervals | 2 |
| [`m-pfesp-ex9003.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-pfesp-ex9003.txt) | Monthly | Simple excess returns for Pfizer and the S&P 500, approximately 1990–2003 | 3 |
| [`m-ppiaco4709.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ppiaco4709.txt) | Monthly | U.S. producer price index for all commodities | 5; 1947-01 to 2009-11 |

---

## Chapter 12 — Markov Chain Monte Carlo Methods

### Datasets Used in the Text

| File | Frequency | Description |
|---|---|---|
| [`w-gs1n3c.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-gs1n3c.txt) | Weekly | Change series for one-year and three-year U.S. Treasury rates |
| [`w-gs3c.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/w-gs3c.txt) | Weekly | Change series for the three-year U.S. Treasury rate |
| [`m-sp500-6209.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-sp500-6209.txt) | Monthly | S&P 500 log returns, approximately 1962–2009 |
| [`m-ibmsp6209.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-ibmsp6209.txt) | Monthly | IBM and S&P 500 log returns, approximately 1962–2009 |
| [`m-sp5-6204.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-sp5-6204.txt) | Monthly | Log level of the S&P 500 index, approximately 1962–2004 |
| [`m-geln.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-geln.txt) | Monthly | GE log returns |

### Exercise Datasets

| File | Frequency | Description | Exercises |
|---|---|---|---:|
| [`m-fsp6508.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-fsp6508.txt) | Monthly | Ford and S&P 500 simple returns, approximately 1965–2008 | 4 and 6 |
| [`d-csco0108.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/d-csco0108.txt) | Daily | Cisco returns, approximately 2001–2008 | 5 |
| [`m-pgvw6508.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-pgvw6508.txt) | Monthly | Procter & Gamble and value-weighted-index returns, approximately 1965–2008 | 7 |
| [`m-mort3mtb7109.txt`](https://faculty.chicagobooth.edu/-/media/faculty/ruey-s-tsay/teaching/fts3/m-mort3mtb7109.txt) | Monthly | Thirty-year mortgage rate and three-month Treasury bill rate, approximately 1971–2009 | 8 |

---

## Interpretation and Data-Quality Notes

Before using any file, verify the following from the data itself and the relevant section of the book:

- whether returns are simple or logarithmic;
- whether returns and rates are decimals or percentages;
- whether a file contains prices, returns, yields, index levels, changes, or excess returns;
- the date encoding and chronological order;
- the presence or absence of column headers;
- the delimiter used by the text or `.dat` file;
- missing-value conventions;
- whether multiple series are aligned to the same trading dates; and
- whether the date range inferred from the filename agrees with the observations.

Descriptions in this catalog summarize the official companion page. They do not replace the book's definitions, table notes, or example-specific transformations.

## Citation

Tsay, R. S. (2010). *Analysis of financial time series* (3rd ed.). Wiley.

