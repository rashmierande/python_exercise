'''
write a script that extracts letters from 26 text files and
put letters in a list

'''

import glob

letters = []
file_list = glob.glob("letters/*.txt") #In letters folder, all files, *.txt

for filename in file_list:
    with open(filename,"r") as f1:
        letters.append(f1.read().strip("\n"))

print(letters)