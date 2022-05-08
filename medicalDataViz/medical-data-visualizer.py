import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

BMI = df['weight'] / ((df['height'] / 100) ** 2)

overweightConditions = [(BMI >= 25), (BMI < 25)]
overweightValues = [1, 0]

df['overweight'] = np.select(overweightConditions, overweightValues)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
conditionsCholesterol = [
    (df['cholesterol'] > 1),
    (df['cholesterol'] <= 1)]
conditionsGluc = [(df['gluc'] > 1),
                  (df['gluc'] <= 1)]
valueChoices = [1, 0]
df['cholesterol'] = np.select(conditionsCholesterol, valueChoices)
df['gluc'] = np.select(conditionsGluc, valueChoices)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columnsOrdered = sorted(['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=columnsOrdered)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.value_counts().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    grid = sns.catplot(x="variable", y="total", col="cardio", hue='value',
                      data=df_cat, kind="bar", order=columnsOrdered, palette=sns.color_palette(['pink', 'green']))
    grid.set_ylabels('total')
    grid.set_xlabels('variable')
    fig = grid.fig
    # Do not modify the next two lines
    plt.show()
    return fig


# Draw Heat Map
def draw_heat_map():
    validValues = df.loc[
    (df["ap_lo"] <= df["ap_hi"])
    & (df["height"] >= df["height"].quantile(0.025))
    & (df["height"] <= df["height"].quantile(0.975))
    & (df["weight"] >= df["weight"].quantile(0.025))
    & (df["weight"] <= df["weight"].quantile(0.975))
]

# Calculate the correlation matrix
    corr = validValues.corr()

# Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
# with sns.axes_style("white"):
    fig, ax = plt.subplots(figsize=(12, 9))

# Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(
    corr,
    mask=mask,
    vmax=0.4,
    square=True,
    fmt=".1f",
    annot=True)

    # Do not modify the next two lines
    plt.show()
    return fig

draw_heat_map()