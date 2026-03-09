[N,K],*b=[[*map(int,i.split())]for i in open(0)]

def btype(y,x):
    if 0<=y<N and 0<=x<N:
        return b[y][x]
    return 2

p=[[[]for _ in[0]*N]for _ in[0]*N]
i=0
pmap={}
for y,x,d in b[N:]:
    p[y-1][x-1]+=[i,d-1],
    pmap[i]=y-1,x-1
    i+=1

for t in range(1,1001):
    for i in range(K):
        y,x=pmap[i]
        n,d=p[y][x][0]
        if n==i:
            dy,dx=[(0,1),(0,-1),(-1,0),(1,0)][d]
            ny,nx=y+dy,x+dx
            tt=btype(ny,nx)
            if tt<2:
                for i,_ in p[y][x]:
                    pmap[i]=ny,nx
                p[ny][nx]+=p[y][x][::-tt|1]
                if 3<len(p[ny][nx]):exit(print(t))
                p[y][x]=[]
            else:
                p[y][x][0][1]^=1
                n,d=p[y][x][0]
                dy,dx=[(0,1),(0,-1),(-1,0),(1,0)][d]
                ny,nx=y+dy,x+dx
                tt=btype(ny,nx)
                if tt<2:
                    for i,_ in p[y][x]:
                        pmap[i]=ny,nx
                    p[ny][nx]+=p[y][x][::-tt|1]
                    if 3<len(p[ny][nx]):exit(print(t))
                    p[y][x]=[]
print(-1)