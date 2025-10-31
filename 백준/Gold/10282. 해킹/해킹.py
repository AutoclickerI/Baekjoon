from heapq import*

for T in[0]*int(input()):
    n,d,c=map(int,input().split())
    edges=[[]for _ in[0]*-~n]
    for _ in[0]*d:
        a,b,s=map(int,input().split())
        edges[b]+=(a,s),
    hq=[(0,c)]
    v=[0]*-~n
    mt=0
    while hq:
        t,c=heappop(hq)
        if v[c]:continue
        mt=t
        v[c]=1
        for e,s in edges[c]:
            if v[e]<1:
                heappush(hq,(t+s,e))
    print(sum(v),mt)