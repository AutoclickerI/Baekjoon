N,K,*A=map(int,open(0).read().split())
A=sorted((v,i)for i,v in enumerate(A))

C,vi=A.pop()
v=[float('inf')]*C
r=[0]*C
v[0]=0
r[0]=[0]*N

hq=[(0,0)]

from heapq import*

while hq:
    c,n=heappop(hq)
    if v[n]<c:
        continue
    for i,z in A:
        nn=(n-i)%C
        if c+i<v[nn]:
            v[nn]=c+i
            r[nn]=r[n][:]
            r[nn][z]+=1
            heappush(hq,(c+i,nn))

t=-K%C
rr=r[t]
if rr==0 or K<v[t]:
    print(-1)
else:
    K-=v[t]
    rr[vi]+=K//C
    print(*rr)