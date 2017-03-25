'''

write a script that iterates through each of 26 text files,
check if the letter inside the text file is in string "python"
and puts the letter in a list if letter is a character of "python"

'''

import glob

file_list=glob.glob("letters/*.txt")
letter =[]
check ="python"

for i in file_list:
    with open(i,"r") as f1:
        str1 = f1.read().strip("\n")
        if str1 in check:
            letter.append(str1)

print(letter)

