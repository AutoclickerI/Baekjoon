_,*l=[[*map(int,i.split())][::-1]for i in open(0)]
l.sort()
d=10000

c=0

from heapq import*
hq=[]
while d:
    while l and d<=l[-1][0]:
        heappush(hq,-l.pop()[1])
    if hq:
        c-=heappop(hq)
    d-=1
print(c)