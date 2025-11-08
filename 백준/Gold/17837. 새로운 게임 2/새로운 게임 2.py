N,K=map(int,input().split())
b=[input()[::2]for _ in[0]*N]
v=[[[]for _ in[0]*N]for _ in[0]*N]
for i in range(K):
    y,x,d=map(int,input().split())
    v[y-1][x-1]+=(i,d-1),

def getpos(i):
    for y in range(N):
        for x in range(N):
            for z in range(len(v[y][x])):
                if v[y][x][z][0]==i:
                    return y,x,z

def gettype(y,x):
    if 0<=ny<N and 0<=nx<N:
        if b[ny][nx]=='0':
            return 0
        if b[ny][nx]=='1':
            return 1
    return 2
T=0
while T<1001:
    T+=1
    for i in range(K):
        y,x,z=getpos(i)
        mv=v[y][x][z:]
        del v[y][x][z:]
        d=mv[0][1]
        dy,dx=[(0,1),(0,-1),(-1,0),(1,0)][d]
        ny,nx=y+dy,x+dx
        if gettype(ny,nx)==0:
            v[ny][nx]+=mv
        if gettype(ny,nx)==1:
            v[ny][nx]+=mv[::-1]
        if gettype(ny,nx)==2:
            mv[0]=(mv[0][0],mv[0][1]^1)
            dy,dx=[(0,1),(0,-1),(-1,0),(1,0)][d^1]
            ny,nx=y+dy,x+dx
            if gettype(ny,nx)==0:
                v[ny][nx]+=mv
            if gettype(ny,nx)==1:
                v[ny][nx]+=mv[::-1]
            if gettype(ny,nx)==2:
                v[y][x]+=mv
        if gettype(ny,nx)!=2 and 3<len(v[ny][nx]):
            break
    else:
        continue
    break
if 1000<T:
    print(-1)
else:
    print(T)