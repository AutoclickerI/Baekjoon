[N,M],*l=[map(int,i.split())for i in open(0)]

b=[N*[float('inf')]for _ in[0]*N]
for i in range(N):b[i][i]=0
for s,e in l:b[s-1][e-1]=b[e-1][s-1]=2
for m in range(N):
    for s in range(N):
        for e in range(N):
            b[s][e]=min(b[s][e],b[s][m]+b[m][e])

m=float('inf')
for i in range(N):
    for j in range(i+1,N):
        nm=sum(map(min,b[i],b[j]))
        if nm<m:
            m=nm
            r=i+1,j+1
print(*r,m)