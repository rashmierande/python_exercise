while True:
    user = input("Enter username :")
    with open("username.txt","r") as f1:
        users = f1.readlines()
        users = [i.strip("\n") for i in users]
        #print(users)
    if user in users:
        print("Username exists")
        continue
    else:
        print("Username is fine")
        break


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)