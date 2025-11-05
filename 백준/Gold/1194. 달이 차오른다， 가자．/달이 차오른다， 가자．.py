N,M=map(int,input().split())
b=[input()for _ in[0]*N]

for y in range(N):
    for x in range(M):
        if b[y][x]=='0':
            l=[(0,1,y,x)]
            v={(y,x,1)}

for cost,state,y,x in l:
    if b[y][x]=='1':
        exit(print(cost))
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M:
            if'A'<=b[ny][nx]<'G' and ((1<<ord(b[ny][nx])-64)&state)and (ny,nx,state)not in v:
                v|={(ny,nx,state)}
                l+=(cost+1,state,ny,nx),
            if'a'<=b[ny][nx]<'g'and (ny,nx,state|(1<<ord(b[ny][nx])-96))not in v:
                v|={(ny,nx,state|(1<<ord(b[ny][nx])-96))}
                l+=(cost+1,state|(1<<ord(b[ny][nx])-96),ny,nx),
            if b[ny][nx] in'.01'and (ny,nx,state)not in v:
                v|={(ny,nx,state)}
                l+=(cost+1,state,ny,nx),
print(-1)