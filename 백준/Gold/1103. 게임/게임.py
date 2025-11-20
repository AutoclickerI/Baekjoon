N,M=map(int,input().split())
b=[input()for _ in[0]*N]
v=[M*[-float('inf')]for _ in[0]*N]
v[0][0]=1

for _ in range(N*M):
    for y in range(N):
        for x in range(M):
            if 0<=v[y][x]:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy*int(b[y][x]),x+dx*int(b[y][x])
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<v[y][x]+1 and b[ny][nx]!='H':
                        v[ny][nx]=v[y][x]+1
try:
    for y in range(N):
        for x in range(M):
            if 0<=v[y][x]:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy*int(b[y][x]),x+dx*int(b[y][x])
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<v[y][x]+1 and b[ny][nx]!='H':
                        print(-1)
                        raise
    print(max(sum(v,[])))
except:
    pass