# Forecast_Submissions

## Name: Xiang Zhong

### Date: 9/27/2021

### Assignment Number: 5
_______
### Grade
3/3: Awesome job! Great work figuring out the for loop for question 5, that part was tricky. 
_________

        This week my forecast is based on median value for last two weeks (94.9) and last week (101.0). Cloudy weather seems will last for a while, so my forecast value for next week will be 105, and next next week 108.

### 1. Provide a summary of the data frames properties
   - Column names: 'agency_cd', 'site_no', 'datetime', 'flow', 'code', 'year', 'month', 'day'.
   - Index: It is a range index, from 0 to 11957.
   - Data yepes of each column:
     'agency_cd': object

     'site_no': int64

     'datetime': object

     'flow': float64

     'code': object

     'year': int32

     'month': int32

     'day': int32
### 2. Provide a summary of the flow column including the min, max, standard deviation and quartiles
   - min: 19.00
   - max: 63400.00
   - standard deviation: 1391.11
   - 25%: 93.50
   - 50%: 157.00
   - 75%: 214.00
### 3. Monthly basis of flow column summary
   Take September as example:
   - min: 37.5
   - max: 5590.0
   - standard deviation: 282.65
   - 25%: 88.625
   - 50%: 118.0
   - 75%: 169.00
### 4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values.
   - 5 highest: 
  
     1993-01-08, 63400.0; 

     1993-02-20, 61000.0; 

     1995-02-15, 45500.0; 

     2005-02-12, 35600.0; 

     1995-03-06, 30500.0.

   - 5 lowest:
  
     2012-07-01, 19.0;

     2012-07-02, 20.1;

     2012-06-30, 22.1;

     2012-06-29, 22.5;

     2012-07-03, 23.4.
### 5. Find the highest and lowest flow values for every month of the year
        Min value happened for month # 1 is year:  2003
        Min value is:  158.0
        Max value happened for month # 1 is year:  1993
        Max value is:  63400.0
        Min value happened for month # 2 is year:  1991
        Min value is:  136.0
        Max value happened for month # 2 is year:  1993
        Max value is:  61000.0
        Min value happened for month # 3 is year:  1989
        Min value is:  97.0
        Max value happened for month # 3 is year:  1995
        Max value is:  30500.0
        Min value happened for month # 4 is year:  2018
        Min value is:  64.9
        Max value happened for month # 4 is year:  1991
        Max value is:  4690.0
        Min value happened for month # 5 is year:  2004
        Min value is:  46.0
        Max value happened for month # 5 is year:  1992
        Max value is:  546.0
        Min value happened for month # 6 is year:  2012
        Min value is:  22.1
        Max value happened for month # 6 is year:  1992
        Max value is:  481.0
        Min value happened for month # 7 is year:  2012
        Min value is:  19.0
        Max value happened for month # 7 is year:  2021
        Max value is:  5270.0
        Min value happened for month # 8 is year:  2019
        Min value is:  29.6
        Max value happened for month # 8 is year:  1992
        Max value is:  5360.0
        Min value happened for month # 9 is year:  2020
        Min value is:  37.5
        Max value happened for month # 9 is year:  2004
        Max value is:  5590.0
        Min value happened for month # 10 is year:  2020
        Min value is:  59.8
        Max value happened for month # 10 is year:  2010
        Max value is:  1910.0
        Min value happened for month # 11 is year:  2016
        Min value is:  117.0
        Max value happened for month # 11 is year:  2004
        Max value is:  4600.0
        Min value happened for month # 12 is year:  2012
        Min value is:  155.0
        Max value happened for month # 12 is year:  2004
        Max value is:  28700.0
### 6. A list of historical dates with flows that are within 10% of your week 1 forecast value.
   - There are 1098 dates within 10% of my week 1 forecast value (105). 
  
        81       1989-03-23

        82       1989-03-24

        83       1989-03-25

        96       1989-04-07

        97       1989-04-08

                ...  

        11950    2021-09-20

        11951    2021-09-21

        11952    2021-09-22

        11953    2021-09-23

        11955    2021-09-25

        Name: datetime, Length: 1098, dtype: object
        
   
