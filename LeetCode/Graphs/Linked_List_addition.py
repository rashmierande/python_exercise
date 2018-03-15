# Time:  O(m + n)
# Space: O(m + n)

# You are given two linked lists representing two non-negative numbers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def add_LL(l1,l2):

     l1_sum=[]
     l2_sum = []
     while l1:
         l1_sum.append(l1.val)
         l1 = l1.next
     while l2:
         l2_sum.append(l2.val)
         l2 = l2.next

     prev, head = None,None
     sum = 0
     while l1_sum or l2_sum:
         sum //=10

         if l1_sum:
             sum += l1_sum.pop()
         if l2_sum:
             sum += l2_sum.pop()

         head = Node(sum % 10)
         head.next = prev
         prev = head

         if sum >=10:
             head = Node(sum//10)
             head.next = prev

         print(head.val)
     return head

l1 = Node(5)
l1_a = Node(3)
l2_b = Node(1)
l1.next = l1_a
l1_a.next = l2_b

l2 = Node(2)
l2_a = Node(2)
l2.next = l2_a

add_LL(l1,l2)