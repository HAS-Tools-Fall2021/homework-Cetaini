Name: Xiang Zhong
Date: 9/13/2021
Assignment Number: 3

1. Describe the variables flow, year, month, and day. What type of objects are they? What data types are they composed of? How long are they?
   They are all lists.
   Flow is composed of floats; year is composed of ints; month of ints; day of ints too.
   Their lengths are all 11943.

2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
   My prediction in the month of September is 94.
   8908 times the daily flow was greater than my prediction.

3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
   In or before 2000, 3509 times.
   In or after 2010, 3016 times.
   

4. How does the daily flow generally change from the first half of September to the second?
   Daily flow in the first half of September is generally more than the second.
   

I guessed the flow to be 94 because the flow has been decreasing for the last several days, and the forecast says there will still be sunny days for the next couple of days. The next next week to be 85 for the same reason.

The added scripts:


# %%
print(type(flow))
print(type(year))
print(type(month))
print(type(day))

print(type(flow[0]))
print(type(year[0]))
print(type(month[0]))
print(type(day[0]))

# %%
len(flow)
len(year)
len(month)
len(day)

# %%
i=0
for x in range(len(flow)):
        if flow[x]>94:
                i+=1
print(i)

# %%
i=0
for x in range(len(flow)):
        if flow[x]>94 and year[x]<=2000:
                i+=1
print(i)

# %%
i=0
for x in range(len(flow)):
        if flow[x]>94 and year[x]>=2010:
                i+=1
print(i)
# %%
first = []
second = []
i=0
for x in range(len(flow)):
        if month[x]==9 and day[x]<=15:
                first.append(flow[x])

i=0
for x in range(len(flow)):
        if month[x]==9 and day[x]>15:
                second.append(flow[x])

np.mean(second)-np.mean(first)

