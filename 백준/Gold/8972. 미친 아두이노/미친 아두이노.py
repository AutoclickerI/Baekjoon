R,C=map(int,input().split())
b=[input()for _ in[0]*R]
s=input()

r=[]

for y in range(R):
    for x in range(C):
        if b[y][x]=='I':
            iy,ix=y,x
        if b[y][x]=='R':
            r+=(y,x),

def sign(n):
    if 0<n:
        return 1
    if 0==n:
        return 0
    return-1

cnt=0
for c in s:
    nb=[C*['.']for _ in[0]*R]
    nb[iy][ix]='.'
    dy,dx=[(y,x)for y in(1,0,-1)for x in(-1,0,1)][int(c)-1]
    iy+=dy
    ix+=dx
    cnt+=1
    if b[iy][ix]=='R':
        print('kraj',cnt)
        exit()
    nb[iy][ix]='I'
    nr=set()
    dr=[]
    for y,x in r:
        ny,nx=y+sign(iy-y),x+sign(ix-x)
        if nb[ny][nx]=='I':
            print('kraj',cnt)
            exit()
        if nb[ny][nx]=='R':
            dr+=(ny,nx),
        if nb[ny][nx]=='.':
            nb[ny][nx]='R'
        nr.add((ny,nx))
    for y,x in dr:
        nr.discard((y,x))
        nb[y][x]='.'
    b=nb
    r=nr
for i in b:
    print(*i,sep='')