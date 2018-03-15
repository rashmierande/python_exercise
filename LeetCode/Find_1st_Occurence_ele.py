'''
Given a sorted array of integers, find index of first or last occurrence of a given number. If the element is not found in the array, report that as well.


For example,

Input:
arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 5

Output:
First occurrence of element 5 is found at index 1
Last occurrence of element 5 is found at index 3


Input:
arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 4

Output:
Element not found in the array
'''

def findEle(lst,ele):
    first_occurence, last_occurence = -1,-1
    for pos,i in enumerate(lst):
        if i ==ele and first_occurence == -1:
            first_occurence = pos
        if first_occurence != -1 and i ==ele:
            last_occurence = pos

    return first_occurence, last_occurence

print(findEle([1,3,2,2,2,3],3))