b=[i[::2]for i in open(0)]

v=set()

def DFS(y,x,s):
    if len(s)==6:
        v.add(s)
        return
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<5 and 0<=nx<5:
            DFS(ny,nx,s+b[ny][nx])

for y in range(5):
    for x in range(5):
        DFS(y,x,b[y][x])
print(len(v))