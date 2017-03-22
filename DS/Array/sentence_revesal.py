'''
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

'''
from nose.tools import assert_equal

def rev_sentence(sen):
    return " ".join(reversed(sen.split()))

print(rev_sentence('Hi John,   are you ready to go?'))


def rev_sentence1(sen):
    return " ".join(sen.split()[::-1])

def rev_sentence2(sen):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(sen)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:
        # If element isn't a space
        if sen[i] not in spaces:
            # The word starts at this index
            word_start = i
            while i <length and sen[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(sen[word_start:i])
        # Add to index
        i +=1

    # Join the reversed words
    return  " ".join(reversed(words))
    


print(rev_sentence2('  Hi John,   are you ready     to go?    '))
print(rev_sentence1('Hi John,   are you ready to go?'))

class ReversalTest(object):

    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")

# Run and test
t = ReversalTest()
t.test(rev_sentence2)