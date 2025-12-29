N=int(input())
b=[[*map(int,input().split())]for _ in[0]*N]
c=int(input()[::-1].translate({89:49,78:48}),2)
P=int(input())

from heapq import*
if c<1:
    if P<1:print(0)
    else:print(-1)
else:
    hq=[(0,c)]
    v=[float('inf')]*2**N
    v[c]=0
    while 1:
        c,n=heappop(hq)
        if v[n]<c:continue
        if P<=n.bit_count():
            break
        for e in range(N):
            nc=float('inf')
            for s in range(N):
                if(1<<s)&n:
                    nc=min(nc,b[s][e]+c)
            if nc<v[n|(1<<e)]:
                v[n|(1<<e)]=nc
                heappush(hq,(nc,n|(1<<e)))
    print(c)