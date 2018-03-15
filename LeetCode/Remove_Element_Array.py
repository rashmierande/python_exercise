'''
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        for i in range(len(A)-1,-1,-1):
            if A[i]==elem:
                length -= 1
                self.swap(A, i, length)
        # print(A)
        return length

    def swap(self, A, pos1, pos2):
        temp = A[pos1]
        A[pos1] = A[pos2]
        A[pos2] = temp


sol = Solution()
print(sol.removeElement([1,2,3,1,5,1,7],1))

