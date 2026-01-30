from collections import deque

def BFS(init_y,init_x):
    v=[w*[float('inf')]for _ in[0]*h]
    if init_y==-1:
        dq=deque(sorted((b[y][x]=='#',y,x)for y in range(h)for x in range(w)if(y in(0,h-1)or x in(0,w-1))and b[y][x]!='*'))
    else:
        dq=deque([(0,init_y,init_x)])
    for c,y,x in dq:
        v[y][x]=c
    while dq:
        c,y,x=dq.popleft()
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and b[ny][nx]!='*':
                nc=c+(b[ny][nx]=='#')
                if nc<v[ny][nx]:
                    v[ny][nx]=nc
                    if nc==c:
                        dq.appendleft((nc,ny,nx))
                    else:
                        dq+=(nc,ny,nx),
    return v

for T in[0]*int(input()):
    h,w=map(int,input().split())
    b=[input()for _ in[0]*h]
    p=[]
    for y in range(h):
        for x in range(w):
            if b[y][x]=='$':
                p+=(y,x),
    (y1,x1),(y2,x2)=p
    v1=BFS(-1,-1)
    v2=BFS(y1,x1)
    v3=BFS(y2,x2)
    mv=v1[y1][x1]+v1[y2][x2]
    for y in range(h):
        for x in range(w):
            mv=min(mv,v1[y][x]+v2[y][x]+v3[y][x]-(b[y][x]=='#')*2)
    print(mv)