import sys
input=sys.stdin.readline

from collections import deque

while'1'<(s:=input()):
    N,M=map(int,s.split())
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    for _ in[0]*M:
        s,e=map(int,input().split())
        edges[s]+=e,
        deg[e]+=1
    dq=deque()
    for i in range(1,N+1):
        if deg[i]<1:dq+=i,
    
    a=[]
    
    while dq:
        n=dq.popleft()
        a+=n,
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                dq+=e,
    
    if len(a)!=N:
        print('IMPOSSIBLE')
    else:
        for i in a:
            print(i)