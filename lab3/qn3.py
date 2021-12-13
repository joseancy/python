'''Write a Python program to append text to a file and display the text.'''

file1 = open("lab3/test.txt", "a")
file1.write("Every One \nReadlines after appending \n")
file1.close()

file1 = open("lab3/test.txt", "r")
print(file1.read())
print()
file1.close()
