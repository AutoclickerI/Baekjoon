N=int(input())
b=[input()for _ in[0]*N]
B=[]
E=[]
for y in range(N):
    for x in range(N):
        if b[y][x]=='B':B+=(y,x),
        if b[y][x]=='E':E+=(y,x),
s=*B[1],B[0][1]==B[1][1]
e=*E[1],E[0][1]==E[1][1]
v=[[2*[0]for _ in[0]*N]for _ in[0]*N]
l=[(0,*s)]
def check(y,x,r):
    if 0<=x<N and 0<=y<N:
        if r==0 and 0<x<N-1:
            for nx in x-1,x,x+1:
                if b[y][nx]=='1':
                    return 0
            return 1
        if r==1 and 0<y<N-1:
            for ny in y-1,y,y+1:
                if b[ny][x]=='1':
                    return 0
            return 1
    return 0
for c,y,x,r in l:
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if check(ny,nx,r)and v[ny][nx][r]<1:
            v[ny][nx][r]=c+1
            l+=(c+1,ny,nx,r),
    nr=r^1
    if check(y-1,x,0)and check(y,x,0)and check(y+1,x,0)and v[y][x][nr]<1:
        v[y][x][nr]=c+1
        l+=(c+1,y,x,nr),

print(v[e[0]][e[1]][e[2]])