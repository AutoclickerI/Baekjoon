[N,M],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]
for A,B,C in l:edges[A]+=(B,C),;edges[B]+=(A,C),
from heapq import*
hq=[(0,1)]
v=[float('inf')]*-~N
v[1]=0

while hq:
    c,n=heappop(hq)
    if v[n]<c:
        continue
    for e,x in edges[n]:
        if c+x<v[e]:
            v[e]=c+x
            heappush(hq,(c+x,e))
print(v[-1])