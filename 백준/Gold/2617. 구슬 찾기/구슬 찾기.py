[N,M],*l=[map(int,i.split())for i in open(0)]

x=[N*[0]for _ in[0]*N]

for s,e in l:
    x[s-1][e-1]=1
    x[e-1][s-1]=-1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if x[s][m]==x[m][e]!=0:
                x[s][e]|=x[s][m]

cnt=0
for i in range(N):
    o=x[i].count(1)
    m=x[i].count(-1)
    if N//2<max(o,m):
        cnt+=1
print(cnt)