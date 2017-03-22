'''
Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and
return the new head of the list.

'''

class Node(object):

    def __init__(self,value):

        self.value = value
        self.next = None


def reverse_iter(head):

    # Set up current , previous and next nodes
    current = head
    previous = None
    next = None

    # until we have gone through to the end of list

    while current:

        # Make sure to copy current node's next to a variable next_node
        # before overwriting as the previous node for reversal
        next = current.nextnode
        #print("next_node",next_node.value)

        # Reverse pointer to the new next_node
        current.next = previous


        # Go one forward in the list
        previous = current
        #print("Previous ", previous.value)
        current = next
        #print("current ",current.value)

    return  previous

def reverse_recursive(head):
    if not head:
        return None

    if not head.next:
        return head
    else:
        new_head = reverse_recursive(head.next)

    head.next.next  = head
    #head.next = None

    return head



# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next = b
b.next = c
c.next = d

print (a.next.value , " -> ",b.next.value , " -> ", c.next.value )

#reverse_iter(a)
reverse_recursive(a)
print (d.next.value , ' -> ',c.next.value , ' -> ',b.next.value )