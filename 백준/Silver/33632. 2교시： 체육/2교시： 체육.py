W,H=map(int,input().split())

x,y=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())

if y<y1:
    print(0)
else:
    dy=y-y1
    dx1=x1-x
    dx2=x2-x
    nx1=min(max(x+dx1/dy*y,0),W)
    nx2=min(max(x+dx2/dy*y,0),W)
    print((nx2-nx1)/W)