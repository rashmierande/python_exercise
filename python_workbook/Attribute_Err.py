'''
The script is supposed to output the cosine of angle 1 radian,
 but instead it is throwing an error. Please fix the code so that
  it prints out the expected output.


Expected output:

0.5403023058681397
'''

import math
from math import cos
#print(math.cosine(1))
print(math.cos(1))
print(dir(math))
#AttributeError: module 'math' has no attribute 'cosine'
#You could get a list of all available methods of the math module
# with dir(math) and see whether cosine is there or not.