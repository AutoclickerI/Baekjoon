ss=open(0).read().strip()

[n,m],*l,[s,t]=[map(int,i.split())for i in ss.split('\n')]
edges=[[]for _ in[0]*-~n]

for a,b,c in l:
    edges[b]+=(a,c),
    edges[a]+=(b,c),

v=[1e9]*-~n
v[s]=0
hq=[(0,s)]

from heapq import*

while 1:
    c,n=heappop(hq)
    if v[n]<c:continue
    if n==t:break
    for e,x in edges[n]:
        if c+x<v[e]:
            v[e]=c+x
            heappush(hq,(c+x,e))
print(c)