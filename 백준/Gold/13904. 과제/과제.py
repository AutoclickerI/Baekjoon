_,*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
d=l[-1][0]

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