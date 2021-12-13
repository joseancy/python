"""Write a Python program to find the index of an item of a tuple."""

tup = tuple("index tuple")
print(tup)

index = tup.index("i")
print('The index of i :', index)

index1 = tup.index("e")
print('The index of e :', index1)

# 'e' after the 4th index is searched
index2 = tup.index('e', 4)   
print('The index of e :', index2)

