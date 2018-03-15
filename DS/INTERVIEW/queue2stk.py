# class Stack(object):
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop() # THIS IS LINE 12
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
# class Queue2Stacks(object):

#     def __init__(self):
#         self.instack =  Stack()
#         self.outstack = Stack()
#
#     def enqueue(self, item):
#         self.instack.push(item)
#
#     def dequeue(self):
#         if  self.outstack:
#             while  self.instack.size():
#                 self.outstack.push(self.instack.pop())
#
#         return self.outstack.pop() # THIS IS LINE 33
#
# q2s = Queue2Stacks()
# q2s.enqueue(1)
# q2s.enqueue(2)
# q2s.enqueue(3)
#
# #q2s.dequeue()
#
#
# for i in range(3):
#      print('Returning : ', q2s.dequeue())  # THIS IS LINE 41

# import datetime
# from datetime import timedelta
#
# d1 = datetime.date(2015,5,4)
# d2 = datetime.date(2017,5,4)
# d3 = timedelta(days=365)
# print(d1)
# print(d2)
#
# print((d2-d1))



# import timeit
#
# #For Loop
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
#
# # List comprehension
# print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
#
# # Map()
# print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
#

s = "Hello world"
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isdecimal())
print(s.isdigit())
print(s.isspace())
print(s.istitle())
print(s.upper())
print(s.endswith('d'))

print(s.split('o'))
print(s.split(' '))

print(s.partition('e'))

