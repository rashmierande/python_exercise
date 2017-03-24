'''
Please download the words1.txt file from the attachment
and then create a Python function that takes a text file as
input and returns the number of words contained in the text file.

Expected output:

10

'''

def word_cnt(file1):
    # f1 = open(file1).readlines()
    # print(f1)
    # words = str(f1).split()
    # print(len(words))
    with open(file1, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)



#print(word_cnt("/Users/Rashmi/PycharmProjects/python_exercise/python_workbook/words1.txt"))
print(word_cnt("words1.txt"))