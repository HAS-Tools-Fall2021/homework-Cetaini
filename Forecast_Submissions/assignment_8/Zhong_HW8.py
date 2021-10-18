# This code is for week 8 forecast assignment of HWRS_501
# HAS_TOOLS class
# Created by: Xiang Zhong
# Created on: 10/17/2021

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter


def cal_forecast(parm_name, weight1, weight2, weight3):
    """ Get forecast values.
    ------------------------------------------
    Parameters:
    Parm_name = 1D numpy array
                contains parameters for the forecast.

    Weight1 to 3 = float
                   numbers between 0 to 1, and the
                   summation should be 1.
    ------------------------------------------
    Returns:
    Forecast = integer
               of forecast value.
    """

    Forecast = weight1*parm_name[0] + weight2*parm_name[1] + \
        weight3*parm_name[2]

    return(round(Forecast))


# %%
# Set the file name and path to the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('..', '..', 'data', filename)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30, names=['agency_cd',
                     'site_no', 'datetime', 'flow', 'code'],
                     parse_dates=['datetime'],
                     index_col=['datetime'])

# %%
# Define the parameters will be used later
Forecast_parm = np.zeros((2, 3))

# %%
# Generate Plot #1
# Time series of flow values for recent two weeks
date_form = DateFormatter("%y/%m/%d")

fig, ax = plt.subplots()
ax.plot(data['flow'], '.-m', label='flow')
ax.xaxis.set_major_formatter(date_form)
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       xlim=[datetime.date(2021, 10, 3), datetime.date(2021, 10, 16)],
       ylim=[120, 240])
plt.setp(ax.get_xticklabels(), rotation=45)

fig.set_size_inches(6, 7)
fig.savefig("HW8_Plot_1.png")

Forecast_parm[:, 0] = np.mean(data.tail(14)['flow'])

# %%
# Generate Plot #2
# Histogram of October
fig, ax = plt.subplots(1, 2)

m = 10
month_name = ['January', 'February', 'March', "April",
              'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
month_data = data[data.index.month == m]

month_week2_data = month_data[(month_data.index.day <= 23) &
                              (month_data.index.day > 16)]
plot_title = month_name[m-1] + "'s Third Week"
ax[0].hist(month_data['flow'], bins=50, color='steelblue')
ax[0].set(xlabel='Flow (cfs)', ylabel='Frequency', title=plot_title)

month_week3_data = month_data[(month_data.index.day <= 30) &
                              (month_data.index.day > 23)]
plot_title = month_name[m-1] + "'s Fourth Week"
ax[1].hist(month_data['flow'], bins=50, color='steelblue')
ax[1].set(xlabel='Flow (cfs)', ylabel='Frequency', title=plot_title)

fig.set_size_inches(8, 3.5)
fig.savefig("HW8_Plot_2.png")

Forecast_parm[0, 1] = stats.mode(month_week2_data['flow'])[0]
Forecast_parm[1, 1] = stats.mode(month_week3_data['flow'])[0]

# %%
# Generate Plot #3
# Scatterplot of this years flow vs last years flow for September
Last = data[(data.index.year == 2020) & (data.index.month == 9)]['flow']
Current = data[(data.index.year == 2021) & (data.index.month == 9)]['flow']

data_reg = pd.DataFrame(list(zip(Last, Current)), columns=['Last', 'Current'])
model = smf.ols('Current ~ Last', data=data_reg)
model = model.fit()

fig, ax = plt.subplots()

ax.scatter(data[(data.index.year == 2020) & (data.index.month == 9)].flow,
           data[(data.index.year == 2021) & (data.index.month == 9)].flow,
           marker='p', color='Orange')
ax.set(xlabel='2020 flow', ylabel='2021 flow',
       title='Flow in September')
ax.plot(data_reg['Last'],
        data_reg['Last']*model.params.Last+model.params.Intercept)

fig.set_size_inches(5, 3.5)
fig.savefig("HW8_Plot_3.png")

Forecast_parm[0, 2] = np.mean(data[(data.index.year == 2020) &
                                   (data.index.month == 10) &
                                   (data.index.day <= 23) &
                                   (data.index.day > 16)]
                                  ['flow'])*model.params.Last+model.\
                                  params.Intercept
Forecast_parm[0, 2] = np.mean(data[(data.index.year == 2020) &
                                   (data.index.month == 10) &
                                   (data.index.day <= 30) &
                                   (data.index.day > 23)]
                                  ['flow'])*model.params.Last+model.\
                                  params.Intercept

Forecast_Week1 = cal_forecast(Forecast_parm[0, :], 0.5, 0.2, 0.3)
print('Forecast value for next week is', Forecast_Week1)
Forecast_Week2 = cal_forecast(Forecast_parm[1, :], 0.4, 0.2, 0.4)
print('Forecast value for next next week is', Forecast_Week2)

# %%
