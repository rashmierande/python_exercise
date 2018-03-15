#
# from IPython.display import clear_output
#
# #
# # print("asdadad")
# # clear_output()
#
# class Line(object):
#
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#
#         return  ( (x2-x1)**2 + (y2-y1)**2 )**0.5
#
#
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return float((y2-y1))/(x2-x1)
#
# l = Line((3,2),(8,10))
# print(l.distance())
# print(l.slope())
#
# class Cylinder(object):
#     pi = 3.14
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
#
#
#     def volume(self):
#         # V = pi * h * r**2
#         return Cylinder.pi * self.height * (self.radius **2)
#
#     def surface_area(self):
#         #A = (2 * pi * r *h) + (2 *pi*)*(r**2)
#         return  (2 * Cylinder.pi * self.radius * self.height)+ (2 * Cylinder.pi)*(self.radius**2)
#
# c = Cylinder(2,3)
# print(c.volume())
# print(c.surface_area())
#
#
# try:
#     for i in['a','b','c']:
#         print (i **2)
# except TypeError:
#     print("errror occured")
#
#
# x = 5
# y = 0
#
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Division by zero")
# finally:
#     print("All Done")

print("****"*10)

# def ask():
#
#     while True:
#         try:
#             s = input("Enter an integer : ")
#         except:
#             print("Error Occured")
#             continue
#         else:
#             print("In else")
#             break
#         # finally:
#         #     print("Finally executed")
#     sq = int(s)
#     print(sq **2)
#
#
#
# ask()
#
#
# try:
#     # f = open("xyz","r")
#     # f.write("hello")
#     print("in try")
# except:
#     print("error")
# else:
#     print("in else")
# finally:
#     print("in finally")

#
# def ask():
#
#     while True:
#         try:
#             n = input('Input an integer: ')
#         except:
#             print ('An error occurred! Please try again!')
#             continue
#         else:
#             break
#
#
#     print ('Thank you, you number squared is: ',int(n)**2)
#
# ask()

# from functools import reduce
#
# lst = [1,4,5,7]
# lst1 = [2,3,4,5]
#
# print(reduce(lambda x,y:x+y,lst1))
#
#
# print(list(map(lambda pair:max(pair), zip(lst,lst1))))


# l = [True,False,False]
# b =[False,False]
#
# c = [True,True]
#
# print("*"*30)
# print(all(c))
# print(any(c))
#
#
# print(all(b))
# print(any(b))
#
# print("****"*10)
#
# print(all(l))
#
# print(any(l))

def word_len(phrase):
    return list(map(len,phrase.split()))


print(word_len("Hello world"))

from functools import reduce

def digits_to_num(digits):
    return reduce(lambda x,y:x*10 + y ,digits)

print(digits_to_num([3,2,5,6]))


def filter_words(word_lst,letter):
   return filter(lambda word:  word[0]==letter,word_lst)

l = ['hello','hi','bye','good']
print(list(filter_words(l,'h')))


def concat(l1,l2,connector):
    return [word1+connector+word2 for(word1,word2) in zip(l1,l2)]

l1 = ['A','B']
l2 = ['a','b']

print(list(concat(l1,l2,"-")))