N,M=map(int,input().split())
b=[[*map(int,input())]for _ in[0]*N]

v=[M*[float('inf')]for _ in[0]*N]
l=[]
for y in range(N):
    for x in range(M):
        if y in(0,N-1)or x in(0,M-1):
            v[y][x]=b[y][x]
            l+=(y,x,b[y][x]),

for y,x,f in l:
    if v[y][x]<f:
        continue
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and max(f,b[ny][nx])<v[ny][nx]:
            v[ny][nx]=max(f,b[ny][nx])
            l+=(ny,nx,v[ny][nx]),
print(sum(v[y][x]-b[y][x]for y in range(N)for x in range(M)))