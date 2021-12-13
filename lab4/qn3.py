'''Write a Python program to convert unix timestamp string to readable date'''

from datetime import datetime

t = int("1284105682")
unix_time = datetime.fromtimestamp(t)
print(unix_time.strftime('%Y-%m-%d %H:%M:%S'))
