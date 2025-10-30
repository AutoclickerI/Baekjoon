b=[4*[0]for _ in[0]*4]
y=0
for i in open(0):
    x=0
    for n,d in zip(*[map(int,i.split())]*2):
        b[y][x]=(n,d%8)
        x+=1
    y+=1

e=b[0][0][0]
b[0][0]=(-1,b[0][0][1])

m=0
l=[(e,b)]

for e,b in l:
    sl=[b[y][x][0]for y in range(4)for x in range(4)if 0<b[y][x][0]]
    sl.sort()
    for i in sl:
        for cy in range(4):
            for cx in range(4):
                if b[cy][cx][0]==i:
                    y,x=cy,cx
        n,d=b[y][x]
        dy,dx=((-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1))[d]
        while y+dy<0 or 3<y+dy or x+dx<0 or 3<x+dx or b[y+dy][x+dx][0]<0:
            d=(d+1)%8
            dy,dx=((-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1))[d]
        b[y+dy][x+dx],b[y][x]=(b[y][x][0],d),b[y+dy][x+dx]
        
    for cy in range(4):
        for cx in range(4):
            if b[cy][cx][0]<0:
                y,x=cy,cx
    n,d=b[y][x]
    dy,dx=((-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1))[d]
    nxt=[]
    ny,nx=y+dy,x+dx
    while 0<=ny<4 and 0<=nx<4:
        if 0<b[ny][nx][0]:
            nxt+=(ny,nx),
        ny,nx=ny+dy,nx+dx
    if not nxt:
        m=max(m,e)
    else:
        b[y][x]=(0,0)
        for ny,nx in nxt:
            nb=[[*i]for i in b]
            nb[ny][nx]=(-1,nb[ny][nx][1])
            l+=(e+b[ny][nx][0],nb),
print(m)