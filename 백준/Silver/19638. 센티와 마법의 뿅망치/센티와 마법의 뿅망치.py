N,H,T,*v=map(int,open(0).read().split())

from heapq import*
v=sorted(-i for i in v)
c=0
while H<=-v[0]and T:
    T-=1
    c+=1
    n=max(-heappop(v)//2,1)
    heappush(v,-n)
n=-heappop(v)
if H<=n:
    print('NO',n)
else:
    print('YES',c)