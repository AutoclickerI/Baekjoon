import sys
input=sys.stdin.readline

N,M=map(int,input().split())

edges=[[]for _ in[0]*N]
v=[0]*N
deg=[0]*N

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s-1]+=e-1,
    deg[e-1]+=1

from heapq import*

hq=[]

for i in range(N):
    if deg[i]<1:
        v[i]=1
        heappush(hq,i)

while hq:
    n=heappop(hq)
    for e in edges[n]:
        deg[e]-=1
        v[e]=max(v[e],v[n]+1)
        if deg[e]<1:
            heappush(hq,e)

print(*v)