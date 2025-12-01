N,M=map(int,input().split())
l=[input()for _ in[0]*N]
v=[M*[0]for _ in[0]*N]
cnt=0
def DFS(y,x,py,px,c):
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if(ny,nx)==(py,px):continue
        if 0<=ny<N and 0<=nx<M and l[ny][nx]==c:
            if v[ny][nx]<1:
                v[ny][nx]=cnt
                DFS(ny,nx,y,x,c)
            elif v[ny][nx]==cnt:
                exit(print('Yes'))

for y in range(N):
    for x in range(M):
        if v[y][x]<1:
            cnt+=1
            DFS(y,x,y,x,l[y][x])
print('No')