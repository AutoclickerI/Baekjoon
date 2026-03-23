from heapq import*
[N,M],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]
edges_pd=[[]for _ in[0]*2*-~N]

for a,b,d in l:
    edges[a]+=(b,2*d),
    edges[b]+=(a,2*d),
    edges_pd[a*2]+=(b*2+1,d),
    edges_pd[a*2+1]+=(b*2,4*d),
    edges_pd[b*2]+=(a*2+1,d),
    edges_pd[b*2+1]+=(a*2,4*d),

def dijkstra(N,s,edges):
    v=[float('inf')]*-~N
    v[s]=0
    hq=[(0,s)]
    while hq:
        c,n=heappop(hq)
        if v[n]<c:
            continue
        for e,dc in edges[n]:
            if c+dc<v[e]:
                v[e]=c+dc
                heappush(hq,(c+dc,e))
    return v

v=dijkstra(N,1,edges)
vab=dijkstra(N*2+1,2,edges_pd)
*vab,=map(min,zip(*[iter(vab)]*2))
print(sum(i<j for i,j in zip(v,vab)))