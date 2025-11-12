N,*p,R,C=map(int,open(0).read().split())
l=[[0]+p]
v=[N*[0]for _ in[0]*N]
for c,y,x in l:
    (y,x)==(R,C)<exit(print(c))
    for dy,dx in(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N and v[ny][nx]<1:
            v[ny][nx]=1
            l+=(c+1,ny,nx),
print(-1)