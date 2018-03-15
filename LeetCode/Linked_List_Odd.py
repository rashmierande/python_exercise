class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def oddEvenList(head):

    if head is None:
        return None
    odd = head
    even = head.next
    evenHead = even
    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    LL_print(head)
    return head

def ispalindrome(head):
    reverse = None
    current = head
    # Reverse the first half part of the list.
    while current and current.next:
        current = current.next.next
        head.next, reverse, head = reverse, head, head.next

    # If the number of the nodes is odd,
    # set the head of the tail list to the next of the median node.
    tail = head.next if current else head

    # Compare the reversed first half list with the second half list.
    # And restore the reversed first half list.
    is_palindrome = True
    while reverse:
        is_palindrome = is_palindrome and reverse.val == tail.val
        reverse.next, head, reverse = head, reverse, reverse.next
        tail = tail.next

    return is_palindrome

#Has o(n2) time complexity
def remove_dups_unsorted_LL(head):
    pt1 = head
    pt2 =None
    dup = None

    while pt1 and pt1.next:
        pt2 = pt1

        while pt2.next:
            if pt1.val == pt2.next.val:
                print("removeing ", pt1.val)
                dup = pt2.next
                pt2.next = pt2.next.next
            else:
                pt2 = pt2.next
        pt1 = pt1.next
    LL_print(head)

def remove_dups_sorted_LL(head):
    current = head
    next = None

    if head is None:
        return

    while current.next:
        if current.data == current.next.data:
            next = current.next.next
            current.next = None
            current.next = next
        else:
            current = current.next

    return head


def LL_print(head):
    while head:
        print(head.val,end = " ")
        head = head.next

l1 = Node(1)
l1_a = Node(2)
l2_b = Node(3)
l3_c = Node(4)
l4_d = Node(1)

l1.next = l1_a
l1_a.next = l2_b
l2_b.next = l3_c
l3_c.next = l4_d

oddEvenList(l1)
print("\n")
print(ispalindrome(l1))
print("\n")
remove_dups_unsorted_LL(l1)

