import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columns = ["Type", "Total", "Regular"]
df = pd.read_csv("Axis of Awesome Data - Sheet1.csv", usecols=columns)
plt.plot(df.Type, df.Total, df.Regular)
plt.show()