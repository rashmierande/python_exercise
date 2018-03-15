def permute(s):
    out = []
    if len(s) ==1:
        out = [s]
    else:
        #For every letter in string,
        for i , let in enumerate(s):
            #print(i,let)
            #for every permutaion resulting from step 2 and 3
            #print (s[:i]+s[i+1:] + "***")
            for perm in permute(s[:i]+s[i+1:]):
                #print("perm is ",perm)
                #print("Current let is", let)
                #print(s[:i]+s[i+1:])
                out +=[let+perm]
    return out


print(permute("abc"))
#print(permute("abc"))

print(permute("hello"))