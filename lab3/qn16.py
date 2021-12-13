'''Write a Python program to remove newline characters from a file.'''

def remove_newlines(fname):
    list = open(fname).readlines()
    return [s.rstrip('\n') for s in list]

print(remove_newlines("lab3/test.txt"))