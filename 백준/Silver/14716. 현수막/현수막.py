[M,N],*b=[[*map(int,i.split())]for i in open(0)]
v=[N*[0]for _ in[0]*M]
c=0
def BFS(y,x):
    l=[(y,x)]
    for y,x in l:
        for dy in-1,0,1:
            for dx in-1,0,1:
                ny,nx=y+dy,x+dx
                if 0<=ny<M and 0<=nx<N and b[ny][nx]and v[ny][nx]<1:
                    v[ny][nx]=1
                    l+=(ny,nx),
for y in range(M):
    for x in range(N):
        if v[y][x]<1 and b[y][x]:
            c+=1
            BFS(y,x)
print(c)