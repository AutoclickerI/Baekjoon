N,*l=map(int,open(0).read().split())
from heapq import*
h=[]
c=r=i=0
for j,k in sorted(zip(l[N:],l)):
 heappush(h,-k);i+=1
 if c*2<i:r-=heappop(h);c+=1
print(r)