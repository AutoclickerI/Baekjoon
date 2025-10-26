N,M,R=map(int,input().split())
edges=[[]for _ in[0]*N]
for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s-1]+=e-1,
    edges[e-1]+=s-1,
l=[R-1]
v=[0]*N
v[R-1]=1
c=1
for i in l:
    for e in sorted(edges[i])[::-1]:
        if v[e]<1:
            c+=1
            v[e]=c
            l+=e,
print(*v)