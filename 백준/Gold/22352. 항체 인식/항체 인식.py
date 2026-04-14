[N,M],*b=[[*map(int,i.split())]for i in open(0)]
b1=b[:N]
b2=b[N:]
l=[]
for y in range(N):
    for x in range(M):
        if b1[y][x]!=b2[y][x]:
            l=[(y,x)]
if[]==l:
    exit(print('YES'))

v=[M*[0]for _ in[0]*N]
for y,x in l:
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b1[ny][nx]==b1[y][x]:
            v[ny][nx]=1
            l+=(ny,nx),

for y,x in l:
    b1[y][x]=b2[l[0][0]][l[0][1]]

if b1==b2:
    print('YES')
else:
    print('NO')