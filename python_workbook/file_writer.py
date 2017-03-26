lst1=[]
while True:
    lines = input("Enter value :")
    if "CLOSE" in lines:
        break
    else:
        lst1.append(lines)

#print(lst1)

with open("user_data_1.txt","a+") as f:
    for i in lst1:
        f.write(i + "\n")
