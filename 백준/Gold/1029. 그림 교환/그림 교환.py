N=int(input())
b=[input()for _ in[0]*N]

v=[[1e9]*2**N for _ in[0]*N]
v[0][1]=0

from heapq import*
hq=[(0,1,0)]

while hq:
    c,n,p=heappop(hq)
    for e in range(N):
        nn=n|1<<e
        nc=int(b[p][e])
        if c<=nc:
            if n!=nn and nc<v[e][nn]:
                v[e][nn]=nc
                heappush(hq,(nc,nn,e))

print(max(i.bit_count()for j in range(N)for i in range(2**N)if v[j][i]!=1e9))