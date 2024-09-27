k,p,q,r,s,a=map(int,open(0).read().split())
x=a
for i in range(k-1):a=(p+r)*a+(q+s<<i);x+=a
print(x%(10**9+7))