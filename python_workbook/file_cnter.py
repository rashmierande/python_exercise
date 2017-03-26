import glob

lst1 = glob.glob("files/*.txt")
#file_list=glob.glob1("files","*.py")

print(len(lst1))

#We're using glob  which is a standard Python library that finds
# pathnames matching
# a specified pattern. From glob  we're using glob1  which
# takes a directory name as first argument and a pattern which in
# our case is *.py  which returns all the files starting with whatever
# and ending with .py in the files  directory.