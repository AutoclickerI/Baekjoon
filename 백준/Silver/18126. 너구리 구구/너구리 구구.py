[N],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for a,b,c in l:
    edges[a]+=(b,c),
    edges[b]+=(a,c),

d=[-1]*-~N
d[1]=0
l=[1]

for n in l:
    for e,w in edges[n]:
        if d[e]<0:
            d[e]=d[n]+w
            l+=e,

print(max(d))