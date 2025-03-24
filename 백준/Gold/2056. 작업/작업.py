N=int(input())

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
v=[0]*-~N

from heapq import*

for e in range(1,N+1):
    c,_,*l=map(int,input().split())
    v[e]=c
    for s in l:
        edges[s]+=e,
        deg[e]+=1

hq=[]
c=[0]*-~N

for s in range(1,N+1):
    if deg[s]<1:
        c[s]=v[s]
        heappush(hq,s)

while hq:
    n=heappop(hq)
    for e in edges[n]:
        c[e]=max(c[e],c[n]+v[e])
        deg[e]-=1
        if deg[e]<1:
            heappush(hq,e)

print(max(c))