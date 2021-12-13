"""Write a Python program to remove an item from a set if it is present in the set."""

# using discard() method
sets = set([10, 20, 30, 40, 50, 10])
sets.discard(10)
print(sets) 

# using remove() method
sets1 = set([10, 20, 30, 40, 50, 10])
sets1.remove(40)
print(sets1)     