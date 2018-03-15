'''
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

'''

def searchInsert(arr,target):
    left = 0
    right = len(arr)-1

    while left < right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        else:
            if target < arr[mid]:
                right = mid
            else:
                left = mid+1

    if arr[left]<target:
         return left+1
    else:
         return left


arr= [1,3,5,6]
print(searchInsert(arr,5))
print(searchInsert([1,3,5,6],7))
print(searchInsert([1,3,5,6],0))
print(searchInsert([1,3,5,6,8],7))
print(searchInsert([1,3,5,6],7))
