N,M,v=map(int,input().split())
b=[[*map(int,input()[::2])]for _ in[0]*N]
y,x=map(int,input().split())
y-=1
x-=1

clients={tuple(~-int(i)for i in input().split())for _ in[0]*M}
clientsstart={i[:2]:i[2:]for i in clients}

def findclients(s):
    v=[N*[0]for _ in[0]*N]
    l=[(0,*s)]
    targets=[]
    mc=float('inf')
    for cost,y,x in l:
        if mc<cost:
            break
        if(y,x)in clientsstart:
            mc=cost
            targets+=(y,x),
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and b[y][x]<1:
                v[ny][nx]=1
                l+=(cost+1,ny,nx),
    return mc,min(targets)

def todestination(s,e):
    v=[N*[0]for _ in[0]*N]
    l=[(0,*s)]
    for cost,y,x in l:
        if (y,x)==e:
            return cost
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and b[y][x]<1:
                v[ny][nx]=1
                l+=(cost+1,ny,nx),
    raise

try:
    while 1:
        mc,tar=findclients((y,x))
        v-=mc
        if v<0:
            raise
        cost=todestination(tar,clientsstart[tar])
        if v<cost:
            raise
        v+=cost
        y,x=clientsstart[tar]
        del clientsstart[tar]
except:
    if clientsstart:
        print(-1)
    else:
        print(v)