import collections

def finder(lst1,lst2): #O(Nlog(N))
    lst1.sort()
    lst2.sort()

    for num1,num2 in zip(lst1,lst2):
        if num1!= num2:
            return num1

    return lst1[-1]


def finder3(arr1, arr2):
    result=0

    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2:  #arr1 + arr2 is just concatnation
        result^=num
        print (num,result)

    return result

def finder2(lst1,lst2):

    # Using default dict to avoid key errors
    d = collections.defaultdict(int)
    for num in lst2:
        d[num] += 1

    for num in lst1:
        if d[num] ==0:
            return num
        else:
            d[num] -=1


# print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder([5,5,7,7],[5,5,7]))
#
# print(finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6]))

print(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
print(finder2([5,5,7,7],[5,5,7]))