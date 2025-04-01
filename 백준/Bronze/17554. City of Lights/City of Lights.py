n,_,*a=map(int,open(0).read().split())
c=[r:=0]*n
for x in a:
 for i in range(x-1,n,x):c[i]^=1
 r=max(r,sum(c))
print(r)