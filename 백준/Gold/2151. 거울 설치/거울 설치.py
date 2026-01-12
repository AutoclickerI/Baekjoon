N=int(input())
b=[input()for _ in[0]*N]
(y,x),(ye,xe)=[(y,x)for y in range(N)for x in range(N)if b[y][x]=='#']
l=[(y,x,0,dy,dx)for dy,dx in[(-1,0),(1,0),(0,1),(0,-1)]]
v=[[[3*[1e9]for _ in[0]*3]for _ in[0]*N]for _ in[0]*N]

for y,x,c,dy,dx in l:
    if b[y][x]=='*':continue
    for ddy,ddx in(dy,dx),*[(dx,dy),(-dx,-dy)]*(b[y][x]=='!'):
        ny,nx=y+ddy,x+ddx
        if 0<=ny<N and 0<=nx<N and c+((dy,dx)!=(ddy,ddx))<v[ny][nx][ddy][ddx]:
            v[ny][nx][ddy][ddx]=c+((dy,dx)!=(ddy,ddx))
            l+=(ny,nx,c+((dy,dx)!=(ddy,ddx)),ddy,ddx),
print(min(sum(v[ye][xe],[])))