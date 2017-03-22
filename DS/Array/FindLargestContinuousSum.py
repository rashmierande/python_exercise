#Given an array of integers (positive and negative) find the largest continuous sum.
from nose.tools import assert_equal

def large_cont_sum(arr):
    #return sum(arr) # It will only work if all the elements are positive

    if len(arr) ==0:
        return 0

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num , num)
        max_sum = max(current_sum,max_sum)

    return max_sum


#print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))


class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')

#Run Test
t = LargeContTest()
t.test(large_cont_sum)