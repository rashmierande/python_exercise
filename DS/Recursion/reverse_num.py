def rev_number(num):

    rev = 0

    while num > 0:
        rev = (10*rev) + num %10
        num //=10
    return rev

print(rev_number(123))



def rev_num2(num):
  return int(str(num)[::-1])

print(rev_num2(123))

def palindrome(num):
    return str(num) == str(num)[::-1]