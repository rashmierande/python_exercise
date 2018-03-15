a =[1,2,3,4,5,7,8,9,10]

print(sum(range(a[0],a[-1]+1))-sum(a))

print(a[-1]*(a[-1]+a[0])/2 -sum(a))


# a = [1,2,3,4,7,8,10]
# from itertools import imap, chain
# from operator import sub
# print (list(chain.from_iterable((a[i] + d for d in range(1,diff))
#                                 for i, diff in enumerate(imap(sub,a[1:],a))
#                                 if diff >1 )))
#
#


# from itertools import count, izip
#
# a=[1,2,3,4,5,7,8,9,10]
# nums = (b for a, b in izip(a, count(a[0])) if a != b)
# next(nums, None)


a=[1,2,3,4,5,7,8,10]
print([(e1+1) for e1,e2 in zip(a, a[1:]) if e2-e1 != 1])
