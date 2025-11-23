[N,M],*b=[[*map(int,i.split())]for i in open(0)]

cnt0=0
c=[]
for y in range(N):
    for x in range(N):
        if 1<b[y][x]:
            b[y][x]=0
            c+=(y,x),
        if b[y][x]<1:cnt0+=1
def BFS(l):
    v=[N*[0]for _ in[0]*N]
    cnt=0
    for y,x in l:
        v[y][x]=1
        cnt+=1
    l=[(0,y,x)for y,x in l]
    for c,y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and b[ny][nx]<1:
                v[ny][nx]=1
                cnt+=1
                l+=(c+1,ny,nx),
    if cnt==cnt0:
        return c
    else:
        return -1
from itertools import*
r=[]
for i in combinations(c,M):
    a=BFS(i)
    if 0<=a:
        r+=a,
print(-(r==[])or min(r))