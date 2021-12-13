'''
Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''
from datetime import datetime

current = datetime.now()
print("Current date and time:",current.strftime("%m/%d/%Y, %H:%M:%S"))
print("Current year:", current.strftime("%Y"))
print("Month of year:", current.strftime("%B"))
print("Week number of the year: ", current.strftime("%W"))
print("Weekday of the week: ", current.strftime("%w"))
print("Day of year: ", current.strftime("%j"))
print("Day of the month : ", current.strftime("%d"))
print("Day of week: ",current.strftime("%A"))
