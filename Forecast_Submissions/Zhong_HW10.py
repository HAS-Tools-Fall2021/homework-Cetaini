# This code is for week 10 forecast assignment of HWRS_501
# HAS_TOOLS class
# Created by: Xiang Zhong
# Created on: 10/29/2021

# %%
# Import the modules we will use
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter
import dataretrieval.nwis as nwis
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression


def cal_forecast(parm_name, weight):
    """ Get forecast values.
    ------------------------------------------
    Parameters:
    Parm_name = 1D numpy array
                contains parameters for the forecast.

    Weight = 1D numpy array
             numbers between 0 to 1, and the
             summation should be 1.
    ------------------------------------------
    Returns:
    Forecast = integer
               of forecast value.
    """

    Forecast = np.sum(parm_name * weight)
    return(round(Forecast))


# %%
station_id = '09506000'
start_formatted = '1989-01-01'
stop_formatted = '2021-10-30'
data = nwis.get_record(sites=station_id, service='dv',
                       start=start_formatted, end=stop_formatted,
                       parameterCd='00060')

# %%
# Define the parameters will be used later
Forecast_parm = np.zeros((2, 4))

# %%
# Generate Plot #1
# Time series of flow values for recent two weeks
date_form = DateFormatter("%y/%m/%d")
start_date = datetime.date(2021, 10, 17)
end_date = datetime.date(2021, 10, 30)
y_min = np.min(data.tail(14)['00060_Mean'])
y_max = np.max(data.tail(14)['00060_Mean'])

fig, ax = plt.subplots()
ax.plot(data['00060_Mean'], '.-m', label='flow')
ax.xaxis.set_major_formatter(date_form)
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       xlim=[start_date, end_date],
       ylim=[y_min - 1, y_max + 1])
plt.setp(ax.get_xticklabels(), rotation=45)

fig.set_size_inches(6, 7)
fig.savefig("HW10_Plot_1.png")

Forecast_parm[:, 0] = np.mean(data.tail(14)['00060_Mean'])

# %%
# Generate Plot #2
# Histogram of October
fig, ax = plt.subplots(1, 2)

