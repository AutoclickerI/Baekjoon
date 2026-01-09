N,M=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
b=[input()for _ in[0]*N]
from collections import*
dq=deque([[x1-1,y1-1,1]])
v=[M*[0]for _ in[0]*N]

while dq:
    y,x,c=dq.popleft()
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1:
            f='0'<b[ny][nx]
            v[ny][nx]=c+f
            if f:
                dq+=(ny,nx,c+1),
            else:
                dq.appendleft((ny,nx,c))
print(v[x2-1][y2-1])