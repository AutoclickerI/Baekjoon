_,n,*a=map(int,open(0).read().split())
m=r=0
for i in a:m=m or n;m-=i*(m>=i);r+=m<1
print(r,m)