# Plain EDA
Group 25 - Contributors: Derrick Jaskiel - Hoi Hin Kwok - Rebecca Rosette Nanfuka - Hooman Esteki
Crouse: DSCI 524

## About
Plaineda is a minimalistic set of resources to ease the very first steps of data exploration, It offers prompt column summaries, elementary statistics, missing value verifications, and several basic images that hasty and dull early EDA.

## Suggested 4 functions:
* summarize_columns(df) – summary table of each column (type, missing %, unique count)
* numeric_profile(df, group_by=None) – basic stats for numeric columns
* plot_target_distribution(df, target_col) – quick visualization of a target column
* quick_correlation(df, method="pearson") – correlation matrix for numeric columns
