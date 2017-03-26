'''
Count the number of "a" characters in this text
 file: http://www.pythonhow.com/data/universe.txt

Expected output:

47
'''

import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")

lst1 = r.text

a = lst1.count("a")
print(a)
