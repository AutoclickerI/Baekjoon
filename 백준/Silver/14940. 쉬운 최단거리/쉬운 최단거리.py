n,m=map(int,input().split())
b=[input()[::2]for _ in[0]*n]

from collections import deque

dq=deque()
visited=[m*[0]for _ in[0]*n]

for y in range(n):
    for x in range(m):
        if b[y][x]=='2':
            dq+=(y,x,0),
        if b[y][x]=='1':
            visited[y][x]=-1

while dq:
    y,x,c=dq.popleft()
    for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and b[ny][nx]=='1'and visited[ny][nx]<1:
            visited[ny][nx]=c+1
            dq+=(ny,nx,c+1),

for i in visited:print(*i)