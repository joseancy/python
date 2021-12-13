'''Write a Python program to write a list to a file.'''

list = ['Hello.','This is a test file.','Thank You All.']
with open('lab3/test.txt', "w") as f:
        for items in list:
                f.write(items + "\n" )

content = open('lab3/test.txt')
print(content.read())
f.close()