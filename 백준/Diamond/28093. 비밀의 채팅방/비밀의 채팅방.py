import math
from random import*
 
def pollardRho(n):
    if is_prime[n]:return n
    if n==1:return 1
    if~n%2:return 2
    x=y=randrange(2,n);c=randrange(1,n);d=1
    f=lambda v:((v*v%n)+c+n)%n
    while d==1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y),n)
        if d==n:return pollardRho(n)
    return d and is_prime[d]or pollardRho(d)
    
def factorize(n):
    d={}
    while n-1:
        p=pollardRho(n)
        d[p]=d.get(p,0)+1
        n//=p
    return d
 
mod=10**9+7
N,M=map(int,input().split())
is_prime=[*range(M+1)]
for i in range(2,M+1):
    if is_prime[i]:
        j=i*2
        while j<=M:
            is_prime[j]=0
            j+=i
 
def calculateK(n):
    F=factorize(n)
    d={1:1}
    for i in F:
        temp={**d}
        for k in d:
            for j in range(F[i]):
                temp[i**(j+1)*k]=i**j*(i-1)*d[k]
        d=temp
    K=0
    for i in d:
        if~i%2 or i==1:
            K+=i==1
            continue
        K+=d[i]*pow(2,(n//i*(1-i)*pow(n,N-1,mod-1))%(mod-1),mod)
        K%=mod
    return pow(n,-1,mod)*K%mod
origK=calculateK(M)
for i in range(1,M):origK==calculateK(i)and exit(print(i))
print('Smart Oldbie')