import sys
input=sys.stdin.readline

from collections import deque

for T in range(1,int(input())+1):
    N=int(input())
    l=0,*map(int,input().split())
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    c=[1]*-~N
    for _ in[0]*~-N:
        s,e=map(int,input().split())
        if l[s]>l[e]:
            edges[e]+=s,
            deg[s]+=1
        if l[e]>l[s]:
            edges[s]+=e,
            deg[e]+=1    
    
    dq=deque()
    for i in range(1,N+1):
        if deg[i]<1:dq+=i,
    while dq:
        n=dq.popleft()
        for e in edges[n]:
            deg[e]-=1
            c[e]+=c[n]
            if deg[e]<1:
                dq+=e,
    print(f'Case #{T}:',max(c))