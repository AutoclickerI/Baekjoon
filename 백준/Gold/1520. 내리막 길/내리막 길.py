import sys
sys.setrecursionlimit(9**9)

M,N=map(int,input().split())

b=[[*map(int,input().split())]for _ in[0]*M]

val=[N*[0]for _ in[0]*M]

def DFS(y,x):
    val[y][x]=1
    for dy,dx in(0,-1),(0,1),(1,0),(-1,0):
        if 0<=x+dx<N and 0<=y+dy<M and b[y+dy][x+dx]<b[y][x] and val[y+dy][x+dx]<1:
            DFS(y+dy,x+dx)

DFS(0,0)

edges=[[]for _ in[0]*M*N]
deg=[0]*M*N

a=[0]*M*N

for y in range(M):
    for x in range(N):
        for dy,dx in(0,-1),(0,1),(1,0),(-1,0):
            n=y*N+x;nn=(y+dy)*N+x+dx
            if 0<=x+dx<N and 0<=y+dy<M and b[y+dy][x+dx]<b[y][x] and val[y][x]:
                edges[n]+=nn,
                deg[nn]+=1

from collections import deque

dq=deque([0])
a[0]=1

while dq:
    n=dq.popleft()
    for e in edges[n]:
        a[e]+=a[n]
        deg[e]-=1
        if deg[e]<1:
            dq+=e,

print(a[-1])