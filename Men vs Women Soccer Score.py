# Import necessary libraries
import pandas as pd
from scipy.stats import mannwhitneyu as mwu  # For non-parametric comparison of two independent samples
import pingouin as pg  # A statistics library with easier syntax and extra functionality
import matplotlib.pyplot as plt
import seaborn as sns


# Display all columns when printing DataFrames
#Use this if working in pycharm
pd.set_option('display.max_columns', None)

# Load datasets for men's and women's international football match results
mens = pd.read_csv('men_results.csv')
womens = pd.read_csv('women_results.csv')

# Filter data: only FIFA World Cup matches played after January 1, 2002
# Using .copy() to avoid SettingWithCopyWarning later when modifying these subsets
mens_subset = mens.loc[
    (mens['tournament'] == 'FIFA World Cup') & (mens['date'] > '2002-01-01')
].copy()

womens_subset = womens.loc[
    (womens['tournament'] == 'FIFA World Cup') & (womens['date'] > '2002-01-01')
].copy()

# Add a 'group' column to label each DataFrame
mens_subset['group'] = 'men'
womens_subset['group'] = 'women'

# Calculate total goals scored in each match by summing home and away team goals
mens_subset['total_goals'] = mens_subset['home_score'] + mens_subset['away_score']
womens_subset['total_goals'] = womens_subset['home_score'] + womens_subset['away_score']

# Combine the two subsets into a single DataFrame for comparison
both = pd.concat([mens_subset, womens_subset], axis=0, ignore_index=True)

# Set the style
sns.set(style="whitegrid")

# Create boxplot + stripplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=both, x='group', y='total_goals', hue='group', palette='Set2')

# Customize the plot
plt.title('Total Goals per Match: FIFA World Cup (Post-2002)', fontsize=14)
plt.xlabel('Group')
plt.ylabel('Total Goals')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Select only the relevant columns for analysis
both_subset = both[['total_goals', 'group']]

# Pivot the data to get two separate columns: one for men's goals, one for women's
both_subset_wide = both_subset.pivot(columns='group', values='total_goals')

# Perform the Mann-Whitney U Test using Pingouin (easier output formatting)
# Alternative = 'greater' tests if women's total goals > men's total goals
results_pg = pg.mwu(
    x=both_subset_wide['women'],
    y=both_subset_wide['men'],
    alternative='greater'
)

# Perform the same Mann-Whitney U Test using SciPy (for validation or comparison)
results_scipy = mwu(
    x=womens_subset['total_goals'],
    y=mens_subset['total_goals'],
    alternative='greater'
)

# Extract the p-value from the Pingouin results
p_val = results_pg['p-val'].values[0]

# Interpret the result based on a significance threshold (alpha = 0.01)
# If p-value is less than or equal to 0.01, reject the null hypothesis
if p_val <= 0.01:
    result = 'Null Hypothesis Rejected'  # Suggests women's matches have significantly more goals
else:
    result = 'Fail to Reject'  # No significant difference in goal scoring

# Store the result in a dictionary for display or further use
result_dict = {'p-val': p_val, 'Result': result}

# Print the result
print(result_dict)
