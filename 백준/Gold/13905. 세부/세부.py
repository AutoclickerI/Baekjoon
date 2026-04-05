from heapq import*
[N,M],[s,e],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for p,q,c in l:
    edges[p]+=(q,c),
    edges[q]+=(p,c),

v=[0]*-~N
v[s]=float('inf')
hq=[(-float('inf'),s)]
while hq:
    c,n=heappop(hq)
    if -c<v[n]:
        continue
    for nn,mc in edges[n]:
        if v[nn]<min(-c,mc):
            v[nn]=min(-c,mc)
            heappush(hq,(-min(-c,mc),nn))
print(v[e])