import sys
input=sys.stdin.readline

flag=1
try:
    *l,=map(int,open(0).read().split())
    iterator=iter(l)
except:
    flag=0

assert flag

from heapq import*

while 1:
    N1,N2,D=next(iterator),next(iterator),next(iterator)
    if N1==N2==D==0:
        break
    N=N1+N2
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    for _ in[0]*D:
        x,y=next(iterator),next(iterator)
        edges[y]+=x,
        deg[x]+=1
    deg_o=deg[:]
    
    hq=[]
    
    for i in range(1,N+1):
        if deg[i]<1:heappush(hq,(N1<i,i))
    
    cnt=0
    f=-1
    
    while hq:
        parity,n=heappop(hq)
        if parity!=f:
            f=parity
            cnt+=1
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                heappush(hq,(parity+((N1<e)^(N1<n)),e))
    
    cnt2=0
    deg=deg_o[:]
    
    for i in range(1,N+1):
        if deg[i]<1:heappush(hq,(2-(N1<i),i))
    f=-1
    
    while hq:
        parity,n=heappop(hq)
        if parity!=f:
            f=parity
            cnt2+=1
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                heappush(hq,(parity+((N1<e)^(N1<n)),e))
    
    print(1+min(cnt,cnt2))