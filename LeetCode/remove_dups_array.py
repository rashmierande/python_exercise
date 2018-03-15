# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
#

def removeDup(lst):
    if not lst:
        return 0

    last , i = 0, 1

    while i <len(lst):
        if lst[last] != lst[i]:
            last +=1
            lst[last] = lst[i]
        i +=1
    return last+1

print(removeDup([1, 1, 2]))