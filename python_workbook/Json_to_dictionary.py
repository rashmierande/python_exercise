'''
Please download the file in the attachment and use Python to print out its content.

Expected output:

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
'''

import json
from pprint import pprint

with open("company1.json","r") as f1:
    d= json.loads(f1.read())


pprint(d)

# We're opening the file in read mode and then using json.loads
#  which gets a string as input and creates a dictionary object out of that.