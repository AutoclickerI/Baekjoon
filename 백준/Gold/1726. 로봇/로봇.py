[M,N]=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*M]
*s,=map(int,input().split())
*e,=map(int,input().split())

v=[[4*[float('inf')]for _ in[0]*N]for _ in[0]*M]
for i in range(3):
    e[i]-=1
    s[i]-=1
s[-1]=[0,2,1,3][s[-1]]
e[-1]=[0,2,1,3][e[-1]]
y,x,d=s
v[y][x][d]=0
from heapq import*
hq=[(0,*s)]
while hq:
    c,y,x,d=heappop(hq)
    if v[y][x][d]<c:continue
    if[y,x,d]==e:break
    for nn,dd in(1,0),(2,0),(3,0),(0,1),(0,3):
        dy,dx=[(0,1),(1,0),(0,-1),(-1,0)][d]
        ny,nx,nd=y+nn*dy,x+nn*dx,d+dd&3
        if 0<=ny<M and 0<=nx<N and max(b[y+dy*i][x+dx*i]for i in range(nn+1))<1 and c+1<v[ny][nx][nd]:
            v[ny][nx][nd]=c+1
            heappush(hq,(c+1,ny,nx,nd))
print(c)