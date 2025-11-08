[N],[M],*l=[map(int,i.split())for i in open(0)]

edges1=[[]for _ in[0]*-~N]
edges2=[[]for _ in[0]*-~N]
for s,e in l:edges1[s]+=e,;edges2[e]+=s,

for i in range(1,N+1):
    v1=[0]*-~N
    v1[i]=1
    l=[i]
    for n in l:
        for e in edges1[n]:
            if v1[e]<1:
                v1[e]=1
                l+=e,
    v2=[0]*-~N
    v2[i]=1
    l=[i]
    for n in l:
        for e in edges2[n]:
            if v2[e]<1:
                v2[e]=1
                l+=e,
    print(N-sum(i|j for i,j in zip(v1,v2)))