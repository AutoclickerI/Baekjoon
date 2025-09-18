import sys
sys.setrecursionlimit(2*10**5)

N,M=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

def DFS(y,x):
    v[y][x]=1
    c=1
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1<=b[ny][nx]:
            c+=DFS(ny,nx)
    return c
i=0
while 1:
    i+=1
    cnt=[M*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(M):
            if b[y][x]:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<M and b[ny][nx]<1:
                        cnt[y][x]+=1
    f=n=0
    for y in range(N):
        for x in range(M):
            b[y][x]=max(0,b[y][x]-cnt[y][x])
            n+=0<b[y][x]
    n<1<exit(print(0))
    v=[M*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(M):
            if b[y][x] and v[y][x]<1 and n!=DFS(y,x):exit(print(i))