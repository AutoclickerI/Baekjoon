from heapq import*
[N,M],v,w=[[*map(int,i.split())]for i in open(0)]
hq=sorted(-i for i in v)
for i in w:
    v=heappop(hq)
    if i<=-v:
        v+=i
        heappush(hq,v)
    else:
        print(0)
        break
else:
    print(1)