M,N=map(int,input().split())
b=[input()for _ in[0]*N]
v=[M*[0]for _ in[0]*N]
v[0][0]=1
from collections import deque

dq=deque([(1,0,0)])
while dq:
    c,y,x=dq.popleft()
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1:
            if b[ny][nx]=='0':
                v[ny][nx]=c
                dq.appendleft((c,ny,nx))
            else:
                v[ny][nx]=c+1
                dq+=(c+1,ny,nx),
print(v[-1][-1]-1)