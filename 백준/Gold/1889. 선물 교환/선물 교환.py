import sys
input=sys.stdin.readline

N=int(input())

edges=[0]
deg=[0]*-~N

for _ in[0]*N:
    a,b=l=[*map(int,input().split())]
    deg[a]+=1
    deg[b]+=1
    edges+=l,

from collections import deque

dq=deque()

for i in range(1,N+1):
    if deg[i]<2:dq+=i,

while dq:
    n=dq.popleft()
    for e in edges[n]:
        deg[e]-=1
        if deg[e]==1:
            dq+=e,

l=[i for i in range(1,N+1)if deg[i]]

print(len(l))
print(*l)