# Time:  O(n^2)
# Space: O(n * d)

# A sequence of numbers is called arithmetic if it consists of at least three elements
# and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequences:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
# A zero-indexed array A consisting of N numbers is given.
# A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk)
# such that 0 ≤ P0 < P1 < ... < Pk < N.
#
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic
# if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k >= 2.
#
# The function should return the number of arithmetic subsequence slices in the array A.
#
# The input contains N integers. Every integer is in the range of -2^31 and 2^31-1 and 0 <= N <= 1000.
# The output is guaranteed to be less than 2^31-1.
#
#
# Example:
#
# Input: [2, 4, 6, 8, 10]
#
# Output: 7
#
# Explanation:
# All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
import collections

# Use this solution
def numberOfArithmeticSlices(A):

    result = 0
    dp = [collections.defaultdict(int) for i in range(len(A))]
    for i in range(1, len(A)):
        for j in range(i):
            diff = A[i]-A[j]
            dp[i][diff] += 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                result += dp[j][diff]
    return result

print(numberOfArithmeticSlices([2, 4, 6, 8, 10]))

# print(numberOfArithmeticSlices([2, 5, 6, 9, 12]))


def numberOfArithmeticSlices1( A):
    """
        :type A: List[int]
        :rtype: int
    """
    res, i = 0, 0
    while i+2 < len(A):
        start = i
        while i+2 < len(A) and A[i+2] + A[i] == 2*A[i+1]:
            res += i - start + 1
            i += 1
        i += 1

    return res

print(numberOfArithmeticSlices1([2, 4, 6, 8, 10]))
print(numberOfArithmeticSlices1([1, 2, 3, 4]))