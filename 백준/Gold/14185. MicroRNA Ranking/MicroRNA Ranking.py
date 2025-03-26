import sys
input=sys.stdin.readline

from heapq import*

while'1'<(s:=input()):
    N,M=map(int,s.split())
    d=[0]*1001000
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    hq=[]
    a=[]
    
    for _ in[0]*M:
        *l,=map(int,input().split())
        for i in range(N):
            for j in range(i+1,N):
                v=l[i]*1000+l[j]
                d[v]+=1
                if M<d[v]*2:
                    edges[l[i]]+=l[j],
                    deg[l[j]]+=1
                    d[v]=0
    
    for i in range(1,N+1):
        if deg[i]<1:
            heappush(hq,i)
    
    while hq:
        n=heappop(hq)
        a+=n,
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                heappush(hq,e)
    if len(a)==N:
        print(*a)
    else:
        print('No solution')