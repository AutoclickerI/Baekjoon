import sys
input=sys.stdin.readline

N,M=map(int,input().split())

edges=[[]for _ in[0]*N]
v=[0]*N
deg=[0]*N

for _ in[0]*M:
    _,*l=map(int,input().split())
    for s,e in zip(l,l[1:]):
        edges[s-1]+=e-1,
        deg[e-1]+=1

from heapq import*

hq=[]

for i in range(N):
    if deg[i]<1:
        v[i]=1
        heappush(hq,i)

a=[]

while hq:
    n=heappop(hq)
    a+=n,
    for e in edges[n]:
        deg[e]-=1
        v[e]=max(v[e],v[n]+1)
        if deg[e]<1:
            heappush(hq,e)

if any(deg):
    print(0)
else:
    for i in a:
        print(i+1)