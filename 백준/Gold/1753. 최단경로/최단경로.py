import sys
input=sys.stdin.readline

V,E=map(int,input().split())

K=int(input())

edges=[[]for _ in[0]*-~V]

for _ in[0]*E:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),

from heapq import*

hq=[(0,K)]
v=[1e9]*-~V
v[K]=0
while hq:
    c,s=heappop(hq)
    if v[s]<c:
        continue
    for n,co in edges[s]:
        if co+c<v[n]:
            v[n]=co+c
            heappush(hq,(co+c,n))

for i in v[1:]:
    print(['INF',i][i<1e9])