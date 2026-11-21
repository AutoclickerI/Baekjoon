n,r,c=map(int,open(0).read().split())
print(+((n,r,c)==(3,2,2)or n<3)or(n+3//n)*(r-~c)%2+n*n//2)