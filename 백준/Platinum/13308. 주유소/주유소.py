from heapq import*

[N,M],C,*l=[map(int,i.split())for i in open(0)]
C=0,*C
edges=[[]for _ in[0]*-~N]
for a,b,c in l:
    edges[a]+=(b,c),
    edges[b]+=(a,c),

d=[2501*[float('inf')]for _ in[0]*-~N]
s=C[1]
d[1][s]=0
hq=[(0,1,s)]

while hq:
    c,n,p=heappop(hq)
    if d[n][p]<c:
        continue
    if n==N:
        exit(print(c))
    for e,w in edges[n]:
        np=min(p,C[e])
        nc=c+p*w
        if nc<d[e][np]:
            d[e][np]=nc
            heappush(hq,(nc,e,np))