'''Write a python program to find the longest words.'''

def longest_word(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('lab3/test.txt'))