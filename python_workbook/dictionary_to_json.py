'''
Store the dictionary in a json file.

'''
import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company.json","w") as f1:
    json.dump(d,f1,indent=4,sort_keys=True)

#As you can see we created the json file using the standard file
#  handling method, but then we used json.dump  which makes it easy
# to write the dictionary content to the file. indent=4  will create 4 white spaces
#  to indent the different levels of the dictionary items and sort_keys=True
# tells Python to preserve the order of the dictionary thrown in the file.