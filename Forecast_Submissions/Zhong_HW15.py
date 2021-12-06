# %%
# Import the modules we will use
import Forecast_function as FF
import numpy as np
import pandas as pd
import csv
# i = 1  # Run on PC
i = 2  # Run on HPC
if (i == 1):
    import dataretrieval.nwis as nwis


# Define the parameters will be used later
Forecast_parm = np.zeros((2,2))

## Get 1st parameter
# Grab streamflow data
if (i == 1):
    station_id = '09506000'
    start_formatted = '1989-01-01'
    stop_formatted = '2021-12-04'
    data = nwis.get_record(sites=station_id, service='dv',
                        start=start_formatted, end=stop_formatted,
                        parameterCd='00060')
    data.to_csv('Zhong_HW15_StreamFlow.csv')
else:
    data = pd.read_csv('Zhong_HW15_StreamFlow.csv', parse_dates=['datetime'])
    data = data.set_index('datetime')

# Get the mean value of week_1 for each year
m = 12
week1_data = data[((data.index.month == m) &
                 (data.index.day >= 5)) |
                 ((data.index.month == m) &
                 (data.index.day <= 11))]

week1_data['year'] = week1_data.index.year

week1_data = week1_data.groupby(['year']).mean()

# Get the mean value of week_2 for each year
week2_data = data[(data.index.month == m) &
                 (data.index.day <= 18) &
                 (data.index.day >= 11)]

week2_data['year'] = week2_data.index.year

week2_data = week2_data.groupby(['year']).mean()

# Get the 1st parameter
Forecast_parm[0, 0] = np.median(week1_data['00060_Mean'])
Forecast_parm[1, 0] = np.median(week2_data['00060_Mean'])

## Get 2nd parameters
# Load precipitation data
if (i == 1):
    url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549" \
        "&vars=prcp&years=&format=csv"
    precip = pd.read_table(url, delimiter=',', skiprows=6)
    precip = precip[precip['year'] >= 1989]
    precip['prcp_s1'] = precip.iloc[:, 2].shift(1)
    precip['d_p'] = precip.iloc[:, 2] - precip.iloc[:, 3]
    precip.to_csv('Zhong_HW15_Precip.csv')
else:
    precip = pd.read_csv('Zhong_HW15_Precip.csv')

# Get a trend: df
data['flow_s1'] = data.iloc[:, 0].shift(1)
data['d_f'] = data.iloc[:, 0] - data.iloc[:, 3]
precip_dp = precip['d_p'][1: 11681]
data_sel = data[(data.index.year <= 2020) &
     ((data.index.month !=2) |
     ((data.index.month == 2) &
      (data.index.day != 29)))
     ]
flow_df = data_sel['d_f'][1: 11681]

model_data = pd.DataFrame(list(zip(precip_dp, flow_df)),
                     columns=['precip','flow'])
trend_nonzero = np.median(model_data[model_data['precip'] != 0]['flow'])
trend_zero = np.median(model_data[model_data['precip'] == 0]['flow'])

# Get trend for next two weeks
# Link: https://www.theweathernetwork.com/us/14-day-weather-trend/arizona/camp-verde
pop_week1 = np.array([0.2, 0.2, 0.3, 0.2, 0.6, 0.4, 0])  # pop is the probability of precipitation
pop_week2 = np.array([0, 0.2, 0.2, 0.3, 0.2, 0.1, 0.2])

trend_week1 = trend_nonzero * np.mean(pop_week1) + trend_zero * (1-np.mean(pop_week1))
trend_week2 = trend_nonzero * np.mean(pop_week2) + trend_zero * (1-np.mean(pop_week2))

# Forecast next two weeks' flow according to the trend
fore_week1 = np.zeros(7)
for i in range(1, 8):
    fore_week1[i-1] = data.tail(1)['00060_Mean'] + trend_week1 * i
fore_week2 = np.zeros(7)
for i in range(1, 8):
    fore_week2[i-1] = fore_week1[6] + trend_week2 * i

# 2nd parameters
Forecast_parm[0, 1] = np.mean(fore_week1)
Forecast_parm[1, 1] = np.mean(fore_week2)

# Get the final forecast value for next two weeks
fore_week1_final = FF.cal_forecast(Forecast_parm[0, :], np.array([0.1, 0.9]))
print('The forecast value for week 1 is: ', fore_week1_final)
fore_week2_final = FF.cal_forecast(Forecast_parm[1, :], np.array([0.2, 0.8]))
print('The forecast value for week 2 is: ', fore_week2_final)
# %%
