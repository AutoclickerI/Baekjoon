N=int(input())
l=[[*map(int,input().split())]for _ in[0]*N]
l.sort()

hq=[]

from heapq import*

for d,W in l:
    heappush(hq,W)
    while d<len(hq):
        heappop(hq)
print(sum(hq))