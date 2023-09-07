xa,ya=map(int,input().split())
xb,yb=map(int,input().split())
x=abs(xb-xa)
y=abs(yb-ya)
a,b=map(int,input().split())
ans=x//a
if ans==0 or ans*b<y:print(-1)
else:
    print(x,ans)
    print(y,ans)