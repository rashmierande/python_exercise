'''
Create a program asks the user to enter a new password
and check that the submitted password should contain
at least one number, one uppercase letter and at least 5 characters.
If the conditions are generated, print out "Password is fine",
otherwise keep prompting the user for a password.

'''

while True:
    pass_wd = input("Enter new password :")
    if any(i.isdigit() for i in pass_wd) and any(i.isupper() for i in pass_wd) and len(pass_wd)>=5:
        print("password is fine")
        break
    else:
        print("password is not fine")

#We're using a while  loop here because we need to keep the program running
# until the user submits a password that satisfies all three conditions.
# Line 3 contains the three conditions connected with an and  operator.
# Line 3 becomes True  only when all three conditions are True .
# If that happens, Password is fine  is generated, and the break statement
# will break the loop, and the program will stop. If at least one of the
# conditions in Line 3 is False , Line 3 evalueates to False  and the print
# statement under else is executed and the loop starts over again.
