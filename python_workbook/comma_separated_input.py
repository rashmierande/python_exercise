
lines = input("Enter input with comma separated :")

lines_lst = lines.replace(",","\n")

with open("user_data_comma.txt","a+") as f:
    for i in lines_lst:
        f.write(i)
