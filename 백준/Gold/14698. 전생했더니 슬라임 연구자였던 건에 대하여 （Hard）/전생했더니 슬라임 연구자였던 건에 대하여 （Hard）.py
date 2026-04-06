from heapq import*
for i in[*open(0)][2::2]:
    hq=sorted(map(int,i.split()))
    r=1
    while 1<len(hq):
        a,b=heappop(hq),heappop(hq)
        r*=a*b
        heappush(hq,a*b)
    print(r%(10**9+7))