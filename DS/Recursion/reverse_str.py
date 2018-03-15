def reverse_str(s):
    if len(s) <=1:
        return s
    else:
        return reverse_str(s[1:])+ s[0]

print(reverse_str("hello world"))
print(reverse_str("hello"))
print(reverse_str("hello world you are welcom"))
print(reverse_str("h"))
print(reverse_str("he"))


