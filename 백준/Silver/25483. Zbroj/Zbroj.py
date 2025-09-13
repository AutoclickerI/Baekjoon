X,Y,N=map(int,open(0).read().split())
l1=10**(X-1)
r1=10**X-1
l2=10**(Y-1)
r2=10**Y-1
if l1==1:l1=0
if l2==1:l2=0
mn=max(l1,N-r2)
mx=min(r1,N-l2)
c=mx-mn+1
print(c-c//2*(X==Y))