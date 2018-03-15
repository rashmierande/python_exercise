'''
Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.
 push(x) – Push element x onto stack.
 pop() – Removes the element on top of the stack.
 top() – Get the top element.
 getMin() – Retrieve the minimum element in the stack.
'''

class Stack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val):
        self.stack.append(val)
        if len(self.minStack)==0 or val <= self.minStack[len(self.minStack)-1]:
            self.minStack.append(val)

    def pop(self):
        if self.stack.pop() == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def getMin(self):
        return self.minStack[len(self.minStack)-1]


s =  Stack()
s.push(4)
s.push(2)
s.push(5)
s.push(1)


print(s.getMin())
print(s.top())
print(s.pop())
print(s.getMin())
print(s.pop())
print(s.getMin())
print(s.pop())
print(s.getMin())
