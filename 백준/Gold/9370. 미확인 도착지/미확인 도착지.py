from heapq import*
for _ in[0]*int(input()):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    edges=[[]for _ in[0]*-~n]
    for _ in[0]*m:
        a,b,d=map(int,input().split())
        d*=2
        if (a,b)in[(g,h),(h,g)]:
            d-=1
        edges[a]+=(b,d),
        edges[b]+=(a,d),
    end=[int(input())for _ in[0]*t]
    v=[float('inf')]*-~n
    hq=[(0,s)]
    v[s]=0
    while hq:
        cost,cur=heappop(hq)
        if v[cur]<cost:
            continue
        for e,d in edges[cur]:
            if cost+d<v[e]:
                v[e]=cost+d
                heappush(hq,(cost+d,e))
    nend=[i for i in end if v[i]%2==1]
    print(*sorted(nend))