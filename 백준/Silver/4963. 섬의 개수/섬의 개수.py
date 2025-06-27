import sys
sys.setrecursionlimit(9**9)

def DFS(y,x,b,v):
    f=0
    if 0<=y<h and 0<=x<w and v[y][x]<1 and '0'<b[y][x]:
        f=1
        v[y][x]=1
        for dy in-1,0,1:
            for dx in-1,0,1:
                if dy==dx==0:continue
                ny,nx=y+dy,x+dx
                DFS(ny,nx,b,v)
    return f

while'1'<(s:=input()):
    w,h=map(int,s.split())
    b=[input()[::2]for _ in[0]*h]
    v=[w*[0]for _ in[0]*h]
    a=0
    for y in range(h):
        for x in range(w):
            a+=DFS(y,x,b,v)
    print(a)