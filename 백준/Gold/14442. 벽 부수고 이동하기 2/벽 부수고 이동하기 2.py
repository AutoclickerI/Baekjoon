N,M,K=map(int,input().split())

b=[input()for _ in[0]*N]

v=[[-~K*[float('inf')]for _ in[0]*M]for _ in[0]*N]

v[0][0][b[0][0]=='1']=0

from collections import deque

dq=deque([(0,0,0,0)])

while dq:
    y,x,k,c=dq.popleft()
    if v[y][x][k]<c:
        continue
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=nx<M and 0<=ny<N:
            if b[ny][nx]=='0'and c+1<v[ny][nx][k]:
                v[ny][nx][k]=c+1
                dq+=(ny,nx,k,c+1),
            if b[ny][nx]=='1'and k+1<=K and c+1<v[ny][nx][k+1]:
                v[ny][nx][k+1]=c+1
                dq+=(ny,nx,k+1,c+1),

z=min(v[-1][-1])+1
print(-(z==float('inf'))or z)