n=int(input())
m,*l=sorted(map(int,input().split()))[::-1]
from heapq import*
hq=[-m]
for i in l:
    if-hq[0]-1>i:
        heappop(hq)
    heappush(hq,-i)
print(len(hq))