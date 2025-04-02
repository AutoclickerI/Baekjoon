import sys
input=sys.stdin.readline

from heapq import*

for TC in[0]*int(input()):
    N=int(input())
    l=[[*map(int,input().split())]for _ in[0]*N]
    
    edges=[[]for _ in[0]*N]
    deg=[0]*N
    
    for i in range(N):
        p,q=l[i]
        for j in range(i+1,N):
            r,s=l[j]
            if p<r<s<q:
                edges[j]+=i,
                deg[i]+=1
    
    hq=[]
    
    for i in range(N):
        if deg[i]<1:heappush(hq,i)
    
    a=[]
    
    while hq:
        n=heappop(hq)
        a+=n,
        for e in edges[n]:
            deg[e]-=1
            if deg[e]<1:
                heappush(hq,e)
    
    print(*[i+1 for i in a])