[N,M],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]
v=[float('inf')]*-~N

for s,e in l:edges[s]+=e,;edges[e]+=s,

v[1]=0

from heapq import*
hq=[(0,1)]

while hq:
    c,n=heappop(hq)
    if v[n]<c:
        continue
    for e in edges[n]:
        if c+1<v[e]:
            v[e]=c+1
            heappush(hq,(c+1,e))
print(m:=max(range(1,N+1),key=lambda i:v[i]),v[m],v.count(v[m]))