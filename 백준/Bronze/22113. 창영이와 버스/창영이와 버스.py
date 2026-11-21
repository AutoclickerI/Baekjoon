n,m,*a=map(int,open(0).read().split())
print(sum(a[m+i*n+j+~n]for i,j in zip(a,a[1:m])))