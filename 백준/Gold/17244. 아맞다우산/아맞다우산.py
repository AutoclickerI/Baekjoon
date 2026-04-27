N,M=map(int,input().split())
b=[input()for _ in[0]*M]

I=[N*[-1]for _ in[0]*M]
K=0

for y in range(M):
    for x in range(N):
        if b[y][x]=='S':
            sy,sx=y,x
        elif b[y][x]=='E':
            ey,ex=y,x
        elif b[y][x]=='X':
            I[y][x]=K
            K+=1

T=(1<<K)-1
v=[[[0]*(1<<K)for _ in[0]*N]for _ in[0]*M]
v[sy][sx][0]=1

l=[(sy,sx,0,0)]

for y,x,m,c in l:
    if(y,x,m)==(ey,ex,T):
        exit(print(c))
    
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<M and 0<=nx<N and b[ny][nx]!='#':
            nm=m
            if 0<=I[ny][nx]:
                nm|=1<<I[ny][nx]
            if v[ny][nx][nm]<1:
                v[ny][nx][nm]=1
                l+=(ny,nx,nm,c+1),