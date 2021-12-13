"""Write a Python program to generate all sublists of a list."""

def sub_lists(list):
    lists = [[]]
    for items in range(len(list) + 1):
        for item in range(items):
            lists.append(list[item : items])
    return lists
 
list = [1, 2, 3]
print(sub_lists(list))