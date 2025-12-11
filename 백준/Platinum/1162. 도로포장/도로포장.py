[N,M,K],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~N]
v=[-~K*[float('inf')]for _ in[0]*N]

for s,e,x in l:
    edges[s-1]+=(e-1,x),
    edges[e-1]+=(s-1,x),

v[0][0]=0

hq=[(0,0,0)]

from heapq import*

while hq:
    c,k,n=heappop(hq)
    if v[n][k]<c:continue
    for e,x in edges[n]:
        if c+x<v[e][k]:
            v[e][k]=c+x
            heappush(hq,(c+x,k,e))
        if k<K and c<v[e][k+1]:
            v[e][k+1]=c
            heappush(hq,(c,k+1,e))
print(min(v[-1]))