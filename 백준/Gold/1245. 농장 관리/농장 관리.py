[N,M],*b=[[*map(int,i.split())]for i in open(0)]

def DFS(y,x):
    f=1
    v[y][x]=1
    for dy in-1,0,1:
        for dx in-1,0,1:
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M:
                if b[y][x]<b[ny][nx]:
                    f=0
                if b[y][x]==b[ny][nx]and v[ny][nx]<1:
                    f&=DFS(ny,nx)
    return f

v=[M*[0]for _ in[0]*N]
r=0
for y in range(N):
    for x in range(M):
        if v[y][x]<1:
            r+=DFS(y,x)
print(r)