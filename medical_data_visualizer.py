import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# Calculate the BMI for each person
df['BMI'] = df['weight'] / ((df['height'] / 100)**2)

# Add the overweight column
df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


def normalize(value):
  if value == 1:
    return 0
  elif value > 1:
    return 1
  else:
    return value


# Normalize 'cholesterol' and 'glu' columns
df["cholesterol"] = df['cholesterol'].apply(normalize)
df["gluc"] = df["gluc"].apply(normalize)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol', 'gluc', 'overweight','smoke'])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  #df_cat = None

  # Draw the catplot with 'sns.catplot()'

  # Get the figure for the output
  fig = sns.catplot(x='variable', hue='value',     col='cardio', data=df_long, kind='count')

  plt.show()
  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) &        (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(14, 8))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr_matrix, annot=True, cmap='cool', mask=mask)
  plt.title('Correlation Matrix')
  plt.show()
  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
