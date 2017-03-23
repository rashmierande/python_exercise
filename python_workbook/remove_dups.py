
'''
We used a set  function to convert the list to a set
 which would intermediately produce {'1', 1, 2}  with no
 duplicates because set objects cannot contain duplicates.
 Then using list  we converted the set back to a list.
 The drawback here is that the original order of the items is lost.
 If you need to preserve the order you may want to use the
 solution in Answer 2 below.

'''

#Answer1

a = ["1",1,"1",2]

print(list(set(a)))

#Answer2
'''
Ordered dictionaries are another data type in Python
that unlike sets and normal dictionaries they preserve
the order of the items. Here OrderedDict.fromkeys(a)
would produce an OrderedDict  like [('1', None), (1, None), (2, None)] .
Then we would convert that OrderedDict  to a list.
'''
from collections import OrderedDict

a = ["1",1,"1",2]

print(list(OrderedDict.fromkeys(a)))


#Answer3
'''

This is another solution that would preserve
the original order. We go through all items of
the original list and append them to the new list
 if they have not been appended before. The downside
of this is the operation can take a lot of time if the
list is large as we need to access both lists and also
perform a conditional in each iteration.
'''

a = ["1",1,"1",2]

b =[]

for i in a:
    if i not in b :
        b.append(i)
print(b)

