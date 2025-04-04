import sys
input=sys.stdin.readline

from collections import deque

N,M=map(int,input().split())
edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
cost={}

for _ in[0]*M:
    s,t,c=map(int,input().split())
    edges[s]+=t,
    deg[t]+=1
    cost[s,t]=max(cost.get((s,t),0),c)

dq=deque()

for i in range(1,N+1):
    if deg[i]<1:dq+=i,

f=0

c=[0]*-~N

while dq:
    n=dq.popleft()
    for e in edges[n]:
        c[e]=max(c[e],c[n]+cost[n,e])
        deg[e]-=1
        if deg[e]<1:dq+=e,

print(max(c))