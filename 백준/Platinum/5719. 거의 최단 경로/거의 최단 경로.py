import sys
input=sys.stdin.readline

from heapq import*

while'1'<(s:=input()):
    N,M=map(int,s.split())
    S,D=map(int,input().split())
    edges=[[]for _ in[0]*N]
    dist=[float('inf')]*N
    used=[[]for _ in[0]*N]
    s=set()
    for _ in[0]*M:
        u,v,p=map(int,input().split())
        s.add((u,v,p))
        edges[u]+=(v,p),
    dist[S]=0
    hq=[(0,S)]
    while hq:
        cost,n=heappop(hq)
        if dist[n]<cost:
            continue
        for e,c in edges[n]:
            if cost+c<dist[e]:
                dist[e]=cost+c
                used[e]=[]
                heappush(hq,(cost+c,e))
            if cost+c==dist[e]:
                used[e]+=(n,e,c),
    de=[0]*-~N
    ld=[D]
    for i in ld:
        if de[i]<1:
            de[i]=1
            for u,v,p in used[i]:
                s.remove((u,v,p))
                ld+=u,
    edges=[[]for _ in[0]*N]
    dist=[float('inf')]*N
    used=[[]for _ in[0]*N]
    for u,v,p in s:
        edges[u]+=(v,p),
    dist[S]=0
    hq=[(0,S)]
    while hq:
        cost,n=heappop(hq)
        if dist[n]<cost:
            continue
        for e,c in edges[n]:
            if cost+c<dist[e]:
                dist[e]=cost+c
                used[e]=[]
                heappush(hq,(cost+c,e))
            if cost+c==dist[e]:
                used[e]+=(n,e,c),
    if dist[D]!=float('inf'):
        print(dist[D])
    else:
        print(-1)