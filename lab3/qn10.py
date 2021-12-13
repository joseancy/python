'''Write a Python program to count the frequency of words in a file.'''

from collections import Counter

def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :\n",word_count("lab3/test.txt"))