M,n=map(int,input().split())
d=y=x=0
p=[(0,1),(-1,0),(0,-1),(1,0)]
f=0
for _ in[0]*n:
    q,v=input().split()
    if q=='TURN':
        d+=-(v<'1')|1
    else:
        dy,dx=p[d%4]
        y+=dy*int(v)
        x+=dx*int(v)
        if M<x or M<y or x<0 or y<0:
            f=1
if f:
    print(-1)
else:
    print(x,y)