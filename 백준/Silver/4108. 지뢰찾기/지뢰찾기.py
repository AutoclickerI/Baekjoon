while 1:
    R,C=map(int,input().split())
    if R==C==0:break
    b=[input()for _ in[0]*R]
    v=[C*['*']for _ in[0]*R]
    for y in range(R):
        for x in range(C):
            if b[y][x]=='*':
                continue
            v[y][x]=0
            for dy in-1,0,1:
                for dx in-1,0,1:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<R and 0<=nx<C:
                        v[y][x]+=b[ny][nx]=='*'
    for i in v:
        print(*i,sep='')