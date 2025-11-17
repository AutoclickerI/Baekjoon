N,M=map(int,input().split())
h=0,*map(int,input().split())
deg=[0]*-~N
edges=[[]for _ in[0]*-~N]

t=[map(int,input().split())for _ in[0]*M]
input()
K={*map(int,input().split())}
for s,e in t:
    if h[s]<h[e]and e not in K:
        deg[e]+=1
        edges[s]+=e,
    if h[e]<h[s]and s not in K:
        deg[s]+=1
        edges[e]+=s,

*K,=K

for n in K:
    for e in edges[n]:
        deg[e]-=1
        if deg[e]<1:K+=e,

if any(deg):
    print('flood')
else:
    print('no flood')