"""Write a python program to count repeated characters in a string."""

import collections

string = "Repeated characters"
frequencies = collections.Counter(string)
repeated = {}

for key, value in frequencies.items():
    if value > 1:
        repeated[key] = value
print(repeated)
