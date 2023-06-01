m,n,*l=map(int,open(0).read().split())
a=[0]*m
while l:i,j,*l=l;a[i-1:j]=[1]*(j-i+1)
print(['NO','YES'][all(a)])