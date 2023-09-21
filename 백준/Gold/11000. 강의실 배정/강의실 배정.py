from heapq import*
hq=[-1]
for p,q in sorted([*map(int,i.split())]for i in[*open(0)][1:]):
    if hq[0]<=p:heapreplace(hq,q)
    else:heappush(hq,q)
print(len(hq))