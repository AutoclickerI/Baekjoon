[N,M],*l=[map(int,i.split())for i in open(0)]
v=[N*[float('inf')]for _ in[0]*N]
p=[[[]for _ in[0]*N]for _ in[0]*N]
for s,e,c in l:
    s-=1
    e-=1
    if c<v[s][e]:
        v[s][e]=v[e][s]=c
        p[s][e]=[s,e]
        p[e][s]=[e,s]
for i in range(N):
    v[i][i]=0
    p[i][i]=[i]

for m in range(N):
    for s in range(N):
        for e in range(N):
            if v[s][m]+v[m][e]<v[s][e]:
                v[s][e]=v[s][m]+v[m][e]
                p[s][e]=p[s][m]+p[m][e][1:]

for i in p:print(*[1+j[1]if 1<len(j)else'-'for j in i])