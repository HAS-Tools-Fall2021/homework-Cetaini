Name: Xiang Zhong
Date: 9/20/2021
Assignment Number: 4


_________
## Grade: 
**3/3**: great job! Your script is very clean and easy to folow and I like the logic of your forecast.  Next time add some markdown formatting to your title. If you preview this you will see it is all ending up on one line. If you have questions about how to do the markdown formatting refer to the cheet sheet or feel free to ask me questions.  
_________

1. Provide a summary of the forecast values you picked and why. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.
- My pick value for next week is 92, the one ahead is still 92. Because I checked the recent trend, and it seems the flow has kind of been frozen to around 92. The median value for last week is 91.3. The quantile for 0, 0.1, 0.5, and 0.9 are 90.8, 91.07, 94.9, 96.88 seperately. I checked the histogram of September for all 33 years and also for 2021 only, they all peaked at around 90.

2. Describe the variable flow_data:
        What is it?
        - It is a numpy array.
        What type of values is is composed of?
        - It is composed of floats.
        What is are its dimensions, and total size?
        - It is a 2-D array, and the total size is 47800.

3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
- 331 times, and around 32.36%.

4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
- In and before 2000: 126, and ~33.87%.
- In and after 2010: 138, and ~37.10%.

5. How does the daily flow generally change from the first half of September to the second?
- In general, the daily flow in the first half of September is greater than the second.

The added python codes are from Line 41 to Line 104.

