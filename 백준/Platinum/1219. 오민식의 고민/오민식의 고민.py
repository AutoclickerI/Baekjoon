[N,ss,ee,M],*l,c=[[*map(int,i.split())]for i in open(0)]
v=[N*[-float('inf')]for _ in[0]*N]
for i in range(N):v[i][i]=0
for s,e,p in l:
    v[s][e]=max(v[s][e],c[e]-p)

for m in range(N):
    for s in range(N):
        for e in range(N):
            v[s][e]=max(v[s][e],v[s][m]+v[m][e])

vt=[i[:]for i in v]

for m in range(N):
    for s in range(N):
        for e in range(N):
            v[s][e]=max(v[s][e],v[s][m]+v[m][e])

for y in range(N):
    for x in range(N):
        if vt[y][x]<v[y][x]:
            v[y][x]=float('inf')

for m in range(N):
    for s in range(N):
        for e in range(N):
            v[s][e]=max(v[s][e],v[s][m]+v[m][e])

if v[ss][ee]==float('inf'):
    print('Gee')
elif v[ss][ee]==-float('inf'):
    print('gg')
else:
    print(v[ss][ee]+c[ss])