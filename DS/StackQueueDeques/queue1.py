class queue(object):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()



q = queue()

print(q.isEmpty())

q.enqueue(1)
q.enqueue("hello")
print(q.isEmpty())
print(q.size())

q.dequeue()
print(q.size())