[N],*b=[[*map(int,i.split())]for i in open(0)]

v=[N*[0]for _ in[0]*N]
t=[]
for y in range(N):
    for x in range(N):
        if v[y][x]<1 and b[y][x]:
            v[y][x]=1
            l=[(y,x)]
            for cy,cx in l:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and b[ny][nx]:
                        v[ny][nx]=1
                        l+=(ny,nx),
            t+=l,

total={*sum(t,[])}
m=1e9
for i in t:
    nt=total-{*i}
    for y,x in i:
        for ny,nx in nt:
            m=min(m,abs(y-ny)+abs(x-nx))
print(m-1)