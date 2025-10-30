R,C=map(int,input().split())
b=[input()for _ in[0]*R]
v=[C*[0]for _ in[0]*R]

def BFS(y,x):
    l=[(y,x)]
    v[y][x]=1
    V=O=0
    for y,x in l:
        V+=b[y][x]=='v'
        O+=b[y][x]=='o'
        for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C and v[ny][nx]<1 and b[ny][nx]!='#':
                v[ny][nx]=1
                l+=(ny,nx),
    return V,O

V=O=0
for y in range(R):
    for x in range(C):
        if v[y][x]<1 and b[y][x]!='#':
            vv,oo=BFS(y,x)
            if vv<oo:
                O+=oo
            else:
                V+=vv
print(O,V)