input()
c=0
a=0
for i in input():
    if i=='1':c=3
    a+=c>0
    c-=1
print(a)