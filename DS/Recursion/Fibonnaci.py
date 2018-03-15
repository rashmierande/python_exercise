def fib(n):
    a = 0
    b = 1

    for i in range(n):
        #print(i , end= " ")
        a , b = b, a+b
        print (a, end=" ")
    return a

def fib_rec(n):

    if n <=1:
        return 1
    else:
        return fib_rec(n-1)+ fib_rec(n-2)

print(fib(5))

n =5
print("\n")
for i in range(n):
    print(fib_rec(i), end= " ")