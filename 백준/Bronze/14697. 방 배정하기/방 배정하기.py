a,b,c,n=map(int,input().split())
k=301
print(+any(n==i%k*a+i//k%k*b+i//k//k*c for i in range(k**3)))