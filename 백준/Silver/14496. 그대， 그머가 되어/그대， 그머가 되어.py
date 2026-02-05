[a,b],[N,M],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for s,e in l:
    edges[s]+=e,
    edges[e]+=s,

v=[0]*-~N
l=[(1,a)]
v[a]=1
for c,n in l:
    if n==b:
        print(c-1)
        break
    for e in edges[n]:
        if v[e]<1:
            v[e]=c+1
            l+=(c+1,e),
else:
    print(-1)