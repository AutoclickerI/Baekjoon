N=int(input())
M=int(input())

edges=[[]for _ in[0]*-~N]
for _ in[0]*M:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),

cost=[1e9]*-~N

s,e=map(int,input().split())
cost[s]=0

from heapq import *

hq=[(0,s)]

while hq:
    c,v=heappop(hq)
    if v==e:
        break
    if c<cost[v]:continue
    for nv,nc in edges[v]:
        if c+nc<cost[nv]:
            cost[nv]=c+nc
            heappush(hq,(c+nc,nv))
print(c)