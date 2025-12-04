[N,M,K],*b=[[*map(int,i.split())]for i in open(0)]

v=[M*[0]for _ in[0]*N]
for y in range(N):
    for x in range(M):
        if v[y][x]<1:
            c=b[y][x]
            l=[(y,x)]
            v[y][x]=1
            for yy,xx in l:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=yy+dy,xx+dx
                    if 0<=ny<N and 0<=nx<M and v[ny][nx]<1 and b[ny][nx]==c:
                        l+=(ny,nx),
                        v[ny][nx]=1
            for yy,xx in l:v[yy][xx]=c*len(l)

dice=1,2,3,4,5,6

def move(dice,d):
    if d==0:
        p=5,1,3,4,6,2 
    if d==1:
        p=4,2,1,6,5,3
    if d==2:
        p=2,6,3,4,1,5
    if d==3:
        p=3,2,6,1,5,4
    return[dice[i-1]for i in p]
r=x=y=0
d=1
for _ in[0]*K:
    dy,dx=[(-1,0),(0,1),(1,0),(0,-1)][d]
    ny,nx=y+dy,x+dx
    if 0<=ny<N and 0<=nx<M:
        dice=move(dice,d)
    else:
        d^=2
        ny,nx=y-dy,x-dx
        dice=move(dice,d)
    r+=v[ny][nx]
    if dice[-1]>b[ny][nx]:
        d=d+1&3
    if dice[-1]<b[ny][nx]:
        d=d+3&3
    y,x=ny,nx
print(r)