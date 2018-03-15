'''
Find the contiguous subarray within an array (containing at least one number) that has the
largest sum.
For example, given the array [2, 1, –3, 4, –1, 2, 1, –5, 4],
The contiguous array [4, –1, 2, 1] has the largest sum = 6.
 Time:  O(n)
 Space: O(1)

'''


def maxSub(arr):
    maxEnd = arr[0]
    final_max= arr[0]
    for i in range(len(arr)):
        maxEnd = max(maxEnd+arr[i],arr[i])
        final_max = max(maxEnd,final_max)

    return final_max

print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))
