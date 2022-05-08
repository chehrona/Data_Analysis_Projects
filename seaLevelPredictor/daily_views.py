import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=["date"], parse_dates=['date'])

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025))
            & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax = sns.lineplot(data=df, x='date', y='value', color='r')
    ax.set_xlabel("Date")
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    plt.show()
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_graph = df.groupby(pd.Grouper(freq='M')).mean()
    df_graph.rename(columns={'value': 'mean'}, inplace=True)
    df_graph.reset_index(inplace=True)
    df_graph['year'] = [d.year for d in df_graph.date]
    df_graph['month'] = [d.strftime('%B') for d in df_graph.date]
    fig, ax = plt.subplots(figsize=(16, 9))
    ax = sns.barplot(data=df_graph, x='year', y='mean', hue='month')
    ax.set_xlabel("Years")
    ax.set_ylabel('Average Page Views')
    plt.legend(
        title="Months",
        loc="upper left",
        labels=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    )

    # Draw bar plot

    # Save image and return fig (don't change this part)
    plt.show()
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.set_theme(style="white")
    fig, axes = plt.subplots(1, 2, figsize=(16, 9))
    sns.boxplot(x=df_box["year"], y=df_box["value"], data=df_box, ax=axes[0])
    sns.boxplot(x=df_box["month"], y=df_box["value"], data=df_box, ax=axes[1], order=[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ], )
    axes[0].set_ylabel('Page Views')
    axes[0].set_xlabel('Year')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    plt.show()
    return fig


draw_box_plot()