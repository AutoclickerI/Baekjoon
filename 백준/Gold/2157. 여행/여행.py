[N,M,K],*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*N]
for s,e,c in l:
    if s<e:
        edges[s-1]+=(e-1,c),

v=[M*[-float('inf')]for _ in[0]*N]
v[0]=[0]*M
for i in range(N):
    for e,c in edges[i]:
        for j in range(M-1):
            v[e][j+1]=max(v[e][j+1],v[i][j]+c)

print(max(v[-1]))