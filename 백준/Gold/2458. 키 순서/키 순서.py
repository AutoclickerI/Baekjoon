[N,M],*l=[map(int,i.split())for i in open(0)]

v=[N*[0]for _ in[0]*N]

for s,e in l:
    v[s-1][e-1]=1

for i in range(N):
    v[i][i]=1

for m in range(N):
    for s in range(N):
        for e in range(N):
            v[s][e]|=v[s][m]&v[m][e]

cnt=0
for s in range(N):
    cnt+=all(v[s][e] or v[e][s]for e in range(N))
        
print(cnt)