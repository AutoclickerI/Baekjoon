[N,M],*l=[map(int,i.split())for i in open(0)]
nn=[N*[0]for _ in[0]*N]
for s,e in l:nn[s-1][e-1]=nn[e-1][s-1]=1
r=0
for i in range(N):
    for j in range(i+1,N):
        if nn[i][j]<1:
            for k in range(j+1,N):r+=nn[i][k]+nn[j][k]<1
print(r)