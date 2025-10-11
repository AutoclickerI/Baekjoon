import sys
sys.setrecursionlimit(2*10**5)

N,M,K=map(int,input().split())
b=[M*[0]for _ in[0]*N]

for _ in[0]*K:
    y,x=map(int,input().split())
    b[y-1][x-1]=1

def DFS(y,x):
    f=0
    if b[y][x]:
        b[y][x]=0
        f=1
        for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and b[ny][nx]:
                f+=DFS(ny,nx)
    return f

m=0
for y in range(N):
    for x in range(M):
        m=max(m,DFS(y,x))

print(m)