---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

### Arbeidskrav Univariant Koding

```{code-cell} ipython3
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('ESS11-subset.csv')

# Display the first few rows of the DataFrame
print(df.head())
```

```{code-cell} ipython3
# Display the list of variables and their data types
print(df.dtypes)

# Convert specific variables to numerical data
variables_to_convert = ['health', 'hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']
df[variables_to_convert] = df[variables_to_convert].apply(pd.to_numeric, errors='coerce')

# Save the edited DataFrame to a new CSV file
df.to_csv('filnavn_edited.csv', index=False)

# Convert 'agea' and 'wkhtot' from object to numeric
df['agea'] = pd.to_numeric(df['agea'], errors='coerce')
df['wkhtot'] = pd.to_numeric(df['wkhtot'], errors='coerce')

# Display the data types to confirm the conversion
print(df[['agea', 'wkhtot']].dtypes)

# Save the edited DataFrame to a new CSV file
df.to_csv('filnavn_edited.csv', index=False)

# Display a success message
print("The variables 'agea' and 'wkhtot' have been converted to numeric and saved to 'filnavn_edited.csv'.")

# Display a success message
print("The variables have been converted to numerical data and saved to 'filnavn_edited.csv'.")
```

```{code-cell} ipython3
# Create ordinal variables
ordinal_mappings = {
    'health': {1: 'Very good', 2: 'Good', 3: 'Fair', 4: 'Bad', 5: 'Very bad'},
    'hlthhmp': {1: 'Yes, to a large extent', 2: 'Yes, to some extent', 3: 'No'},
    'hincfel': {1: 'Living comfortably', 2: 'Coping', 3: 'Difficult', 4: 'Very difficult'},
    'sclmeet': {1: 'Never', 2: '< Once a month', 3: 'Once a month', 4: 'Several times a month', 5: 'Once a week', 6: '> Once a week'}
}

for var, mapping in ordinal_mappings.items():
    df[var + '_ordinal'] = df[var].map(mapping)

# Save the edited DataFrame to a new CSV file
df.to_csv('filnavn_edited.csv', index=False)

# Display a success message
print("The ordinal variables have been created and saved to 'filnavn_edited.csv'.")
```

```{code-cell} ipython3
# Check the range, min, and max of the data for the specified variables
variables_to_check = ['health', 'hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']
range_min_max = df[variables_to_check].agg(['min', 'max'])

print("Range, min, and max of the data for the specified variables:\n")
print(range_min_max)

# Remove all rows that contain a variable with the value 66, 77, 88, 99 (except for agea and wkhtot)
values_to_remove = [66, 77, 88, 99]
df = df[~df[variables_to_check[:-2]].isin(values_to_remove).any(axis=1)]

# Code values 666, 777, 888, and 999 as missing for agea and wkhtot
values_to_code_as_missing = [666, 777, 888, 999]
df['agea'] = df['agea'].replace(values_to_code_as_missing, pd.NA)
df['wkhtot'] = df['wkhtot'].replace(values_to_code_as_missing, pd.NA)


# Save the edited DataFrame to a new CSV file
df.to_csv('filnavn_edited.csv', index=False)

# Remove the values 7, 8, and 9 from the variables health, hlthhmp, and hincfel, and code them as missing
variables_to_modify = ['health', 'hlthhmp', 'hincfel']
values_to_code_as_gone = [7, 8, 9]
df[variables_to_modify] = df[variables_to_modify].replace(values_to_code_as_gone, pd.NA)

# Save the edited DataFrame to a new CSV file
df.to_csv('filnavn_edited.csv', index=False)

# Display a success message
print("\nThe values 7, 8, and 9 have been removed from the variables health, hlthhmp, and hincfel, and coded as missing. The edited data has been saved to 'filnavn_edited.csv'.")

# Display a success message
print("\nRows with specified values have been removed and coded as missing where applicable. The edited data has been saved to 'filnavn_edited.csv'.")

#Kjør cellen to ganger da det ikke fjerner "missing values" på første forsøk.
```

```{code-cell} ipython3
# Display descriptive statistics for the specified variables
# Convert the specified variables from object to numeric (int or float)
variables_to_convert = ['hlthhmp', 'hincfel', 'wkhtot', 'agea']
df[variables_to_convert] = df[variables_to_convert].apply(pd.to_numeric, errors='coerce')

variables_to_describe = ['health', 'hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']
descriptive_stats = df[variables_to_describe].describe()

print(round(descriptive_stats,2))
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np

# Calculate mean, median, and mode
mean_agea = df['agea'].mean()
median_agea = df['agea'].median()
mode_agea = df['agea'].mode()[0]

# Plot a histogram of the 'agea' variable
plt.hist(df['agea'].dropna(), bins=30, edgecolor='black', alpha=0.7)

# Add lines for mean, median, and mode
plt.axvline(mean_agea, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_agea:.2f}')
plt.axvline(median_agea, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_agea:.2f}')
plt.axvline(mode_agea, color='blue', linestyle='dashed', linewidth=1, label=f'Mode: {mode_agea:.2f}')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age with Mean, Median, and Mode')
plt.legend()

# Show the plot
plt.show()
```

