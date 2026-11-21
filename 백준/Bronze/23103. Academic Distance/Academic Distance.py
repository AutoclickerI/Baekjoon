n,x,y,*l=map(int,open(a:=0).read().split())
while l:p,q,*l=l;a+=abs(x-p)+abs(y-q);x,y=p,q
print(a)