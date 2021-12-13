"""Write a Python program to count the number of characters (character frequency) in a string."""

test_str = "characterfrequency"
all_freq = {}
  
for n in test_str:
    if n in all_freq:
        all_freq[n] += 1
    else:
        all_freq[n] = 1

print(all_freq)