'''Write a Python program to read a file line by line and store it into a list.'''


def file_read(fname):
        with open(fname) as f:                    
                list = f.readlines()             
                print(list)
               
file_read('lab3/test.txt')
