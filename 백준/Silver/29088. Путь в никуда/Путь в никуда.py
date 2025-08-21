n,m,x,y=map(int,open(0).read().split())
c=1
i=0
while 1:
    i+=1
    if x+i<=n:
        x+=i
        c+=i
    else:
        c+=n-x
        break
    if 0<y-i:
        y-=i
        c+=i
    else:
        c+=y-1
        break
    i+=1
    if 0<x-i:
        x-=i
        c+=i
    else:
        c+=x-1
        break
    if y+i<=m:
        y+=i
        c+=i
    else:
        c+=m-y
        break
print(c)