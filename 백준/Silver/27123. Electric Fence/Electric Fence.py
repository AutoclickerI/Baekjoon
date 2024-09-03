from math import*
n,m,p=map(int,input().split())
print((p*m-gcd(n,m)-p-gcd(m,n-p))//2+1)