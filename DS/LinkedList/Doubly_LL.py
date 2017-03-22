class DoblyLL(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoblyLL(1)
b= DoblyLL(2)
c = DoblyLL(3)
d =DoblyLL(4)

a.next_node = b
b.next_node = c
c.next_node = d

b.prev_node = a
c.prev_node = a
d.prev_node = c

