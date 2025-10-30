s=[input()for _ in[0]*5]

from itertools import*

a=0
for v in combinations(range(25),7):
    l=[(i//5,i%5)for i in v]
    v=[0]*7
    chk=[0]
    v[0]=1
    for i in chk: 
        y,x=l[i]
        for n in range(7):
            ny,nx=l[n]
            if abs(ny-y)+abs(nx-x)==1 and v[n]<1:
                v[n]=1
                chk+=n,
    if all(v) and 3<sum(s[y][x]=='S'for y,x in l):
        a+=1
print(a)