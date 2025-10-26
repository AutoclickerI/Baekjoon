N,M=map(int,input().split())
b=[input()for _ in[0]*M]
v=[N*[0]for _ in[0]*M]
def DFS(y,x,c):
    a=1
    v[y][x]=1
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<M and 0<=nx<N and v[ny][nx]<1 and b[ny][nx]==c:
            a+=DFS(ny,nx,c)
    return a
l=[0,0]
for y in range(M):
    for x in range(N):
        if v[y][x]<1:
            l[b[y][x]=='B']+=DFS(y,x,b[y][x])**2
print(*l)