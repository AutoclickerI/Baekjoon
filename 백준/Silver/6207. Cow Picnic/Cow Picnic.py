[K,N,M],*l=[[*map(int,i.split())]for i in open(0)]

edges=[[]for _ in[0]*-~N]

for s,e in l[K:]:
    edges[s]+=e,

r=[0]*-~N

for i,in l[:K]:
    v=[0]*-~N
    v[i]=1
    q=[i]
    for n in q:
        for e in edges[n]:
            if v[e]<1:
                v[e]=1
                q+=e,
    for i in range(N+1):
        r[i]+=v[i]

print(sum(i==K for i in r))