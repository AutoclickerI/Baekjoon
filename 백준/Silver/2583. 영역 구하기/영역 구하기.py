import sys

sys.setrecursionlimit(2*10**5)
#input=sys.stdin.readline

(M,N,_),*l=[map(int,i.split())for i in open(0)]

z=[N*[1]for _ in[0]*M]

for a,b,c,d in l:
    for x in range(a,c):
        for y in range(b,d):
            z[y][x]=0

def DFS(y,x):
    z[y][x]=0
    r=1
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<M and 0<=nx<N and z[ny][nx]:r+=DFS(ny,nx)
    return r

l=[]
for y in range(M):
    for x in range(N):
        if z[y][x]:l+=DFS(y,x),

print(len(l),*sorted(l))