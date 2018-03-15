# Time:  O(n)
# Space: O(1)
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

def climbStairs(n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current

print(climbStairs(5))

# Time:  O(2^n)
# Space: O(n)
def climbStairs1( n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n - 1) + climbStairs(n - 2)



print(climbStairs1(5))
