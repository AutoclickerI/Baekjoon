import sys
input=sys.stdin.readline

from collections import deque

for T in[0]*int(input()):
    n,c,s=map(int,input().split())
    edges=[[]for _ in[0]*-~n]
    deg=[0]*-~n
    l=[-1]
    for _ in[0]*n:
        l+=int(input()),
    for _ in[0]*c:
        p,e=map(int,input().split())
        edges[e]+=p,
        deg[p]+=1
    
    cnt=[0]*-~n # 1 odd, 2 even, 3 all
    
    dq=deque()
    
    for i in range(1,n+1):
        if deg[i]<1:
            dq+=i,
            cnt[i]=2
    
    while dq:
        n=dq.popleft()
        for e in edges[n]:
            if l[e]==l[n]:
                cnt[e]|=cnt[n]%2*2+cnt[n]//2
            elif l[n]==0:
                if cnt[n]==1:
                    cnt[e]|=2
                if cnt[n]==2:
                    cnt[e]|=1
            else:
                if cnt[n]==2:
                    cnt[e]|=1
                if cnt[n]==1:
                    cnt[e]|=2
            deg[e]-=1
            if deg[e]<1:
                dq+=e,
    #print(cnt)
    if l[s]:
        if cnt[s]%2:
            print(1)
        else:
            print(0)
    else:
        if cnt[s]//2:
            print(0)
        else:
            print(1)