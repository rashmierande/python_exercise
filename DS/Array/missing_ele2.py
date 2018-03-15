import collections

def finder(arr1,arr2):

    result=0
    print(arr1 + arr2)
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        print(num,result, bin(num),bin(result))
        result^=num
        print (result)
        print(bin(result))

    return result


print(finder([1,2],[4,1,2]))


0b1
0b0
==
0b1
