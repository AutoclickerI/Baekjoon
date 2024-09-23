n=a=0
N=int(input())
while n<N:n=n*10+1
while N:r,N=divmod(N,n);a+=r;n//=10
print(a)