N=int(input())
y,x=map(int,input().split())
s={(y,x)}
def degree(y,x):
    return sum(0<y+dy<=N>=x+dx>0 for dy,dx in[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]if (y+dy,x+dx)not in s)

ans=[]

def tiebreaker(pt):
    md=8
    ret=-1,-1
    for _,_,y,x in pt:
        s.add((y,x))
        d=8
        for dy,dx in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
            ny,nx=y+dy,x+dx
            if 0<ny<=N>=nx>0 and (ny,nx)not in s:
                d=min(degree(ny,nx),d)
        if d<md:
            md=d
            ret=y,x
        s.remove((y,x))
    return ret

while True:
    ans+=(y,x),
    q=[]
    for dy,dx in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
        ny,nx=y+dy,x+dx
        if 0<ny<=N>=nx>0 and (ny,nx)not in s:
            q+=(degree(ny,nx),-abs((N+1)/2-ny)**2-abs((N+1)/2-nx)**2,ny,nx),
    if not q:
        break
    else:
        deg,dist,y,x=min(q)
        pt=[i for i in q if i[:2]==(deg,dist)]
        if len(pt)>1:
            y,x=tiebreaker(pt)
        s.add((y,x))

if len(ans)!=N**2:
    print(-1)
else:
    for i in ans:
        print(*i)