f1 = open("user_data_2.txt","a+")

lst=[]
while True:
    val = input("Enter val : ")
    if val == "SAVE" :
        f1.close()
        f1 = open("user_data_2.txt","a+")
    elif val == "CLOSE":
        f1.close()
        break
    else:
        f1.write(val +"\n")
