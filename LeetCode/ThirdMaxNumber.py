# Time:  O(n)
# Space: O(1)

# Given an array of integers, return the 3rd Maximum Number in this array,
# if it doesn't exist, return the Maximum Number.
# The time complexity must be O(n) or less.

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    top = [float("-inf")] * 3
    for num in nums:
        if num > top[0]:
            top[0], top[1], top[2] = num, top[0], top[1]
            count += 1
        elif num != top[0] and num > top[1]:
            top[1], top[2] = num, top[1]
            count += 1
        elif num != top[0] and num != top[1] and num >= top[2]:
            top[2] = num
            count += 1

    if count < 3:
        return top[0]

    return top[2]

print(thirdMax([7,4,2,1,5]))

#My Solution
def topmax(nums):
    first, second,third  = 0,0,0
    for n in nums:
        if n > first:
            first, second,third = n, first,second
        elif n != first and n > second:
            second,third = n, second
        elif n != first and n != second and n >= third:
            third = n

    return third

print(topmax([7,4,2,1,5]))

