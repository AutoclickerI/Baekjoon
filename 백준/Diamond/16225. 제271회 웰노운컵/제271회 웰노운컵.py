_,A,B=[map(int,i.split())for i in open(0)]

from heapq import*
hq=[]
c=r=0
for i,(j,k)in enumerate(sorted(zip(B,A))):
    heappush(hq,-k)
    if c*2<=i:
        r-=heappop(hq)
        c+=1
print(r)