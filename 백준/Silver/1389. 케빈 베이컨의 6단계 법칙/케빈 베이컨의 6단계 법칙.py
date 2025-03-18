N,M=map(int,input().split())

adj=[N*[1e9]for _ in[0]*N]
for i in range(N):adj[i][i]=0

for _ in[0]*M:
    s,e=map(int,input().split())
    adj[s-1][e-1]=1
    adj[e-1][s-1]=1

for m in range(N):
    for s in range(N):
        for e in range(N):
            adj[s][e]=min(adj[s][e],adj[s][m]+adj[m][e])

m=1e9
for i in range(N):
    v=sum(adj[i])
    if v<m:
        m=v
        idx=i

print(idx+1)