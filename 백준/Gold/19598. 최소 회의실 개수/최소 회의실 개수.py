l=sorted([[*map(int,i.split())]for i in open(0)][1:])
from heapq import*
h=[]
m=0
for s,e in l:
    while h and h[0]<=s:heappop(h)
    heappush(h,e);m=max(len(h),m)
print(m)