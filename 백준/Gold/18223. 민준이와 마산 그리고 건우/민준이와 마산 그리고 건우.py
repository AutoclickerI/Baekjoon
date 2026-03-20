import sys
input=sys.stdin.readline

V,E,P=map(int,input().split())
edges=[[]for _ in[0]*-~V]

for _ in[0]*E:
    a,b,c=map(int,input().split())
    edges[a]+=(b,3*c-(P in(a,b))),
    edges[b]+=(a,3*c-(P in(a,b))),

v=[float('inf')]*-~V
v[1]=0
from heapq import*

hq=[(1,0)]

while hq:
    n,c=heappop(hq)
    if v[n]<c:
        continue
    for e,dc in edges[n]:
        if c+dc<v[e]:
            v[e]=c+dc
            heappush(hq,(e,c+dc))

print(['GOOD BYE','SAVE HIM'][0<v[V]%3])