```{code-cell} ipython3
# Define variables to boxplot
variables_to_boxplot = ['health', 'hlthhmp', 'hincfel', 'sclmeet']

# Create a boxplot of the specified variables in one figure
plt.figure(figsize=(8, 4))
df[variables_to_boxplot].boxplot()
plt.title('Boxplot of Selected Variables')
plt.xticks(rotation=45)
plt.show()

# Define variables to boxplot
variables_to_bplot = ['agea', 'wkhtot']

# Create a boxplot of the specified variables in one figure
plt.figure(figsize=(8, 4))
df[variables_to_bplot].boxplot()
plt.title('Boxplot of Selected Variables')
plt.xticks(rotation=45)
plt.show()
```

### Arbeidskrav Bivariat koding

```{code-cell} ipython3
from scipy.stats import pearsonr

# Drop rows with missing values in 'agea' and 'wkhtot'
df = df.dropna(subset=['agea', 'wkhtot'])

# Perform correlation analysis between 'agea' and 'wkhtot'
correlation, p_value = pearsonr(df['agea'], df['wkhtot'])

print(f"Correlation coefficient between 'agea' and 'wkhtot': {correlation}")
print(f"P-value: {p_value}")

# Test for statistical significance
alpha = 0.01
if p_value < alpha:
    print("The correlation is statistically significant.")
else:
    print("The correlation is not statistically significant.")
```

```{code-cell} ipython3
# Select the specified variables
variables = ['health', 'hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']

# Create a correlation table
correlation_table = df[variables].corr()

# Display the correlation table
print(round(correlation_table, 4))
```

### Arbeidskrav Multivariat koding

```{code-cell} ipython3
import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
import matplotlib.pyplot as plt
import seaborn as sns

# Convert relevant variables from object to numeric
variables_to_convert = ['health', 'hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']
df[variables_to_convert] = df[variables_to_convert].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values in the specified variables
df = df.dropna(subset=variables_to_convert)

# Define the dependent and independent variables
X = df[['hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea']]
y = df['health']

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the OLS regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression model
print(model.summary())

# Test for linearity using scatter plots
sns.pairplot(df, x_vars=['hlthhmp', 'hincfel', 'sclmeet', 'wkhtot', 'agea'], y_vars='health', kind='reg')
plt.show()

# Test for homoscedasticity using Breusch-Pagan test
test_results = sms.het_breuschpagan(model.resid, model.model.exog)
names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
print(lzip(names, test_results))

# Test for normality of residuals using Jarque-Bera test
jb_test = sms.jarque_bera(model.resid)
print(f"Jarque-Bera test statistic: {jb_test[0]}, p-value: {jb_test[1]}")

# Plot histogram of residuals to visually inspect normality
plt.hist(model.resid, bins=30, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.show()

# Test for multicollinearity using Variance Inflation Factor (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)
```

```{code-cell} ipython3
import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
import matplotlib.pyplot as plt

# Load the dataset (update the filename accordingly)
file_path = "filnavn_edited.csv"
df = pd.read_csv(file_path)

# Define dependent and independent variables
dependent_var = "health"
independent_vars = ["hlthhmp", "hincfel", "sclmeet", "wkhtot", "agea"]

# Drop rows with missing values in the relevant columns
df = df.dropna(subset=[dependent_var] + independent_vars)

# Define X (independent variables) and y (dependent variable)
X = df[independent_vars]
y = df[dependent_var]

# Add constant to independent variables for OLS regression
X = sm.add_constant(X)

# Fit the OLS model
model = sm.OLS(y, X).fit()

# Perform Breusch-Pagan test
bp_test = smd.het_breuschpagan(model.resid, X)
labels = ["LM Statistic", "p-value", "F-Statistic", "F p-value"]

# Print results
print(dict(zip(labels, bp_test)))

# Scatter plot of residuals vs fitted values
plt.figure(figsize=(8, 6))
plt.scatter(model.fittedvalues, model.resid, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Heteroskedasticity Check: Residuals vs Fitted Values")
plt.show()
```
