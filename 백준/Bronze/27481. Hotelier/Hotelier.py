p,q=open(0)
l=[0]*10
for i in q[:-1]:
    match i:
        case'L':l[l.index(0)]=1
        case'R':
            n=9
            while l[n]:n-=1
            l[n]=1
        case _:l[int(i)]=0
print(*l,sep='')