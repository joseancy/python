'''Write a Python program to count the number of lines in a text file.'''

file = open("lab3/test.txt","r")
Count = 0

Content = file.read()
lines = Content.split("\n")
  
for i in lines:
    if i:
        Count += 1
                  
print("Count of lines in the file :",Count)
