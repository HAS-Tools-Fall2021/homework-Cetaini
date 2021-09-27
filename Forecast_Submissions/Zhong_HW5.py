# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('..','data', filename) # Added "'..'," here
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :)
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# %%
# Forecast
data.sort_values("datetime",ascending=False).iloc[0:14,:].describe()
data.sort_values("datetime",ascending=False).iloc[0:7,:].describe()

# %%
# 1. Provide a summary of the data frames properties
# column names
data.columns
# index
data.index
# data types of each column
data.info()

# %%
# 2. Provide a summary of the flow column including the min, max, standard deviation and quartiles
data[["flow"]].describe()

# %%
# 3. Monthly basis of flow column summary
data.groupby("month")[["flow"]].describe()

# %%
# 4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values.
data.sort_values("flow").tail()
data.sort_values("flow").head()

# %%
# 5. Find the highest and lowest flow values for every month of the year
for i in range(1,13,1):
        a = data[data.month == i].sort_values("flow",ascending = True).iloc[0,5]
        b = data[data.month == i].sort_values("flow",ascending = True).iloc[0,3]
        print('Min value happened for month #', i, 'is year: ', a)
        print('Min value is: ', b)
        c = data[data.month == i].sort_values("flow",ascending = False).iloc[0,5]
        d = data[data.month == i].sort_values("flow",ascending = False).iloc[0,3]
        print('Max value happened for month #', i, 'is year: ', c)
        print('Max value is: ', d)

# %%
# 6. A list of historical dates with flows that are within 10% of your week 1 forecast value.
week1 = 105
data[((data["flow"]-week1)/week1 <= .1) & ((data["flow"]-week1)/week1 >= -.1)].loc[:,'datetime']
