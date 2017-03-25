'''
Please complete the code so that it prints out the expected output.


Expected output:

Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
'''

a = [1, 2, 3]

for index,item in enumerate(a):
    print("Item %s has index %s "%(item,index))

# enumerate(a)  creates an enumerate object which yields
#  pairs of indexes and items. Then we iterate through that
#  object print out the item-index pairs in each iteration
# together with some other strings.