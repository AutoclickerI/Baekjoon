N,M=map(int,input().split())
K,C=map(int,input().split())
b=[input()for _ in[0]*N]
for y in range(N):
    for x in range(M):
        if b[y][x]=='S':
            s=y,x

v=[[100*[10**18]for _ in[0]*M]for _ in[0]*N]
from collections import deque
dq=deque([[*s,0,0]])
v[s[0]][s[1]][0]=0
while dq:
    y,x,c,idx=dq.popleft()
    if v[y][x][c]<idx:
        continue
    if b[y][x]=='E':
        print(idx)
        break
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1),(0,0):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and b[ny][nx]!='#':
            nc=max(c-K,0)if b[ny][nx]=='H'else c+C
            if nc<100 and idx+1<v[ny][nx][nc]:
                v[ny][nx][nc]=idx+1
                dq.append([ny,nx,nc,idx+1])
else:
    print(-1)