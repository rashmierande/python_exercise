'''
Create a script that generates a file where all letters of
English alphabet are listed two in each line.
The inside of the text file would look like:

ab
cd
ef

and so on.
'''

import string

with open("txt4.txt","w") as f:
    for let1,let2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        f.write(let1+let2+"\n")
