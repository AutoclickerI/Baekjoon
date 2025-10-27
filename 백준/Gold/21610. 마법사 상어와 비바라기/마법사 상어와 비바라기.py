N,M=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
c=[N*[0]for _ in[0]*N]
c[-1][0]=c[-1][1]=c[-2][0]=c[-2][1]=1

for _ in[0]*M:
    d,s=map(int,input().split())
    dy,dx=[0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)][d]
    nc=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if c[y][x]:
                nc[(y+dy*s)%N][(x+dx*s)%N]=1
    for y in range(N):
        for x in range(N):
            if nc[y][x]:
                b[y][x]+=1
    db=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if nc[y][x]:
                for dy,dx in(-1,-1),(-1,1),(1,-1),(1,1):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<N and b[ny][nx]:
                        db[y][x]+=1
    for y in range(N):
        for x in range(N):
            b[y][x]+=db[y][x]
    c=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if nc[y][x]<1 and 1<b[y][x]:
                b[y][x]-=2
                c[y][x]=1
print(sum(sum(i)for i in b))