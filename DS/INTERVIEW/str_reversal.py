def str_reversal(s):

    if len(s)==1:
        return s
    else:
        return str_reversal(s[1:]) + s[0]


print(str_reversal("hello world"))


