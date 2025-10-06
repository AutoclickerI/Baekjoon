[N],*l=[[*map(int,i.split())]for i in open(0)]

b=[N*[1]for _ in[0]*N]

for y,x in sorted([(y,x)for y in range(N)for x in range(N)],key=lambda i:l[i[0]][i[1]]):
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N and l[y][x]<l[ny][nx]:
            b[ny][nx]=max(b[ny][nx],b[y][x]+1)
print(max(sum(b,[])))