'''Write a Python program to combine each line from first file with the corresponding line in second file.'''

with open('lab3/test.txt') as file1, open('lab3/test2.txt') as file2:
    for line1, line2 in zip(file1, file2):
       
        print(line1+line2)