def num_find (arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 !=num2:
            return num1
    return arr1[-1]

def finder(arr1,arr2):

    if len(arr1) < len(arr2):
        return num_find(arr2,arr1)
    else:
        return num_find(arr1,arr2)




print(finder([1,4,5,7],[4,5,1]))