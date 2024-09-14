N=int(input())
y,x=map(int,input().split())
s={(y,x)}
def degree(y,x):
    return sum(0<y+dy<=N>=x+dx>0 for dy,dx in[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]if (y+dy,x+dx)not in s)

ans=[]
while True:
    ans+=(y,x),
    q=[]
    for dy,dx in(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2):
        if 0<y+dy<=N>=x+dx>0 and (y+dy,x+dx)not in s:
            ny,nx=y+dy,x+dx
            q+=(degree(ny,nx),-abs((N+1)/2-ny)**2-abs((N+1)/2-nx)**2,y+dy,x+dx),
    if not q:
        break
    else:
        _,_,y,x=min(q)
        s.add((y,x))

if len(ans)!=N**2:
    print(-1)
else:
    for i in ans:
        print(*i)