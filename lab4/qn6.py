'''Write a Python program to calculate the sum of a list of numbers'''

total = 0
list1 = [20, 50, 10, 10, 30]

for items in range(0, len(list1)):
    total = total + list1[items]
 
print("Sum of all elements in given list: ", total)
