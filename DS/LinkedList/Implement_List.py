class Singly_LL(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

a = Singly_LL(1)
b = Singly_LL(2)
c = Singly_LL(3)


a.nextnode = b
b.nextnode = c


class Doubly_LL(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None
        self.previousnode = None

a = Doubly_LL(1)
b = Doubly_LL(2)
c = Doubly_LL(3)

a.nextnode = b
b.nextnode = c

c.previousnode = b
b.previousnode = a