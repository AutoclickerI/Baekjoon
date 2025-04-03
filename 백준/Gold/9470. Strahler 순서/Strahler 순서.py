import sys
input=sys.stdin.readline

from collections import deque

for T in[0]*int(input()):
    K,M,P=map(int,input().split())
    edges=[[]for _ in[0]*M]
    deg=[0]*M
    c=[[0,0]for _ in[0]*M]
    
    for _ in[0]*P:
        s,e=map(int,input().split())
        edges[s-1]+=e-1,
        deg[e-1]+=1
    
    dq=deque()
    
    for i in range(M):
        if deg[i]<1:dq+=i,;c[i]=1
    
    while dq:
        n=dq.popleft()
        for e in edges[n]:
            c[e][1]+=c[e][0]==c[n]
            c[e]=max(c[e],[c[n],0])
            deg[e]-=1
            if deg[e]<1:
                c[e]=c[e][0]+(c[e][1]>0)
                dq+=e,
    
    print(K,max(c))