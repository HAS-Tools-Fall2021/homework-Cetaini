# This code is for week 11 forecast assignment of HWRS_501
# HAS_TOOLS class
# Created by: Xiang Zhong
# Created on: 11/7/2021

# %%
# Import the modules we will use
import os
import xarray as xr
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter
import dataretrieval.nwis as nwis


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
# Define the parameters will be used later
Forecast_parm = np.zeros((2, 3))

# %%
# Get 1st parameter
station_id = '09506000'
start_formatted = '1989-01-01'
stop_formatted = '2021-11-06'
data = nwis.get_record(sites=station_id, service='dv',
                       start=start_formatted, end=stop_formatted,
                       parameterCd='00060')

date_form = DateFormatter("%y/%m/%d")
start_date = datetime.date(2021, 10, 17)
end_date = datetime.date(2021, 10, 30)
y_min = np.min(data.tail(14)['00060_Mean'])
y_max = np.max(data.tail(14)['00060_Mean'])

Forecast_parm[:, 0] = np.mean(data.tail(14)['00060_Mean'])

# %%
# Get 2nd parameter
m = 11
month_name = ['January', 'February', 'March', "April",
              'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
month_data = data[(data.index.month == m)]  # | (data.index.month == m - 1)]

month_week2_data = month_data[(month_data.index.day <= 13) &
                              (month_data.index.day > 6)]

month_week3_data = month_data[(month_data.index.day <= 20) &
                              (month_data.index.day > 13)]

Forecast_parm[0, 1] = stats.mode(month_week2_data['00060_Mean'])[0]
Forecast_parm[1, 1] = stats.mode(month_week3_data['00060_Mean'])[0]

# %%
# Get 3rd parameter
data_path = os.path.join('..', 'data',
                         'X184.183.149.211.310.11.11.38.nc')

dataset_nc = xr.open_dataset(data_path)

rhum = dataset_nc['rhum']
rhum = rhum.sel(lon=247.5, lat=35)
rhum_df = rhum.to_dataframe()
rhum_w = rhum_df.resample('W').mean()

# Get a timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
rhum_w.plot(y='rhum',
            marker='o',
            ax=ax,
            color='grey',
            markerfacecolor='purple',
            markeredgecolor='purple',
            legend=None)

ax.set(title="Weekly Mean of Relative Humidity at (112.5W, 35 N) \
(1/1/1989 - 11/6/2021)")
plt.savefig("HW11_Plot.png")

# Train the rh data
model_data = rhum_w['rhum']
flow_data_w = data['00060_Mean'].resample('W').mean()

model_data = pd.DataFrame(list(zip(rhum_w['rhum'], flow_data_w)),
                          columns=['rhum', 'flow'])
model_data = model_data[(model_data['rhum'] <= 20) &
                        (model_data['rhum'] >= 18)]

model = smf.ols('flow ~ rhum', data=model_data)
model = model.fit()

# Get from weather forecast
# https://www.myweather2.com/City-Town/United-States-Of-America/Arizona/Phoenix/14-Day-Forecast.aspx
week1_rhum = np.array([13, 14, 15, 17, 19, 23, 24, 19,
                       15, 15, 19, 26, 27, 27, 29, 22,
                       17, 18, 21, 23, 21, 23, 24, 20,
                       20, 22, 24, 27, 28, 31, 29, 21,
                       17, 16, 18, 20, 21, 23, 23, 14,
                       11, 11, 13, 14, 15, 16, 16, 12,
                       10, 10, 11, 12]).mean()
Forecast_parm[0, 2] = model.params.Intercept + model.params.rhum * week1_rhum

week2_rhum = np.array([21, 15, 13, 16, 15, 14, 12, 16,
                       16, 22, 13, 42, 25, 42, 19, 10,
                       34, 11, 24, 12, 27, 12, 15, 12,
                       21, 10, 16, 12]).mean()
Forecast_parm[1, 2] = model.params.Intercept + model.params.rhum * week2_rhum


# %%
weight_w1 = np.array([0.5, 0.3, 0.2])
Forecast_Week1 = cal_forecast(Forecast_parm[0, :], weight_w1)
print('Forecast value for next week is', Forecast_Week1)
weight_w2 = np.array([0.5, 0.3, 0.2])
Forecast_Week2 = cal_forecast(Forecast_parm[1, :], weight_w2)
print('Forecast value for next next week is', Forecast_Week2)

# %%
