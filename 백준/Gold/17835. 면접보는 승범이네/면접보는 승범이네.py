[N,M,K],*l,v=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]

for i in v:
    edges[0]+=(i,0),

for u,v,c in l:
    edges[v]+=(u,c),

v=[float('inf')]*-~N
v[0]=0

from heapq import*

hq=[(0,0)]

while hq:
    n,c=heappop(hq)
    if v[n]<c:
        continue
    for e,dc in edges[n]:
        if c+dc<v[e]:
            v[e]=c+dc
            heappush(hq,(e,c+dc))

r=-1
for i in range(N+1):
    if r<v[i]!=float('inf'):
        r=v[i]
        a=i
print(a,r)