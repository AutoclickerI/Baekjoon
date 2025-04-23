R,C,E,N=map(int,input().split())

b=[[*map(int,input().split())]for _ in[0]*R]

for _ in[0]*N:
    y,x,d=map(int,input().split())
    nv=max(b[i-1][j-1]for i in range(y,y+3)for j in range(x,x+3))-d
    for i in range(y,y+3):
        for j in range(x,x+3):
            b[i-1][j-1]=min(nv,b[i-1][j-1])

print(sum(max(0,E-b[i][j])for i in range(R)for j in range(C))*5184)