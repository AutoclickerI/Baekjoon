import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N,M=map(int,input().split())

edges=[[]for _ in[0]*-~N]

deg=[0]*-~N

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1

from heapq import*

hq=[]

for i in range(1,N+1):
    if deg[i]<1:
        heappush(hq,i)

a=[]

while hq:
    v=heappop(hq)
    a+=v,
    for e in edges[v]:
        deg[e]-=1
        if deg[e]<1:
            heappush(hq,e)

print(*a)