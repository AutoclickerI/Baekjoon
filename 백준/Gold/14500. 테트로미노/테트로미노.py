tet=[((0,1),(0,2),(0,3)),
     ((0,1),(1,1),(1,0)),
     ((1,0),(2,0),(2,1)),
     ((1,0),(1,1),(2,1)),
     ((0,1),(1,1),(0,2))]

N,M=map(int,input().split())

def check(y,x,t):
    for dy,dx in t:
        ny,nx=y+dy,x+dx
        if len(b)<=ny or len(b[0])<=nx:
            return 0
    return 1

m=0
b=[[*map(int,input().split())]for _ in[0]*N]

def update():
    global m
    for y in range(len(b)):
        for x in range(len(b[0])):
            for t in tet:
                if check(y,x,t):
                    v=b[y][x]
                    for dy,dx in t:
                        ny,nx=y+dy,x+dx
                        v+=b[ny][nx]
                    m=max(m,v)

for _ in[0]*4:
    update()
    *b,=zip(*b)
    update()
    b=[i[::-1]for i in b]

print(m)