from collections import deque

for _ in[0]*int(input()):
    n=int(input())
    y,x=map(int,input().split())
    dq=deque([(0,y,x)])
    v=[n*[0]for _ in[0]*n]
    v[y][x]=1
    ey,ex=map(int,input().split())
    while 1:
        c,y,x=dq.popleft()
        if(y,x)==(ey,ex):break
        for dy,dx in(-1,2),(1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1):
            ny=y+dy;nx=x+dx
            if 0<=ny<n and 0<=nx<n and v[ny][nx]<1:
                v[ny][nx]=1
                dq+=(c+1,ny,nx),
    print(c)