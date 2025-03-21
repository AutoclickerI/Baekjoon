N,M=map(int,input().split())

b=[input().split()for _ in[0]*N]

z=[]
bi=[]

for y in range(N):
    for x in range(M):
        if b[y][x]=='0':
            z+=(y,x),
        if b[y][x]=='2':
            bi+=(y,x),

from collections import deque
def BFS(l):
    dq=deque(bi)
    visited=[M*[1]for _ in[0]*N]
    for y,x in z:visited[y][x]=0
    for y,x in l:visited[y][x]=1
    while dq:
        y,x=dq.popleft()
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and visited[ny][nx]<1 and b[ny][nx]=='0':
                visited[ny][nx]=1
                dq+=(ny,nx),
    return sum(M-sum(i)for i in visited)
    

from itertools import combinations

m=0
for l in combinations(z,3):
    for y,x in l:
        b[y][x]='1'
    m=max(m,BFS(l))
    for y,x in l:
        b[y][x]='0'
print(m)