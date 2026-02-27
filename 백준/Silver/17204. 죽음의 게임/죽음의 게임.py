N,K,*l=map(int,open(0).read().split())
v=[0]*N
i=c=0
while v[i]<1:
    c+=1
    v[i]=1
    i=l[i]
    if i==K:
        exit(print(c))
else:
    print(-1)