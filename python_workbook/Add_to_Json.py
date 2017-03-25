'''
Please download the json file in the attachment and use Python to add a new employee to
the content of the file so that the file looks like in the expected output below.
'''

import json

with open("company1.json","r+") as f1:
     d= json.loads(f1.read())
     d["employees"].append(dict(firstName="Albert",lastName="Bert"))
     f1.seek(0)   #puts the curser at the top of file
     json.dump(d,f1,indent=4,sort_keys=True)  #review sort_key
     f1.truncate() # truncate everything under curser