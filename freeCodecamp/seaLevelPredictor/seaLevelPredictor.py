import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    reg = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
    oldLastYear = df['Year'].max()
    futureYears = np.arange(oldLastYear + 1, 2051, dtype=int)

    dfNew = pd.DataFrame({'Year': futureYears})
    df = df.append(dfNew)
    plt.scatter(df['Year'], df["CSIRO Adjusted Sea Level"])
    yCalculated = reg.slope * df['Year'] + reg.intercept
    plt.plot(df['Year'], yCalculated, 'r')
    plt.xlim(xmin=1850, xmax=2075)

    # Create second line of best fit
    dfClean = df.loc[(df['Year'] >= 2000) & (df['Year'] <= 2013)]
    plt.scatter(dfClean['Year'], dfClean["CSIRO Adjusted Sea Level"])
    regNew = linregress(dfClean['Year'], dfClean["CSIRO Adjusted Sea Level"])
    dfFiltered = df.loc[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]
    plt.plot(dfFiltered['Year'], regNew.slope * dfFiltered['Year'] + regNew.intercept, "r")
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xlim(xmin=1850, xmax=2075)
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()