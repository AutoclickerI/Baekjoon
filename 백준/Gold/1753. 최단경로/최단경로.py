[V,E],[K],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~V]

for s,e,c in l:
    edges[s]+=(e,c),

from heapq import*

hq=[(0,K)]
v=[float('inf')]*(V+1)
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
    if i==float('inf'):
        print('INF')
    else:
        print(i)