[N],*b=[[*map(int,i.split())]for i in open(0)]
v=[N*[0]for _ in[0]*N]
l=[(0,0)]
for y,x in l:
    for dy,dx in(1,0),(0,1):
        ny,nx=y+dy*b[y][x],x+dx*b[y][x]
        if 0<=ny<N and 0<=nx<N and v[ny][nx]<1:
            v[ny][nx]=1
            l+=(ny,nx),
print(['Hing','HaruHaru'][v[-1][-1]])