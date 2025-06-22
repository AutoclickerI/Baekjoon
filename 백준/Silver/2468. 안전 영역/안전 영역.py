import sys
sys.setrecursionlimit(9**9)


def DFS(v,b,y,x):
    if b[y][x]<1 and v[y][x]<1:
        v[y][x]=1
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<1:
                DFS(v,b,ny,nx)
        return 1
    return 0

def chk(b):
    c=0
    v=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):c+=DFS(v,b,y,x)
    return c

def fill(b,t):
    return[[j<t for j in i]for i in b]

N=int(input())
b=[[*map(int,input().split())]for _ in[0]*N]

m=0
for i in range(99):
    m=max(m,chk(fill(b,i)))

print(m)