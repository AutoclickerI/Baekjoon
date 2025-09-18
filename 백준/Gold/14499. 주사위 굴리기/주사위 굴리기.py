N,M,y,x,K=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
d=[0,0,0,0,0,0]
def roll(c):
    global d
    q,w,e,r,t,y=d
    if c=='1':
        q,w,e,r,t,y=r,w,q,y,t,e
    if c=='2':
        q,w,e,r,t,y=e,w,y,q,t,r
    if c=='3':
        q,w,e,r,t,y=t,q,e,r,y,w
    if c=='4':
        q,w,e,r,t,y=w,y,e,r,q,t
    d=[q,w,e,r,t,y]
    
for i in input()[::2]:
    dy,dx=[0,(0,1),(0,-1),(-1,0),(1,0)][int(i)]
    ny,nx=y+dy,x+dx
    if 0<=ny<N and 0<=nx<M:
        y,x=ny,nx
        roll(i)
        if b[y][x]:
            d[5]=b[y][x]
            b[y][x]=0
        else:
            b[y][x]=d[5]
        print(d[0])