# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
# note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('..', 'data', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
# 1. Timeseries of observed flow values
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], '-k', label='daily')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Daily Avg Flow [cfs]",
        yscale='log')
ax.legend()

# %%
#2. Time series of flow values with the x axis range limited to recent two weeks
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'],'.-m', label='flow')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        xlim=[datetime.date(2021, 9, 18), datetime.date(2021, 10, 2)],
        ylim=[80,250])

# %%
#3. Histogram of October
fig, ax = plt.subplots()

m = 10
month_data = data[data['month'] == m]
plot_title = 'Month ' + str(m)
ax.hist(month_data['flow'], bins=50, color='steelblue')
ax.set(xlabel='Flow cfs', ylabel='count', title=plot_title)

# %%
#4 Boxplot of flows by month in selected years
Sep_mean_2021 = np.mean(data[(data['month'] == 9) & (data['year'] == 2021)])['flow']
Years = []
for i in range(1989, 2021):
        x = np.mean(data[(data['month'] == 9) & (data['year'] == i)])['flow']
        if abs(x - Sep_mean_2021) <= (Sep_mean_2021 * 0.1):
                Years.append(i)
Oct_slc_data = data[(data['day'] <= 7) & (data['month'] == 10) & ((data['year'] == Years[0]) | (data['year'] == Years[1]) | (data['year'] == Years[2]) | (data['year'] == Years[3]) | (data['year'] == Years[4]))]

fig, ax = plt.subplots()
ax = sns.boxplot(x="year", y="flow",  data=Oct_slc_data,
                 linewidth=0.3)
ax.set_xlabel('Year')
ax.set_ylabel('Flow (cfs)')

# %%
# 5. Plot the October flows for the selected years
#making a color palette to use for plotting (using the viridis one here with 12 colors)
mypal = sns.color_palette('Reds', 5)
mypal
colpick = 0
fig, ax = plt.subplots()

Sep_mean_2021 = np.mean(data[(data['month'] == 9) & (data['year'] == 2021)])['flow']
Years = []
for i in range(1989, 2021):
        x = np.mean(data[(data['month'] == 9) & (data['year'] == i)])['flow']
        if abs(x - Sep_mean_2021) <= (Sep_mean_2021 * 0.1):
                Years.append(i)

for i in Years:
        plot_data=data[(data['year']==i) & (data['month']==10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=mypal[colpick], label=i)
        ax.legend()
        colpick = colpick+1

# %%
#6. scatterplot this years flow vs last years flow for September
fig, ax = plt.subplots()

ax.scatter(data[(data['year'] == 2020) & (data['month'] == 9)].flow,  data[(data['year'] == 2021) & (data['month'] == 9)].flow, marker='p',
           color='Orange')
ax.set(xlabel='2020 flow', ylabel='2021 flow')
ax.legend()

Forecast = data[(data['year'] == 2020) & (data['month'] == 10) & (data['day'] <= 7)]['flow']
Forecast = np.mean(Forecast)
Forecast = Forecast * 2 + 90
print(Forecast)
