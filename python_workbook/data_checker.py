'''
Please take a look at the following list:


One of the items is not a country. Please use Python and
 the file containing the list of countries (attached) as data
  source to filter out the checklist  of non-country items.
  Once you have filtered out checklist , then print it out.

Expected output:

['Germany', 'Portugal', 'Spain']
'''

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries-clean.txt","r") as f1:
    lst1 = f1.readlines()

lst1 = [i.rstrip('\n') for i in lst1]
checked =[i for i in checklist if i in lst1]
print(checked)
