[N,D],*l=[[*map(int,i.split())]for i in open(0)]

v=[float('inf')]*-~D
v[0]=0

edges=[[]for _ in[0]*-~D]
for s,e,c in l:
    if e<=D:
        edges[s]+=(e,c),

for i in range(D+1):
    v[i]=min(v[i],v[i-1]+1)
    for e,c in edges[i]:
        v[e]=min(v[e],v[i]+c)

print(v[-1])