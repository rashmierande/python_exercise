'''
Make script that prints out letter of english alphabet from a to z

'''

import string

for letter in string.ascii_lowercase:
    print(letter)


# string  is a built-in module and string.ascii_lowercase
# returns a string object containing all 26 letters of English alphabet.
# Then we simply iterate through that string and print out the string items.