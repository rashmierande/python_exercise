import os
import datetime

print(os.getcwd())

dir1 = os.getcwd()

print(os.listdir(dir1))

print(os.stat('date_excersize1.py'))
print(os.stat('date_excersize1.py').st_size)
print(datetime.datetime.fromtimestamp(os.stat('date_excersize1.py').st_mtime))

for dirpath,dirname,filename in os.walk(os.getcwd()):
    print("val is ",dirpath, dirname, filename)

print(os.environ)
print(os.environ.get('HOME'))

#os.path.join creates proper path with /
print(os.path.join(os.environ.get('HOME'),"text1.txt"))
#os.path.basename :- gives filename , os.path.dirname :- gives dir name
# and os.path.split :- gives both filename and dir name in a tuple

print(os.path.basename(os.path.join(os.environ.get('HOME'),"text1.txt")))
print(os.path.dirname(os.path.join(os.environ.get('HOME'),"text1.txt")))
print(os.path.split(os.path.join(os.environ.get('HOME'),"text1.txt")))

#os.path.exists :- checks if file exists , os.path.splitext :- splits extension and file
print(os.path.exists(os.path.join(os.environ.get('HOME'),"text1.txt")))
print(os.path.splitext("/tmp/text1.txt"))
print(os.path.isdir("/tmp/text1.txt"))


li = [-6,-5,-4,1,2,3]

sort_li = sorted(li,key=abs)
print(sort_li)

# makedir
# makedirs
# rmdir
# removedirs
# rname
