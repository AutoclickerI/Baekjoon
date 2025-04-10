from collections import deque

for T in[0]*int(input()):
    N=int(input())
    *l,=map(int,input().split())
    
    edges=[[]for _ in[0]*N]
    deg=[0]*N
    
    for i in range(N):
        edges[i]+=l[i]-1,
        deg[l[i]-1]+=1
    
    dq=deque()
    for i in range(N):
        if deg[i]<1:
            dq+=i,
    
    a=0
    
    while dq:
        n=dq.popleft()
        a+=1
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                dq+=e,
    
    print(a)