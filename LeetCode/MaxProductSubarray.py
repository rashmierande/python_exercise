'''
Find the contiguous subarray within an array of integers that has the largest product. For
example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product
= 6.
Example Questions Candidate Might Ask:
Q: Could the subarray be empty?
A: No, the subarray must contain at least one number
Time:  O(n)
Space: O(1)

'''

def maxProduct(arr):

    global_max,local_max,local_min = float("-inf"),1,1
    for x in arr:
        local_max,local_min = max(x,local_max*x,local_min*x), min(x,local_max*x,local_min*x)
        global_max = max(global_max,local_max)
    return global_max

print(maxProduct([2, -2, -4]))
print(maxProduct([-4,-3]))