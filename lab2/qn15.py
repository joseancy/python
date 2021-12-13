"""Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new password."""

import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

total = lower + upper + number + symbols
passwordlen = 12

password =  "".join(random.sample(total,passwordlen))
print("Generated new strong password :",password)