R,C=map(int,input().split())
b=[input()for _ in[0]*R]
v=[C*[0]for _ in[0]*R]
l=[]
cnt=0
nxt=[]
def BFS(y,x,c):
    ss=[(y,x)]
    v[y][x]=c
    for y,x in ss:
        if b[y][x]=='L':
            l.append(c)
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C and v[ny][nx]<1:
                v[ny][nx]=c
                if b[ny][nx]=='X':
                    nxt.append((ny,nx,c))
                else:
                    ss+=(ny,nx),
for y in range(R):
    for x in range(C):
        if v[y][x]<1 and b[y][x]!='X':
            cnt+=1
            BFS(y,x,cnt)
l1,l2=l
*p,=range(cnt+1)
def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]
def merge(a,b):
    a,b=sorted([find(a),find(b)])
    p[b]=a
aa=0

while 1:
    for y,x,c in nxt:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C and c!=v[ny][nx]!=0:
                merge(c,v[ny][nx])
    if find(l1)==find(l2):
        break
    aa+=1
    tmp=[]
    for y,x,c in nxt:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C:
                if v[ny][nx]<1:
                    tmp+=(ny,nx,c),
                else:
                    merge(v[ny][nx],c)
                v[ny][nx]=c
    nxt=tmp
print((l1!=l2)*(aa+1))