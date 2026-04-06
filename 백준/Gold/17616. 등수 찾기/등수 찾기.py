[N,M,X],*l=[map(int,i.split())for i in open(0)]
b=[N*[0]for _ in[0]*N]

for s,e in l:
    b[s-1][e-1]=1
    b[e-1][s-1]=-1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if b[s][m]==b[m][e]!=0:
                b[s][e]=b[s][m]

n,z,p=map(b[X-1].count,[-1,0,1])
print(N-(z+p)+1,n+z)