import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv", sep = ",")

# Add 'overweight' column
df["overweight"] = df["weight"]/(df["height"]/100)**2
df["overweight"] = df["overweight"].map(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].map(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].map(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df,id_vars = ["cardio"] , value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    
    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = plt.figure()
    g = sns.catplot(data = df_cat, kind="count", x="variable", hue="value", col="cardio")
    fig = g.fig
    plt.xlabel("variable")
    plt.ylabel("total")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_hi"] >= df["ap_lo"]) & 
         (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975)) & 
         (df["weight"] >= df["weight"].quantile(0.025)) & (df["weight"] <= df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(df_heat.corr())

    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    sns.heatmap(ax=ax, data=corr, annot=True, fmt='.1f', mask=mask)

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
