R,C=map(int,input().split())
b=[[*input()]for _ in[0]*R]

fires=[]
for y in range(R):
    for x in range(C):
        if b[y][x]=='J':
            l=[(1,y,x)]
        if b[y][x]=='F':
            fires+=(y,x),

def step():
    global fires
    nf=[]
    for y,x in fires:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C and b[ny][nx]not in'F#':
                b[ny][nx]='F'
                nf+=(ny,nx),
    fires=nf

v=[C*[0]for _ in[0]*R]
p=0
for c,y,x in l:
    if c!=p:step()
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<R and 0<=nx<C:
            if v[ny][nx]<1 and b[ny][nx]not in'#F':
                v[ny][nx]=1
                l+=(c+1,ny,nx),
        else:
            exit(print(c))
    p=c
print('IMPOSSIBLE')