import glob

lst = glob.glob("subdirs/**/*.py",recursive=True)

print(len(lst))

# We're using glob.glob  in contrast to glob.glob1 ,
# gets a pathname pattern and a recursive  argument which
#  indicates whether you want to search sub-directories or not.