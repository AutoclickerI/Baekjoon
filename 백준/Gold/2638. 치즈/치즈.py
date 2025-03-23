N,M=map(int,input().split())

b=[input().split()for _ in[0]*N]

from collections import deque

def BFS():
    visited=[M*[0]for _ in[0]*N]
    dq=deque()
    for i in range(N):
        if b[i][0]=='0':
            dq+=(i,0),
            visited[i][0]=1
        if b[i][M-1]=='0':
            dq+=(i,M-1),
            visited[i][M-1]=1
    for i in range(1,M-1):
        if b[0][i]=='0':
            dq+=(0,i),
            visited[0][i]=1
        if b[N-1][i]=='0':
            dq+=(N-1,i),
            visited[N-1][i]=1
    while dq:
        y,x=dq.popleft()
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny=y+dy;nx=x+dx
            if 0<=ny<N and 0<=nx<M:
                if b[ny][nx]=='0':
                    if visited[ny][nx]<1:
                        dq+=(ny,nx),
                        visited[ny][nx]=1
                else:
                    visited[ny][nx]+=1
    for y in range(N):
        for x in range(M):
            if visited[y][x]>1:
                b[y][x]='0'

a=0
while 1:
    f=0
    for y in range(N):
        for x in range(M):
            f|=b[y][x]=='1'
    if f<1:
        break
    BFS()
    a+=1
print(a)