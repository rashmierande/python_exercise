months = ['Jan','March','April','May','Jun','Aug','Sept']

def substring(s):
    for i in months:
        if i.lower() in s.lower():
            return i

with open('months.txt','r') as f:
    for line in f:
        # print(line.strip('\n'))
       if substring(line.strip('\n')) is not None:
           print(substring(line.strip('\n')))

# How can you find the highest value in an array?

l = [1,4,5,10,12,15]
max = l[0]

for i in range(1,len(l)):
    if max < l[i]:
        max = l[i]
print(max)

# median

for i in range(len(l)-1,0,-1):
        for n in range(i):
            if l[n]>l[n+1]:
                temp = l[n]
                l[n]=l[n+1]
                l[n+1]=temp
print(l)
print("the median is ", l[len(l)//2])

# Aver
p = [6,11,7]
print(sum(p)//len(p))