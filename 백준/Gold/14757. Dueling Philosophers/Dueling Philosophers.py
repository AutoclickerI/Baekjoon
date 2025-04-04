import sys
input=sys.stdin.readline

from collections import deque
while 1:
    N,M=map(int,input().split())
    if N==M==0:break
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    
    for _ in[0]*M:
        d,u=map(int,input().split())
        edges[d]+=u,
        deg[u]+=1
    
    dq=deque()
    
    for i in range(1,N+1):
        if deg[i]<1:dq+=i,
    
    f=0
    a=0
    
    while dq:
        f|=len(dq)>1
        n=dq.popleft()
        a+=1
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:dq+=e,
    
    print(-~f*(a==N))