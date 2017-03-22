class deque(object):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def addFront(self,item):
        return self.items.insert(0,item)

    def addRear(self,item):
        return self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items ==[]

d =deque()
print(d.isEmpty())
print(d.size())
print(d.addFront("One"))
print(d.addFront("Two"))
print(d.addRear("Third"))
print(d.size())
print(d.removeRear())
print(d.removeFront())
print(d.size())