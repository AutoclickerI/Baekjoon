t=[1001*[0]for _ in[0]*1001]

t[0][0]=1
for i in range(1,1001):
    for j in range(1,1001):
        t[i][j]+=t[i-1][j-1]+t[i-2][j-1]+t[i-3][j-1]

for i in[*open(0)][1:]:
    n,m=map(int,i.split())
    print(t[n][m]%(10**9+9))