import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
f=0

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1

from collections import deque

dq=deque()

for i in range(1,N+1):
    if deg[i]<1:
        dq+=i,

a=[]

while dq:
    n=dq.popleft()
    a+=n,
    for e in edges[n]:
        deg[e]-=1
        if deg[e]<1:
            dq+=e,
    f|=len(dq)>1

print(*a)
print(f)