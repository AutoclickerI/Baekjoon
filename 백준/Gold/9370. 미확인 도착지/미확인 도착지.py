import sys
input=sys.stdin.readline

from heapq import heappush,heappop
for _ in[0]*int(input()):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    edges=[[]for _ in[0]*-~n]
    for _ in[0]*m:
        a,b,d=map(int,input().split())
        edges[a]+=(b,d),
        edges[b]+=(a,d),
    end=[int(input())for _ in[0]*t]
    v=[float('inf')]*-~n
    vgh=[float('inf')]*-~n
    hq=[(1,0,s)]
    v[s]=0
    while hq:
        flag,cost,cur=heappop(hq)
        if v[cur]<cost:
            continue
        for e,d in edges[cur]:
            if cost+d<=v[e]:
                if flag and(cur,e)in[(g,h),(h,g)]:
                    vgh[e]=cost+d
                    v[e]=cost+d
                    heappush(hq,(0,cost+d,e))
                elif cost+d<v[e]:
                    v[e]=cost+d
                    heappush(hq,(flag,cost+d,e))
            if flag<1 and cost+d<vgh[e]:
                vgh[e]=cost+d
                heappush(hq,(flag,cost+d,e))
    nend=[i for i in end if v[i]==vgh[i]!=float('inf')]
    print(*sorted(nend))