# Time:  O(n)
# Space: O(1)

# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and
# there will not be any extra space in the string.

def reverseStr(sen):
    for i in sen.split():
        print(i[::-1],end = " ")


def reverseStr1(sen):

    def rev(sen,begin,end):
        for i in range((end-begin)//2):
            sen[begin+i],sen[end-1-i] = sen[end-1-i], sen[begin+i]

    sen = list(sen)
    i =0
    for j in range(len(sen)+1):
        if j == len(sen) or sen[j]==' ':
            rev(sen,i,j)
            i = j + 1
    return "".join(sen)


print(reverseStr1("Let's take LeetCode contest"))
reverseStr("Let's take LeetCode contest")