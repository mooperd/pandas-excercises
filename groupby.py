import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")


dataframe = pd.read_csv("https://raw.githubusercontent.com/mooperd/uk-towns-amazing/edit/uk-towns-sample.csv")

# The result of df.groupby(...) is not a DataFrame. 
# To get a DataFrame back, you have to apply a function to each group, transform each element of a group, or filter the groups.

dataframe = dataframe.groupby(['nuts_region']).size().reset_index(name='size')

# Draw a barplot

g = sns.catplot(
    data=dataframe, kind="bar",
    x="nuts_region", y="size",
    ci="sd", palette="dark", height=6
)
g.despine(left=True)
g.set_axis_labels("", "Number of Towns")
# Set the labels
g.set_xticklabels(rotation=-90, ha="left")
g.tight_layout()
# g.legend.set_title("")

plt.show()

print(dataframe)