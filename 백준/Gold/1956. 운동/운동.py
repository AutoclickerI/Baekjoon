[V,E],*l=[map(int,i.split())for i in open(0)]

v=[V*[float('inf')]for _ in[0]*V]

for s,e,c in l:v[s-1][e-1]=c

for m in range(V):
    for s in range(V):
        for e in range(V):
            v[s][e]=min(v[s][e],v[s][m]+v[m][e])

m=min(v[i][i]for i in range(V))
print(-(m==float('inf'))or m)