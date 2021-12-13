'''Write a Python program to subtract five days from current date'''

from datetime import date, timedelta

sub_date = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before from Current Date :',sub_date)