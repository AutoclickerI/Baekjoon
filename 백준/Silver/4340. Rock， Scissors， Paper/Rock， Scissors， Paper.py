for _ in[0]*int(input()):
    r,c,n=map(int,input().split())
    b=[[*input()]for _ in[0]*r]
    for _ in[0]*n:
        nb=[i[:]for i in b]
        for y in range(r):
            for x in range(c):
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<r and 0<=nx<c and b[y][x]+b[ny][nx]in'RP PS SR':
                        nb[y][x]='RPS'['SR'.find(b[y][x])]
        b=nb
    for i in b:print(*i,sep='')
    print()