m = 11
month_name = ['January', 'February', 'March', "April",
              'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
month_data = data[(data.index.month == m) | (data.index.month == m - 1)]

month_week1_data = month_data[((month_data.index.day <= 6) &
                              (month_data.index.month == m)) |
                              ((month_data.index.day > 30) &
                              (month_data.index.month == m - 1))]
plot_title = month_name[m-1] + "'s First Week"
ax[0].hist(month_data['00060_Mean'], bins=50, color='steelblue')
ax[0].set(xlabel='Flow (cfs)', ylabel='Frequency', title=plot_title)

month_week2_data = month_data[(month_data.index.day <= 13) &
                              (month_data.index.day > 6) &
                              (month_data.index.month == m)]
plot_title = month_name[m-1] + "'s Second Week"
ax[1].hist(month_data['00060_Mean'], bins=50, color='steelblue')
ax[1].set(xlabel='Flow (cfs)', ylabel='Frequency', title=plot_title)

fig.set_size_inches(8, 3.5)
fig.savefig("HW10_Plot_2.png")

Forecast_parm[0, 1] = stats.mode(month_week1_data['00060_Mean'])[0]
Forecast_parm[1, 1] = stats.mode(month_week2_data['00060_Mean'])[0]

# %%
# Generate Plot #3
# Scatterplot of this years flow vs last years flow for September
Last = data[(data.index.year == 2020) & (data.index.month == 10)]['00060_Mean']
Current = data[(data.index.year == 2021) & (data.index.month == 10)]\
          ['00060_Mean']

data_reg = pd.DataFrame(list(zip(Last[0:len(Current)], Current)),
                        columns=['Last', 'Current'])
model = smf.ols('Current ~ Last', data=data_reg)
model = model.fit()

fig, ax = plt.subplots()

ax.scatter(data_reg['Last'], data_reg['Current'],
           marker='p', color='Orange')
ax.set(xlabel='2020 flow', ylabel='2021 flow',
       title='Flow in October')
ax.plot(data_reg['Last'],
        data_reg['Last']*model.params.Last+model.params.Intercept)

fig.set_size_inches(5, 3.5)
fig.savefig("HW10_Plot_3.png")

Forecast_parm[0, 2] = np.mean(data[((data.index.year == 2020) &
                                   (data.index.month == 10) &
                                   (data.index.day > 30)) |
                                   ((data.index.year == 2020) &
                                   (data.index.month == 11) &
                                   (data.index.day <= 6))]
                                  ['00060_Mean'])*model.params.Last+model.\
                                  params.Intercept
Forecast_parm[1, 2] = np.mean(data[(data.index.year == 2020) &
                                   (data.index.month == 11) &
                                   (data.index.day <= 13) &
                                   (data.index.day > 6)]
                                  ['00060_Mean'])*model.params.Last+model.\
                                  params.Intercept

# %%
# First Create the URL for the rest API
# Insert token
mytoken = '15942499399a49ab9e32bbb36f7c72f6'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data
# Note that end date will not be included
args = {
    'start': '199701010000',
    'end': '202110310000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum_24_hour',
    'stids': 'KPRC',
    'units': 'temp|F, precip|mm',
    'token': mytoken}

# Takes arguments and paste them together
# into a string for the api
apiString = urllib.parse.urlencode(args)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString

# Get the API response
response = req.urlopen(fullUrl)

# Read the data
responseDict = json.loads(response.read())

# Grab variables
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']\
                     ['precip_accum_24_hour_set_1']

# Combine this into a pandas data frame
data_precip = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_precip_daily = data_precip.resample('D').sum()

# %%
# Generate Plot 4
# Time series of flow values for recent two weeks
date_form = DateFormatter("%y/%m/%d")
data_flow_weekly = data.resample('W').mean()
data_precip_weekly = data_precip_daily.resample('W').mean()

start_date = datetime.date(2000, 10, 29)
end_date = datetime.date(2021, 10, 30)

fig, ax = plt.subplots()
ax.plot(data['00060_Mean'], marker='.',
        color='darkgreen', label='flow')
ax.xaxis.set_major_formatter(date_form)
ax.set(title="Observed Flow & Weekly Precipitation",
       xlabel="Date",
       xlim=[start_date, end_date],
       yscale='log')
ax.set_ylabel(ylabel="Weekly Avg Flow [cfs]", color="darkgreen")
ax.tick_params(axis='y', colors='darkgreen')
plt.setp(ax.get_xticklabels(), rotation=45)
ax2 = ax.twinx()
ax2.plot(data_precip_weekly['Precip'], marker='.',
         color='blue', label='precipitation')
ax2.set_ylabel("Weekly Precipitation [mm/day]",
               color="blue")
ax2.tick_params(axis='y', colors='blue')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

fig.set_size_inches(12, 7)
fig.savefig("HW10_Plot_4.png")

# %%
# Generate 4th parameter through sklearn model
model_data = data_flow_weekly[data_flow_weekly.index.date >=
                              datetime.date(2000, 10, 29)]
# Step 1: setup a lag 1 array
model_data['precip_tm1'] = data_precip_weekly['Precip'].shift(1)
model_data['precip_tm2'] = data_precip_weekly['Precip'].shift(2)

# Step 2 - pick training data and test data
train = model_data[2:400][['00060_Mean', 'precip_tm1', 'precip_tm2']]
test = model_data[400:][['00060_Mean', 'precip_tm1', 'precip_tm2']]

# Step 3: Fit a linear regression model using sklearn
model_w1 = LinearRegression()
x_w1 = train['precip_tm1'].values.reshape(-1, 1)
y_w1 = train['00060_Mean'].values
model_w1.fit(x_w1, y_w1)

model_w2 = LinearRegression()
x_w2 = train['precip_tm2'].values.reshape(-1, 1)
y_w2 = train['00060_Mean'].values
model_w2.fit(x_w2, y_w2)

# Look at the results
# r^2 values
r_sq_w1 = model_w1.score(x_w1, y_w1)
print('coefficient of determination:', np.round(r_sq_w1, 2))

r_sq_w2 = model_w2.score(x_w2, y_w2)
print('coefficient of determination:', np.round(r_sq_w2, 2))

# Get the fourth parameter
last_week_precip = data_precip_weekly.tail(1)['Precip']
Forecast_parm[0, 3] = model_w1.intercept_ + model_w1.coef_ * last_week_precip
Forecast_parm[1, 3] = model_w2.intercept_ + model_w2.coef_ * last_week_precip

# %%
weight_w1 = np.array([0.5, 0.2, 0.2, 0.1])
Forecast_Week1 = cal_forecast(Forecast_parm[0, :], weight_w1)
print('Forecast value for next week is', Forecast_Week1)
weight_w2 = np.array([0.4, 0.2, 0.3, 0.1])
Forecast_Week2 = cal_forecast(Forecast_parm[1, :], weight_w2)
print('Forecast value for next next week is', Forecast_Week2)

# %%
