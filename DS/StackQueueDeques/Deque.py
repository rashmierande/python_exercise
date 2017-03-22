
'''
1. Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
2. addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
3. addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
4. removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
5. removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
6. isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
7. size() returns the number of items in the deque. It needs no parameters and returns an integer.

'''

class Deque(object):
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


d = Deque()
print(d.isEmpty())
print(d.addFront(1))

print(d.isEmpty())
d.addRear(2)
d.addRear(3)
d.addFront(5)
print(d.size())
print(d.removeFront())
print(d.removeRear())
print(d.isEmpty())

