N,*l=map(int,open(0).read().split())
from heapq import*
h=[]
r=i=0
for j,k in sorted(zip(l[N:],l)):
 heappush(h,-k);i+=1
 if 0<i:r-=heappop(h);i-=2
print(r)