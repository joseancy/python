'''write a program that prints out all the elements of the list that are less than 5.
    Take this list
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]'''
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
for item in a:
    if item < 5:
        newList.append(item)
print(newList)
