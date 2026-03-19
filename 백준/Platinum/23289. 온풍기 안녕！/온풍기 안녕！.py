RR,CC,K=map(int,input().split())
b=[input().split()for _ in[0]*RR]
dv=[CC*[0]for _ in[0]*RR]
v=[CC*[0]for _ in[0]*RR]
W=int(input())
w=set()

for _ in[0]*W:
    y,x,t=map(int,input().split())
    y-=1
    x-=1
    if t:
        w.add((y,x,y,x+1))
    else:
        w.add((y-1,x,y,x))

def getwall(p1,p2):
    if p2<p1:
        p1,p2=p2,p1
    return*p1,*p2

def check(y,x,mv):
    for dy,dx in mv:
        ny,nx=y+dy,x+dx
        if 0<=ny<RR and 0<=nx<CC:
            if getwall((y,x),(ny,nx))in w:
                return 0
            y,x=ny,nx
        else:
            return 0
    return y,x

chk=[]

for y in range(RR):
    for x in range(CC):
        if b[y][x]=='5':
            chk+=(y,x),
L,R,U,D=(0,-1),(0,1),(-1,0),(1,0)

for y in range(RR):
    for x in range(CC):
        if b[y][x]in'1234':
            if b[y][x]=='1':
                di=R
                lr=U,D
            if b[y][x]=='2':
                di=L
                lr=U,D
            if b[y][x]=='3':
                di=U
                lr=L,R
            if b[y][x]=='4':
                di=D
                lr=L,R
            if check(y,x,[di])==0:
                continue
            l=[(5,*check(y,x,[di]))]
            visit=set()
            for c,yy,xx in l:
                dv[yy][xx]+=c
                for mv in[(lr[0],di),(di,),(lr[1],di)]:
                    r=check(yy,xx,mv)
                    if r and r not in visit:
                        visit.add(r)
                        if 1<c:
                            l+=(c-1,*r),

for cnt in range(1,102):
    for y in range(RR):
        for x in range(CC):
            v[y][x]+=dv[y][x]
    mvt=[CC*[0]for _ in[0]*RR]
    for y in range(RR):
        for x in range(CC):
            for dy,dx in(0,-1),(0,1),(-1,0),(1,0):
                ny,nx=y+dy,x+dx
                if 0<=ny<RR and 0<=nx<CC and v[ny][nx]<v[y][x] and (not getwall((y,x),(ny,nx))in w):
                    mv=v[y][x]-v[ny][nx]>>2
                    mvt[y][x]-=mv
                    mvt[ny][nx]+=mv
    for y in range(RR):
        for x in range(CC):
            v[y][x]+=mvt[y][x]
    for y,x in{(0,i)for i in range(CC)}|{(RR-1,i)for i in range(CC)}|{(i,0)for i in range(RR)}|{(i,CC-1)for i in range(RR)}:
        v[y][x]-=0<v[y][x]
    if all(K<=v[yy][xx]for yy,xx in chk):
        break
print(cnt)