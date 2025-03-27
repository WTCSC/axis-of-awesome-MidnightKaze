import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Starts by pulling the data from the csv file
columns = ["Type", "Total", "Regular", "PseudoLedgendary", "Ledgendary", "Mythical", "Megas"]
df = pd.read_csv("data.csv", usecols=columns)

# Basic scatterplot visualization for the data set
plt.scatter(df.Type, df.Total, color="red", label="Total")
plt.scatter(df.Type, df.Regular, color="orange", label="Regular")
plt.scatter(df.Type, df.PseudoLedgendary, color="green", label="Pseudo Ledgendary")
plt.scatter(df.Type, df.Ledgendary, color="blue", label="Ledgendary")
plt.scatter(df.Type, df.Mythical, color="purple", label="Mythical")
plt.scatter(df.Type, df.Megas, color="pink", label="Mega")

# Generates the legend
plt.legend()

# Defines the axis labels
plt.xlabel('Type')
plt.ylabel('Number of Pokemon')

# More complex double donut visualization
# Preperation for the outside donut
plt.figure(figsize=(7, 7))
labels = df.Type
sizes = df.Total
colors = ["#a8a878", "#f08030", "#6890f0", "#78c850", "#f8d030", "#98d8d8", "#c03028", "#a040a0", "#e0c068", "#a890f0", "#f85888", "#a8b820", "#b8a038", "#705898", "#7038f8", "#705848", "#b8b8d0", "#ee99ac"]
explode = [0] * len(labels)
textprops = {"fontsize":14, "color":"black"}

plt.pie(sizes,
        explode=explode,
        pctdistance =0.9,
        labels=labels,
        colors=colors,
        autopct="%.2f%%",
        shadow=False,
        textprops =textprops,
        wedgeprops={"linewidth": 3.0, "edgecolor": "white"})

center_circle = plt.Circle((0,0),0.65, color="grey", fc="white", linewidth=1.00)
fig = plt.gcf()
fig.gca().add_artist(center_circle)
plt.axis("equal")

# Shows the graph
plt.show()