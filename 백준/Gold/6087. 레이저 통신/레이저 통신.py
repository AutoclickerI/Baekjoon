W,H=map(int,input().split())
b=[input()for _ in[0]*H]

l=[]
for y in range(H):
    for x in range(W):
        if b[y][x]=='C':
            l+=(y,x),

e=l.pop()

v=[[4*[float('inf')]for _ in[0]*W]for _ in[0]*H]

from collections import deque
dq=deque([(*l[0],i,1)for i in range(4)])

while dq:
    y,x,d,c=dq.popleft()
    if(y,x)==e:print(c-1);break
    dy,dx=[(0,1),(1,0),(0,-1),(-1,0)][d]
    ny,nx=y+dy,x+dx
    if 0<=ny<H and 0<=nx<W and c<v[ny][nx][d] and b[ny][nx]!='*':
        v[ny][nx][d]=c
        dq.appendleft((ny,nx,d,c))
    for dd in 1,3:
        nd=d+dd&3
        if c+1<v[y][x][nd]:
            v[y][x][nd]=c+1
            dq.append((y,x,nd,c+1))