import sys
input=sys.stdin.readline

from collections import deque

N,M,C=map(int,input().split())

S=[0,*map(int,input().split())]

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
cost={}

for _ in[0]*C:
    s,e,t=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1
    cost[s,e]=max(cost.get((s,e),0),t)

dq=deque()

for i in range(1,N+1):
    if deg[i]<1:dq+=i,

while dq:
    n=dq.popleft()
    for e in edges[n]:
        S[e]=max(S[e],S[n]+cost[n,e])
        deg[e]-=1
        if deg[e]<1:
            dq+=e,

print(*S[1:])