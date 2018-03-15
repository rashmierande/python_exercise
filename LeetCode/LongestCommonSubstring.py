def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)

    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer


print (longestSubstringFinder("apple pie available", "apple pies"))
print (longestSubstringFinder("apples", "appleses"))
print (longestSubstringFinder("bapples", "cappleses"))


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


# def long_substr(data):
#     substr = ''
#     if len(data) > 1 and len(data[0]) > 0:
#         for i in range(len(data[0])):
#             for j in range(len(data[0])-i+1):
#                 if j > len(substr) and all(data[0][i:i+j] in x for x in data):
#                     substr = data[0][i:i+j]
#     return substr

print (long_substr(['Oh, hello, my friend.',
                   'I prefer Jelly Belly beans.',
                   'When hell freezes over!']))