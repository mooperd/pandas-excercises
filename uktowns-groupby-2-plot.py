import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
sns.set_theme(style="whitegrid")
rcParams.update({'figure.autolayout': True})

dataframe = pd.read_csv("https://raw.githubusercontent.com/mooperd/uk-towns/master/uk-towns-sample.csv")

# The result of df.groupby(...) is not a DataFrame. 
# To get a DataFrame back, you have to apply a function to each group, transform each element of a group, or filter the groups.

dataframe = dataframe.groupby(['nuts_region']).agg({'elevation': ['mean'],
                                                    'nuts_region': ['size']}).reset_index()
dataframe.columns = list(map('_'.join, dataframe.columns.values))

# We need to melt our dataframe down into a different format that can be put into the graph.
# 'Melting' is converting a table from wide into long format. 
# This gives us two columns: ‘variable’ and ‘value’.
# https://en.wikipedia.org/wiki/Wide_and_narrow_data
#                Nuts_Region_          Variable       Value
#0              East Midlands    elevation_mean   88.192308
#1                    Eastern    elevation_mean   60.256198
#2                Isle of Man    elevation_mean  130.000000
#3                     London    elevation_mean   52.142857
#4                 North East    elevation_mean  101.621622
tidy = dataframe.melt(id_vars='nuts_region_').rename(columns=str.title)
print(tidy)
# Create a subplot. A Subplot makes it convenient to create common layouts of subplots.
# https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html
fig, ax1 = plt.subplots(figsize=(6, 6))
# ax1.tick_params(labelrotation=-90)
# https://stackoverflow.com/questions/40877135/plotting-two-columns-of-dataframe-in-seaborn
g = sns.barplot(x='Nuts_Region_', y='Value', hue='Variable', data=tidy, ax=ax1)

plt.tight_layout()
plt.xticks(rotation=45, ha="right")
plt.show()


