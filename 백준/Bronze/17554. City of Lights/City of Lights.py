n,_,*a=map(int,open(0).read().split())
c=[r:=0]*n
for x in a:
 i=x-1
 while i<n:c[i]^=1;i+=x
 r=max(r,sum(c))
print(r)