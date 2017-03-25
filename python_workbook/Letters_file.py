'''
Create a script that generates a text file with
all letters of English alphabet inside it, one letter per line.
'''
import string

def f1():
    with open("txt3.txt",'w') as f:
        for i in string.ascii_lowercase:
            f.write(i+"\n")


f1()