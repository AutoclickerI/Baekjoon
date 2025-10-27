[N,K],*b,[S,X,Y]=[[*map(int,i.split())]for i in open(0)]
l=[]
for y in range(N):
    for x in range(N):
        if b[y][x]:l+=(b[y][x],y,x),
l.sort()
for _ in[0]*S:
    t=[]
    for c,y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and b[ny][nx]<1:
                b[ny][nx]=c
                t+=(c,ny,nx),
    l=t
print(b[X-1][Y-1])