n,x,y,r,*t=map(int,open(b:=0).read().split())
for i in t:l=abs(i-x);n-=l!=r;b+=l<r
print(b,n)