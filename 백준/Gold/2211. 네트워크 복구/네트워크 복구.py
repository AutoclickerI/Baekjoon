[N,M],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]
for s,e,c in l:
    edges[s]+=(e,c),
    edges[e]+=(s,c),
v=[float('inf')]*-~N
r=[]
v[1]=0
from heapq import*

hq=[(0,1,1)]

while hq:
    c,n,p=heappop(hq)
    if v[n]<c:continue
    r+=(p,n),
    for e,x in edges[n]:
        if c+x<v[e]:
            v[e]=c+x
            heappush(hq,(c+x,e,n))

r=r[1:]
print(len(r))
for i in r:print(*i)