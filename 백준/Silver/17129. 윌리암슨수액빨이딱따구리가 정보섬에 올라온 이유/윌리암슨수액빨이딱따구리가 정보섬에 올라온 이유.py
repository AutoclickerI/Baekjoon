from collections import*

N,M=map(int,input().split())
b=[input()for _ in[0]*N]
v=[M*[0]for _ in[0]*N]

for y in range(N):
    for x in range(M):
        if b[y][x]=='2':
            dq=deque([(0,y,x)])
            v[y][x]=1

while dq:
    c,y,x=dq.popleft()
    if '2'<b[y][x]:
        exit(print('TAK',c))
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1:
            if b[ny][nx]!='1':
                v[ny][nx]=1
                dq+=(c+1,ny,nx),
print('NIE')