'''
Create a function that calculates acceleration given initial velocity v1,
final velocity v2, start time t1, and end time t2.
The formula is :-
a = (v2 - v1) / (t2 - t1) .

To test your solution, call the function by inputting
values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively,
and you should get the expected output.

Expected output:

0.5

'''

def acc_cal(v1,v2,t1,t2):
    a = (v2-v1)/(t2-t1)
    print (a)

acc_cal(0,10,0,20)


'''
Answer (Python 2):

def acceleration(v1, v2, t1, t2):
    a = float(v2 - v1) / float(t2 - t1)
    return a

print(acceleration(0,10,0,20))

If you were creating this in Python 2 the solution would
need to have two float  functions converting the two differences
to float numbers because if the differences are integers,
Python will also output an integer (e.g. 3 / 2 outputs 0).
In Python 3 you don't have to convert to floats.


'''