import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    # Import data
    df = pd.read_csv('medical_examination.csv')

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    # Normalize data by making 0 always good and 1 always bad
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio' and show the counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})

    # Convert the data into long format and create a catplot
    cat_plot = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=5,
        aspect=1
    )

    # Get the figure for the output
    fig = cat_plot.fig

    # Save the plot as an image file
    fig.savefig('catplot.png')

    return fig


def draw_heat_map():
    # Import data
    df = pd.read_csv('medical_examination.csv')

    # Clean the data
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
        ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Plot the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=0.5,
        cmap='coolwarm',
        square=True,
        cbar_kws={"shrink": 0.5}
    )

    # Save the heatmap as an image file
    fig.savefig('heatmap.png')

    return fig


# Do not modify the next two lines
draw_cat_plot()
draw_heat_map()
