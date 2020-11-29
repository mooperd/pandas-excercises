from tabulate import tabulate
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.dates as mdates
sns.set_theme(style="whitegrid")
rcParams.update({'figure.autolayout': True})
rcParams["date.autoformatter.month"] = "%b %Y"

dataframe = pd.read_csv("bank-transactions.csv")


# convert dates to datetime
dataframe['Date'] = pd.to_datetime(dataframe['Date'])
dataframe = dataframe.drop(["Account number", "Amount (Foreign Currency)", "Type Foreign Currency", "Exchange Rate", "Payment reference"], axis=1)

# print(dataframe)

# grouped_dataframe = dataframe.groupby([pd.Grouper(key = 'Date', freq = 'M'), "Transaction type"]).agg({"Amount (EUR)": "sum"}).reset_index()
grouped_dataframe = dataframe.groupby([pd.Grouper(key='Date', freq='M'), "Transaction type"])[["Amount (EUR)"]].sum()

# print(grouped_dataframe)

grouped_dataframe_unstacked = grouped_dataframe.unstack()
fig, ax = plt.subplots(figsize=(6, 10))
grouped_dataframe.unstack().plot(kind='bar', ax=ax, stacked=True)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# plt.xticks(rotation=45, ha="right")
plt.show()