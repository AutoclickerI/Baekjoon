from heapq import*
_,*l=map(int,open(a:=0))
hq=[]
for i in l:
    while hq and hq[0]<=i:
        heappop(hq)
    a+=len(hq)
    heappush(hq,i)
print(a)