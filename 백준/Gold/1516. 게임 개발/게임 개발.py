import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())

edges=[[]for _ in[0]*N]
deg=[0]*N
c=[]

for i in range(N):
    p,*l,_=map(int,input().split())
    c+=p,
    for j in l:
        edges[j-1]+=i,
        deg[i]+=1

v=[0]*N

from collections import deque

dq=deque()

for i in range(N):
    if deg[i]<1:
        v[i]=c[i]
        dq+=i,

while dq:
    n=dq.popleft()
    for e in edges[n]:
        deg[e]-=1
        v[e]=max(v[e],v[n]+c[e])
        if deg[e]<1:
            dq+=e,

print(*v)