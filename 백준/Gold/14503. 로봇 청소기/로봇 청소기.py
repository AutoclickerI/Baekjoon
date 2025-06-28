def clean(y,x,d):
    while 1:
        v[y][x]=1
        f=0
        for dy,dx in(-1,0),(0,1),(0,-1),(1,0):
            ny,nx=y+dy,x+dx
            f|=0<=ny<N and 0<=nx<M and b[ny][nx]<1 and v[ny][nx]<1
        if f:
            d=(d-1)%4
            dy,dx=((-1,0),(0,1),(1,0),(0,-1))[d]
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and b[ny][nx]<1 and v[ny][nx]<1:
                y,x=ny,nx
        else:
            dy,dx=((-1,0),(0,1),(1,0),(0,-1))[d^2]
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<M and b[ny][nx]<1:
                y,x=ny,nx
            else:
                return
            

N,M=map(int,input().split())
r,c,d=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
v=[M*[0]for _ in[0]*N]
clean(r,c,d)
print(sum(sum(v,[])))