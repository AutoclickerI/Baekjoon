A,K=map(int,input().split())

v=[0]*-~K
l=[(0,A)]
for c,n in l:
    for e in-~n,2*n:
        if e<=K and v[e]<1:
            v[e]=c+1
            l+=(c+1,e),
print(v[K])