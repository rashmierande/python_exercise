checklist = ["Portugal","Germany","Spain"]
checklist = [i+"\n" for i in checklist]

with open("countries-missing.txt","r") as f1:
    content = f1.readlines()

up_list = sorted(checklist + content)

with open("countries-missing-fixed.txt","w") as f1:
    for i in up_list:
        f1.write(i)