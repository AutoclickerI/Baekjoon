n,*A=map(int,open(0).read().split())
a=b=x=0
for i in range(n):a+=A[i];b+=A[n+i];x=-~i*(a==b)or x
print(x)