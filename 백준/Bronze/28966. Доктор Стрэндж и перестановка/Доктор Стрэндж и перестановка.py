n,*l=map(int,open(0).read().split())
L=[(~i%2)^(j%2)for i,j in enumerate(l)]
if sum(L)==0:
    if n>2:
        print(1,3)
    else:
        print(-1,-1)
elif sum(L)==2:
    i=L.index(1)
    L[i]=0
    j=L.index(1)
    if i+j&1:
        print(i+1,j+1)
    else:
        print(-1,-1)
else:
    print(-1,-1)