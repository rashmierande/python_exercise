'''
Validate if a given string is numeric.
Some examples:
"0"  true
"0.1"  true
"abc"  false
'''

def isNumber(str):
    i = 0
    n = len(str)
    while i<n and str[i]=="":
        i +=1
    if i < n and str[i]=="+" or str[i]=='-':
        i +=1
    isNumeric = False
    while i < n :
        for c in str:
            if c =='.':
                i +=1
            if c.isdigit():
                i +=1
                isNumeric = True

    return isNumeric and i ==n


print(isNumber("1 2"))
print(isNumber("1.2"))
print(isNumber("-12"))
print(isNumber("1e2"))