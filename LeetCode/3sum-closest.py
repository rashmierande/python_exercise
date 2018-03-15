# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threeSumClosest(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
    """
    nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
    # nums, result, min_diff, i = sorted(nums), 0,0, 0

    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i - 1]:
            j, k = i + 1, len(nums) - 1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                # print(nums[i] , nums[j] , nums[k] , target)
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    j += 1
                elif diff > 0:
                    k -= 1
                else:
                    return target
        i += 1
    return result

print(threeSumClosest([-1, 2, 1, -4], 1))


# @return an integer
def threeSumClosest1(num, target):
    num.sort()
    error = float("infinity")
    if len(num)<3:
        return 0
    for i in range(0, len(num)-2):
        begin = i+1
        end = len(num)-1
        while begin<end:
            if abs(num[i]+num[begin]+num[end]-target) < error:
                error = abs(num[i]+num[begin]+num[end]-target)
                solution = num[i]+num[begin]+num[end]
            if num[i]+num[begin]+num[end] > target:
                end -= 1
            else:
                begin += 1
    return solution

print(threeSumClosest1([-1, 2, 1, -4], 1))

