import sys
input=sys.stdin.readline

N,O,S,E=map(int,input().split())

edges=[[]for _ in[0]*-~N]
wormholes={}

for _ in[0]*int(input()):
    s,e=map(int,input().split())
    edges[s]+=e,
    edges[e]+=s,

for _ in[0]*int(input()):
    wormholes[tuple(map(int,input().split()))]=1

cost=[-~N*[float('inf')]for _ in[0]*-~O]

cost[1][S]=0
    
from heapq import*

hq=[(0,1,S)]

while hq:
    c,o,n=heappop(hq)
    if cost[o][n]<c:
        continue
    if(o,n)in wormholes:
        cost[o+1][n]=cost[o][n]
        heappush(hq,(c,o+1,n))
    for e in edges[n]:
        if cost[o][n]+1<cost[o][e]:
            cost[o][e]=cost[o][n]+1
            heappush(hq,(c+1,o,e))

v=cost[-1][E]
f=v==float('inf')

for _ in[0]*int(input()):
    a,b=map(int,input().split())
    if f:
        print(-1)
    else:
        print(a*v+~-O*b)