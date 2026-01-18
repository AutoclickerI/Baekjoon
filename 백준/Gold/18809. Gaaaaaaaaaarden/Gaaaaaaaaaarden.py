[N,M,G,R],*b=[[*map(int,i.split())]for i in open(0)]
p=[]
for y in range(N):
    for x in range(M):
        if b[y][x]==2:
            p+=(y,x),
from itertools import*

m=0
for i in combinations(p,G+R):
    for v in combinations(i,G):
        ng=pg={*v}
        nr=pr={*i}-ng
        v=[M*[0]for _ in[0]*N]
        for y,x in i:v[y][x]=1
        c=0
        while ng and nr:
            tg=set()
            tr=set()
            for y,x in ng:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b[ny][nx]:
                        tg|={(ny,nx)}
            for y,x in nr:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b[ny][nx]:
                        tr|={(ny,nx)}
            fl=tg&tr
            c+=len(fl)
            for y,x in*tg,*tr:
                v[y][x]=1
            ng=tg-fl
            nr=tr-fl
        m=max(m,c)
print(m)