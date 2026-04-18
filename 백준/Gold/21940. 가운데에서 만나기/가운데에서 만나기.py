[N,M],*l,_,C=[map(int,i.split())for i in open(0)]

N+=1

d=[N*[float('inf')]for _ in[0]*N]
for i in range(N):d[i][i]=0
for s,e,t in l:d[s][e]=min(d[s][e],t)

for m in range(N):
    for s in range(N):
        for e in range(N):
            d[s][e]=min(d[s][e],d[s][m]+d[m][e])

for i in range(N):d[i][i]=float('inf')

v=[0]*N

for i in C:
    for j in range(N):
        if d[j][i]+d[i][j]!=float('inf'):
            v[j]=max(v[j],d[j][i]+d[i][j])

m=min(filter(int,v))

for i in range(N):
    if v[i]==m:print(i)