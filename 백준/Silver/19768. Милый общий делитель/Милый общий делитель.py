from math import*
n=gcd(*map(int,input().split()))
a=0
for i in range(1,1+isqrt(n)):
    if n%i<1:a=max(a,i,n//i,key=lambda x:sum(int(a)for a in str(x)))
print(a)