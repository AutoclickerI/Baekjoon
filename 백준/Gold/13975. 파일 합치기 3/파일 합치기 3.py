from heapq import*

for i in[*open(0)][2::2]:
    *hq,=map(int,i.split())
    heapify(hq)
    a=0
    while 1<len(hq):
        v=heappop(hq)+heappop(hq)
        heappush(hq,v)
        a+=v
    print(a)