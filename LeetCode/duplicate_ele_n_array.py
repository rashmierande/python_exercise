'''
Find out duplicate number between 1 to N numbers.
'''

def findDuplicateNumber(numbers):

    highestNumber = len(numbers) - 1
    total = getSum(numbers)
    # print(highestNumber*(highestNumber+1)/2)
    duplicate = total - (highestNumber*(highestNumber+1)//2)
    return duplicate


def getSum(numbers):

    sum = 0
    for num in numbers:
        sum += num

    return sum


print(findDuplicateNumber([1,2,3,1,5]))


def printRepeating(arr, size):

    print("The repeating elements are : ")

    for i in range(0,size):
        # print(arr[abs(arr[i])], " ", abs(arr[i]), " ", i )
        if(arr[abs(arr[i])] > 0):
            arr[abs(arr[i])] = -arr[abs(arr[i])]
            # print(arr[abs(arr[i])])
        else:
            print(abs(arr[i]) , end = " ")


lst = [1,2,3,1,5,2]
print(printRepeating(lst,len(lst)))

def finddups(lst):
    cnt = {}
    for num in lst:
        if num in cnt:
            cnt[num] +=1
        else:
            cnt[num] =1

    for i,k in cnt.items():
        if k >1:
            print(i,k)

finddups([1,2,3,1,5,2])

# My sol
def finddup1(lst):
    lst = sorted(lst)
    for i in range(1,len(lst)):
        if lst[i]==lst[i-1]:
            print("dup ", lst[i],end =" ")

finddup1([1,2,3,1,5,2])
# finddup1([ 1, 5, 23,5,23, 2, 1, 6, 3, 1, 8, 12, 3, 23])
