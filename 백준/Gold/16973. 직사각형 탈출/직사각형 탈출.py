[N,M],*b,[H,W,Sr,Sc,Fr,Fc]=[map(int,i.split())for i in open(0)]

ps=[[0]*-~M]
for i in b:
    t=[0]
    for j,v in enumerate(i):
        t+=t[-1]+v+ps[-1][j+1]-ps[-1][j],
    ps+=t,

def check(y,x):
    if H<=y+H<=N and W<=x+W<=M:
        return ps[y+H][x+W]-ps[y+H][x]-ps[y][x+W]+ps[y][x]<1
    return 0

v=[M*[float('inf')]for _ in[0]*N]
v[Sr-1][Sc-1]=0
l=[(Sr-1,Sc-1,0)]
F=Fr-1,Fc-1
for y,x,c in l:
    if (y,x)==F:
        print(c)
        break
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if check(ny,nx) and c+1<v[ny][nx]:
            v[ny][nx]=c+1
            l+=(ny,nx,c+1),
else:
    print(-1)