l=sorted([[*map(int,i.split())]for i in open(0)][1:])
from heapq import*
hq=[]
m=0
for s,e in l:
    while hq and hq[0]<=s:
        heappop(hq)
    heappush(hq,e)
    m=max(len(hq),m)
print(m)