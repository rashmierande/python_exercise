'''
Add a new pair of key (e.g. c ) and
value (e.g. 3 ) to the dictionary and
print out the new dictionary.

d = {"a": 1, "b": 2}

{'a': 1, 'c': 3, 'b': 2}

'''

d = {"a": 1, "b": 2}

d["c"] = 3

print(d)

'''
Adding pairs of keys and values is straightforward
as you can see. Note though that you cannot fix
the order of the dictionary items.
Dictionaries are unordered collections of items.

'''

'''
Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}

'''

d = {"a": 1, "b": 2, "c": 3}

print(d.values())
print(sum(d.values()))


# d.values()  returns a list-like dict_values
# object while the sum  function calculates
# the sum of the dict_values  items.