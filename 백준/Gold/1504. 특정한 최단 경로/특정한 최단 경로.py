import sys
input=sys.stdin.readline

N,E=map(int,input().split())

edges=[[]for _ in[0]*-~N]

for _ in[0]*E:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),
    edges[e]+=(s,c),

from heapq import*

def dijkstra(s,e):
    hq=[(0,s)]
    v=[1e9]*-~N
    v[s]=0
    while hq:
        c,s=heappop(hq)
        if s==e:
            return c
        if v[s]<c:
            continue
        for n,co in edges[s]:
            if co+c<v[n]:
                v[n]=co+c
                heappush(hq,(co+c,n))
    return -1

s,e=map(int,input().split())

c1s=dijkstra(1,s)
c1e=dijkstra(1,e)
ces=dijkstra(e,s)
csN=dijkstra(s,N)
ceN=dijkstra(e,N)

if -1 in[c1s,c1e,ces,csN,ceN]:
    print(-1)
else:
    print(min(c1s+ceN,c1e+csN)+ces)