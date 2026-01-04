[N,M],v,*l=[[*map(int,i.split())]for i in open(0)]
v[-1]=0
edges=[[]for _ in[0]*N]
for s,e,c in l:
    if v[s]|v[e]<1:
        edges[s]+=(e,c),
        edges[e]+=(s,c),
v=[float('inf')]*N
v[0]=0
hq=[(0,0)]
from heapq import*

while hq:
    c,n=heappop(hq)
    if v[n]<c:
        continue
    for e,dc in edges[n]:
        if c+dc<v[e]:
            v[e]=c+dc
            heappush(hq,(c+dc,e))

print(-(v[-1]==float('inf'))or v[-1])