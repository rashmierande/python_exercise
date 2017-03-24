#The following script throws a NameError  in the last
# line saying that c  is not defined. Please fix the function
# so that there is no error and the last line is able to print
# out the value of c  (i.e. 1 ).

#c = 1
def foo():
    #c = 1
    global c
    c = 1
    return c
foo()
#print(c)
#NameError: name 'c' is not defined
#print(foo())
print(c)