N,M=map(int,input().split())
b=[input()for _ in[0]*N]

def step(y,x):
    global m
    l=[(1,y,x)]
    v=[M*[0]for _ in[0]*N]
    v[y][x]=1
    for c,y,x in l:
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b[ny][nx]=='L':
                v[ny][nx]=1
                m=max(m,c)
                l+=(c+1,ny,nx),

m=0

for y in range(N):
    for x in range(M):
        if b[y][x]=='L':step(y,x)

print(m)