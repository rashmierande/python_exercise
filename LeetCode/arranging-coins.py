# Time:  O(logn)
# Space: O(1)

# You have a total of n coins that you want to form in a staircase shape,
# where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.


# Time:  O(logn)
# Space: O(1)

def arrangeCoins( n):
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        if 2 * n < mid * (mid+1):
            right = mid - 1
        else:
            left = mid + 1
    return left - 1

print(arrangeCoins(8))

