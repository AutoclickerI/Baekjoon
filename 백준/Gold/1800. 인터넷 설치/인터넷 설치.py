[N,P,K],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for s,e,c in l:
    edges[s]+=(e,c),
    edges[e]+=(s,c),

from heapq import*

def dijkstra(mc):
    v=[float('inf')]*-~N
    v[1]=0
    
    hq=[(0,1)]
    while hq:
        cc,n=heappop(hq)
        if v[n]<cc:
            continue
        for e,c in edges[n]:
            nc=cc+(mc<c)
            if nc<v[e]:
                v[e]=nc
                heappush(hq,(nc,e))
    
    return v[N]

v=dijkstra(0)
if v==float('inf'):
    print(-1)
elif v<=K:
    print(0)
else:
    s=0
    e=10**6+1
    while 1<e-s:
        m=s+e>>1
        if dijkstra(m)<=K:
            e=m
        else:
            s=m
    print(e)