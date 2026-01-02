[N],*l,[L,P]=[[*map(int,i.split())]for i in open(0)]
l.sort()
hq=[]
c=0
from heapq import*
try:
    for a,b in l:
        while P<a:
            P-=heappop(hq)
            c+=1
        heappush(hq,-b)
    while P<L:
        P-=heappop(hq)
        c+=1
    print(c)
except:
    print(-1)