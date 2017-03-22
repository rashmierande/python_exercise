
class stack(object):
    def __init__(self):
        self.items =[]

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        #return self.items[-1]
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

s = stack()

print(s.isEmpty())

s.push(1)

print(s.isEmpty())
print(s.size())
s.push(2)
s.push('Hello')
print(s.peek())
print(s.pop())
print(s.isEmpty())

