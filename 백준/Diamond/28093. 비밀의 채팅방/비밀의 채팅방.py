import time
import sys
import math
from random import*
sys.setrecursionlimit(10**5)
 
def pollardRho(n):
    if is_prime[n]:return n
    if n==1:return 1
    if n%2-1:return 2
    x=y=randrange(2, n);c=randrange(1, n);d=1
    f=lambda v:((v*v%n)+c+n)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime[d]:return d
    else:return pollardRho(d)
    
def factorize(n):
    d={}
    while n-1:
        p=pollardRho(n)
        d[p]=d.get(p,0)+1
        n//=p
    return d
 
mod=10**9+7
N,M=map(int,input().split())
s=time.time()
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
        if i==1:
            K+=1
            continue
        if i%2==0:
            continue
        K+=d[i]*pow(2,(n//i*(1-i)*pow(n,N-1,mod-1))%(mod-1),mod)
        K%=mod
    K=pow(n,mod-2,mod)*K%mod
    return K
origK=calculateK(M)
for i in range(1,M):
    if origK==calculateK(i):
        print(i)
        break;
else:
    print('Smart Oldbie')
#print(time.time()-s)