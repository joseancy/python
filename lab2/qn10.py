"""Write a Python program to reverse a tuple."""

def Reverse(tuples):
    new_tuples = tuples[::-1]
    return new_tuples
      
tuples = ('R','e','v','e','r','s','e','t','u','p','l','e','s')
print(Reverse(tuples))