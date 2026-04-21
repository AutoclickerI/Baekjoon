[N,M,K],[S,D],*l=[[*map(int,i.split())]for i in open(0)]
v=[N*[float('inf')]for _ in[0]*-~N]
v[S][0]=0

edges=[[]for _ in[0]*-~N]

for s,e,c in l[:M]:
    edges[s]+=(e,c),
    edges[e]+=(s,c),

from heapq import*
hq=[(0,0,S)]

while hq:
    t,cost,n=heappop(hq)
    if v[n][t]<cost:
        continue
    for e,c in edges[n]:
        if t+1<N and cost+c<v[e][t+1]and cost+c<v[e][t]:
            v[e][t+1]=cost+c
            heappush(hq,(t+1,cost+c,e))

tx=0
for i,in[0],*l[M:]:
    tx+=i
    r=float('inf')
    for j in range(N):
        r=min(r,v[D][j]+j*tx)
    print(r)