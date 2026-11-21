m,n,*l=map(int,open(0).read().split())
a=[1]*m
while l:i,j,*l=l;a[i-1:j]=[0]*(j-i+1)
print('YNEOS'[any(a)::2])