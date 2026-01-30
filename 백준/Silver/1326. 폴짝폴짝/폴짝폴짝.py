N,*b,s,e=map(int,open(0).read().split())
v=[0]*N
l=[(0,s-1)]
for c,n in l:
    for d in range(0,10000,b[n]):
        if n+d<N and v[n+d]<1:
            v[n+d]=c+1
            l+=(c+1,n+d),
        if 0<=n-d and v[n-d]<1:
            v[n-d]=c+1
            l+=(c+1,n-d),
print(v[e-1]or-1)