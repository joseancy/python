'''Write a program that asks the user to enter their name and their age. 
   Print out a message that greets them and that tells them the year 
   that they will turn 100 years old.'''

from datetime import datetime

name = input('What is your name?\n')
age = int(input('How old are you?\n'))
hundred = int((100-age) + datetime.now().year)
print ('Hi %s. You are %d years old. You will turn 100 years old in %d.' % (name, age, hundred))

