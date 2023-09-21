from heapq import*
_,*l=[[*map(int,i.split())]for i in open(0)]
hq=[-1]
for p,q in sorted(l):
    if hq[0]<=p:
        heapreplace(hq,q)
    else:
        heappush(hq,q)
print(len(hq))