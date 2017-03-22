from nose.tools import assert_equal

class AnagramTest(object):
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print ("ALL TEST CASES PASSED")


def anagram(s1,s2):
    # lst1 = s1.replace(' ','').lower()
    # lst2 = s2.replace(' ','').lower()
    # print(s1.strip().lower())
    # print(s2.strip().lower())
    # print(lst1,lst2)
    #return sorted(lst1) == sorted(lst2)
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1)!= len(s2):
        return False

    count ={}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


# print(anagram('dog','god'))
# print(anagram('aa','ab'))
# print(anagram('clint eastwood','old west action'))

t = AnagramTest()
t.test(anagram)