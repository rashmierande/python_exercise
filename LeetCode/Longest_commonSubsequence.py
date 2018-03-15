#  http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

str1 = "ABCDGHLQR"
str2 = "AEDPHR"

result = lcs(str1, str2)
print("result ",result)


# Recursion :- This solution is similar to the Haskell one. It is slow.
def lcs1(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs1(xs, ys)
    else:
        return max(lcs1(xstr, ys), lcs1(xs, ystr), key=len)

print(lcs1("ABCDGHLQR","AEDPHR"))