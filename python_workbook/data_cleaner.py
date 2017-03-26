'''
 Please download the attached countries_raw.txt file.
 The file contains the list of country names, but it also
 contains some unnecessary text among the countries.

Please clean the list with Python by generating a new text
 file that contains a flawless list of country names without any
 other text or break lines in it. The new file content should look
 like in the expected output.

'''

with open("countries-raw.txt","r") as f:
    lst1 = f.readlines()
lst1 = [i.strip("\n") for i in lst1 if "\n" in i]
lst1 = [i for i in lst1 if i!=""]
lst1 = [i for i in lst1 if len(i)!=1]

print(lst1)

with open("countries-clean.txt","w") as f:
    for i in lst1:
        f.write(i + "\n")

