'''
Create a script that asks the user to enter
their age and the script calculates the user's year of
birth and prints it out in a string like in the expected output.
Please make sure you generate the current year dynamically.

Expected output:

You were born back in 1988
'''

from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("You were born back in %s" % year_birth)

#We're getting user input and we are converting it
# to an integer since input  loads everything as a string.
# Then we produce the current year dynamically
# with datetime.now().year  and we subtract the age from
# that to find out the year of birth. Lasty, in line 5,
# we use string formatting to produce a string with
# the year inside it.