from nose.tools import assert_equal

def pair_sum(arr,sum):

    if len(arr)<2:
        return

    seen = set()
    output = set()

    for i in arr:
        target = sum-i

        if target not in seen:
            seen.add(i)
            #print ("target ",i)
        else:
            output.add((min(i,target),max(i,target)))
            print(min(i,target),max(i,target))

    #print('\n'.join(map(str,list(output)))  )
    print ("output is " ,output)
    return len(output)


class TestPair(object):

    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print ('ALL TEST CASES PASSED')

#Run tests
# t = TestPair()
# t.test(pair_sum)


print(pair_sum([1,2,3,2,4,0],4))


