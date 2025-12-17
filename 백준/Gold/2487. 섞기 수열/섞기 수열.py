input()
l=0,*map(int,input().split())
v=[0]*len(l)
r=[]
for i in range(len(l)):
    if v[i]<1:
        c=0
        while v[i]<1:
            v[i]=1
            i=l[i]
            c+=1
        r+=c,
import math
print(math.lcm(*r))