'''
Please concatenate this file with this one to a single text file.
The content of the output file should look like below.
Expected output:

x,y
3,5
4,9
6,10
7,11
8,12
6,10
8,18
12,20
14,22
16,24

'''


import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data1 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

data2 = pandas.concat([data,data1]).to_csv("sampledata_new.txt",index=None)

