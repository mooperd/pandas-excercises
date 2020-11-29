import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

dataframe = pd.read_csv("https://raw.githubusercontent.com/mooperd/uk-towns/master/uk-towns-sample.csv")

# The result of df.groupby(...) is not a DataFrame. 
# To get a DataFrame back, you have to apply a function to each group, transform each element of a group, or filter the groups.

dataframe = dataframe.groupby(['nuts_region']).agg({'elevation': ['mean'],
                                                    'nuts_region': ['size']}).reset_index()
dataframe.columns = list(map('_'.join, dataframe.columns.values))

fig, ax1 = plt.subplots(figsize=(12,6))
dataframe.plot.bar(x='nuts_region_', ax=ax1)
plt.tight_layout()
plt.xticks(rotation=45, ha="right")
plt.show()


