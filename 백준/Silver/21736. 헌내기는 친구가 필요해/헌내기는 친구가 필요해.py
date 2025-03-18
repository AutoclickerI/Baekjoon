N,M=map(int,input().split())
b=[input()for _ in[0]*N]

visited=[M*[0]for _ in[0]*N]

from collections import deque

dq=deque()

for y in range(N):
    for x in range(M):
        if b[y][x]=='I':
            dq+=(y,x),

while dq:
    y,x=dq.popleft()
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny=y+dy;nx=x+dx
        if 0<=ny<N and 0<=nx<M and b[ny][nx]!='X' and visited[ny][nx]<1:
            visited[ny][nx]=1
            dq+=(ny,nx),

s=0
for y in range(N):
    for x in range(M):
        s+=b[y][x]=='P'*(visited[y][x])

print(s or'TT')