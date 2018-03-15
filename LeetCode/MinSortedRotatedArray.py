'''
. Find Minimum in Sorted Rotated Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array

'''


def findMin(arr):
    left = 0
    right = len(arr)-1
    while left < right and arr[left]>= arr[right]:
        mid = (left+right)//2
        if arr[mid]>arr[right]:
            left = mid+1
        else:
            right = mid

    return arr[left]

print(findMin([7,1,2,3,4]))


# Array with duplicates

def findMindups(arr):
    left = 0
    right = len(arr)-1

    while left < right and arr[left]>= arr[right]:
        mid = (left+right)//2
        if arr[mid]>arr[right]:
            left = mid +1
        elif arr[mid]<arr[left]:
            right = mid
        else:
            #IF arr[left]==arr[mid]==arr[right]
            left = left +1
    return arr[left]
print(findMin([7,8,2,3,2,4]))
