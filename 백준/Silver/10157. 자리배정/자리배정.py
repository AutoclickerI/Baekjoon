C,R,K=map(int,open(0).read().split())
v=[C*[0]for _ in[0]*R]
y,x=R-1,0
d=0
for cnt in range(C*R):
    v[y][x]=cnt+1
    if cnt==C*R-1:break
    while 1:
        dy,dx=[(-1,0),(0,1),(1,0),(0,-1)][d]
        ny,nx=y+dy,x+dx
        if 0<=ny<R and 0<=nx<C and v[ny][nx]<1:
            break
        d=(d+1)%4
    y,x=ny,nx

if C*R<K:
    print(0)
else:
    for y in range(R):
        for x in range(C):
            if v[y][x]==K:
                print(x+1,R-y)