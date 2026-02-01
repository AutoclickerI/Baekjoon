c=[float('inf'),0,0,0,0,0]
f=m=0
for i in map('quack'.find,input()):
    c[i]-=1
    c[i+1]+=1
    c[-1]=0
    if c[i]<0:
        f=-1
    m=max(m,sum(c[1:]))
if f or sum(c[1:]):
    print(-1)
else:
    print(m)