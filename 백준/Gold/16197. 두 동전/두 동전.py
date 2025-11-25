N,M=map(int,input().split())
bb=[input()for _ in[0]*N]
c=[]
for y in range(N):
    for x in range(M):
        if bb[y][x]=='o':c+=(y,x),
[a,b],[c,d]=sorted(c)
v={(a,b,c,d):0}
l=[(0,a,b,c,d)]

def move(y,x,dy,dx):
    ny,nx=y+dy,x+dx
    if 0<=ny<N and 0<=nx<M:
        if bb[ny][nx]!='#':
            return ny,nx
        else:
            return y,x
    
for cost,a,b,c,d in l:
    if 9<cost:break
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        nab,ncd=move(a,b,dy,dx),move(c,d,dy,dx)
        if nab==None and ncd or nab and ncd==None:
            exit(print(cost+1))
        if nab and ncd:
            [na,nb],[nc,nd]=sorted([nab,ncd])
            if(na,nb,nc,nd)not in v:
                v[na,nb,nc,nd]=cost+1
                l+=(cost+1,na,nb,nc,nd),
print(-1)