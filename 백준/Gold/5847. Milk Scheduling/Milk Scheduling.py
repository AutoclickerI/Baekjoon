import sys
input=sys.stdin.readline

N,M=map(int,input().split())

c=[0]

for _ in[0]*N:
    c+=int(input()),

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1

from collections import deque

dq=deque()
v=[0]*-~N

for i in range(1,N+1):
    if deg[i]<1:dq+=i,;v[i]=c[i]

while dq:
    n=dq.popleft()
    for e in edges[n]:
        deg[e]-=1
        v[e]=max(v[e],v[n]+c[e])
        if deg[e]<1:
            dq+=e,

print(max(v))