N,L=map(int,input().split())
l=sorted(map(int,input().split()))
from heapq import*
hq=[l.pop()]
added=[]
hval=1
m=1
while l and ((hq[0]>=hval-1 if hq else 1) or L) and (hval<=added[0]if added else 1):
    hval+=1
    heappush(hq,l.pop())
    while L and hq and hq[0]<hval:
        heappush(added,heappop(hq)+1)
        L-=1
    if (hq[0]>=hval if hq else 1) and (hval<=added[0]if added else 1):
        m=len(hq)+len(added)
print(m)