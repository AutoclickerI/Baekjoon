[N,K],*b=[[*map(int,i.split())]for i in open(0)]
d={i:{}for i in range(N)}

from heapq import*
hq=[(0,K,1<<K)]

while hq:
    c,n,v=heappop(hq)
    if v==2**N-1:
        print(c)
        break
    for e in range(N):
        nn=v|(1<<e)
        if c+b[n][e]<d[e].get(nn,1e9):
            d[e][nn]=c+b[n][e]
            heappush(hq,(c+b[n][e],e,nn))