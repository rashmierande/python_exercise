def SecondMax(nums):
    first,second = 0,0

    for n in nums:
        if n > first:
            first,second = n,first
        elif n<first and n> second:
            second = n

    return second

print(SecondMax([3,1,5,7,4]))


