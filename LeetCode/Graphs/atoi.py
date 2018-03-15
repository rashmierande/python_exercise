# def demo_atoi(astr):
#     num = 0
#     for c in astr:
#         if '0' <= c <= '9':
#             num  = num * 10 + ord(c) - ord('0')
#         else:
#             raise ValueError('demo_atoi argument (%s) contains
# non-digit(s)' % astr)
#     return num



# Python program for implementation of atoi

# A simple atoi() function
def myAtoi(string):
    res = 0

    # Iterate through all characters of input string and
    # update result
    for i in range(len(string)):
        res = res*10 + (ord(string[i]) - ord('0'))

    return res

# Driver program
string = "89789"
print (myAtoi(string))
