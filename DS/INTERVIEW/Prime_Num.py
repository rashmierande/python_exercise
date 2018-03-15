import math

def prime(num):

    if num % 2 == 0 and num >2 :
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i ==0:
            return False
    return True


print(prime(3))
print(prime(9))
print(prime(19))
print(prime(15))
print(prime(1))


