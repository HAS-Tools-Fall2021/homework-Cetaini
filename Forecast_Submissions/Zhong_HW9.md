# Forecast_Submissions

## Name: Xiang Zhong

### Date: 10/25/2021

### Assignment Number: 9
____________


### Plot #1
![Getting Started](HW9_Plot_1.png)

The first plot is for the time series in recent two weeks.

Take the average as the first parameter.

### Plot #2
![Getting Started](HW9_Plot_2.png)

The second plot is histograms for historical 10/24-10/30, and for 10/31-11/6.

Take the mode values for each category as the second parameter

### Plot #3
![Getting Started](HW9_Plot_3.png)

The third plot is a scatterplot between September flow in the current year and which in last year.

Try to establish a linear relationship between the two series, and get the third parameter from the predicted value.

### Plot #4
![Getting Started](HW9_Plot_4.png)

The last plot is the timeseries of the flow and the precipitation for the overlappting period of both data. The value is weekly average.

Fourth parameter is extracted from a learning model build between flow value and lag-1 precipitation and lag-2 precipitation value separately.

---
### Summary
This time I used a weighted average method to get the forecast value, and wrote it as a function. Forecast parameters are described above.

The final predicted value for next week is 162, for next next week is 167 cfs.
