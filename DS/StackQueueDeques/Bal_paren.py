'''
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [],
and curly brackets: {}. Assume that the string doesn’t contain any other character than these,
no spaces words or numbers. As a reminder, balanced parentheses require every opening
parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced
but ‘([)]’ is not.
'''
from nose.tools import assert_equal

def balance_check(s):

    # Check if even number of brackets
    if len(s)%2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    matches = set([('(',')'),('{','}'),('[',']')])

    # Use a list as a "stack"
    stack = []
    #print(s)
    # Check every paren in string
    for paren in s:
        #print(paren)
        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)
        else :

            # Check that there are paren in stack
            if len(stack) == 0:
                return False
            # Check the last open paren
            last_open = stack.pop()
            #print("last open ", last_open)

            #print(last_open,paren)
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False

    return len(stack) == 0


# class TestBalanceCheck(object):
#     def test(self,sol):
#         assert_equal(sol('[](){[[[]]]}('),False)
#         assert_equal(sol('[{{{(())}}}]((()))'),True)
#         assert_equal(sol('[[[]])]'),False)
#         print ('ALL TEST CASES PASSED')
#
# t = TestBalanceCheck()
# t.test(balance_check)

#print(balance_check('[]'))
#print(balance_check('[](){([[]])}'))
print(balance_check('[{()}]'))
#print(balance_check('()(){]}'))
#print(balance_check(''))
#print(balance_check('sfsd'))