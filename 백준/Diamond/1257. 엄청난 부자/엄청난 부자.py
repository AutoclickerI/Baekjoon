M,N,*A=map(int,open(0).read().split())
A.sort()

C=A.pop()
v=[float('inf')]*C
v[0]=0

hq=[(0,0)]

from heapq import*

while hq:
    c,n=heappop(hq)
    if v[n]<c:
        continue
    for i in A:
        nn=(n+C-i)%C
        if c+C-i<v[nn]:
            v[nn]=c+C-i
            heappush(hq,(c+C-i,nn))

print((M+v[-M%C])//C)