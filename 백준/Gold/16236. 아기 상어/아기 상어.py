N=int(input())
t=0
size=2
add=0

b=[[*map(int,input().split())]for _ in[0]*N]

for y in range(N):
    for x in range(N):
        if b[y][x]==9:
            py=y
            px=x
            b[y][x]=0

from collections import deque

def getnext(y,x):
    v=[N*[0]for _ in[0]*N]
    dq=deque([(y,x,0)])
    v[y][x]=1
    a=[]
    mc=9e9
    while dq:
        y,x,c=dq.popleft()
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny=y+dy;nx=x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<1:
                if b[ny][nx]<=size:
                    v[ny][nx]=1
                    if 0<b[ny][nx]<size and c<mc:
                        a+=(ny,nx),
                        mc=c+1
                    elif c<mc:
                        dq+=(ny,nx,c+1),
    return min(a),mc

while 1:
    try:
        (py,px),c=getnext(py,px)
        b[py][px]=0
        t+=c
        add+=1
        size,add=size+add//size,add%size
    except:
        break

print(t)