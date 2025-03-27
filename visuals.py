import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Starts by pulling the data from the csv file
columns = ["Type", "Total", "Regular", "PseudoLedgendary", "Ledgendary", "Mythical", "Megas"]
df = pd.read_csv("Axis of Awesome Data - Sheet1.csv", usecols=columns)

# Basic scatterplot visualization for the data set
plt.scatter(df.Type, df.Total, color="red", label="Total")
plt.scatter(df.Type, df.Regular, color="orange", label="Regular")
plt.scatter(df.Type, df.PseudoLedgendary, color="green", label="Pseudo Ledgendary")
plt.scatter(df.Type, df.Ledgendary, color="blue", label="Ledgendary")
plt.scatter(df.Type, df.Mythical, color="purple", label="Mythical")
plt.scatter(df.Type, df.Megas, color="pink", label="Mega")

# Defines the axis labels
plt.xlabel('Type')
plt.ylabel('Number of Pokemon')
plt.legend() # Generates the legend
plt.show() # Shows the graph