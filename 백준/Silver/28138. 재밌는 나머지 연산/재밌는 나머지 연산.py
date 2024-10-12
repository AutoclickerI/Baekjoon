import sys
import math
from random import*
sys.setrecursionlimit(9**9)

def miller_rabin(n,a):
    r=0;d=n-1
    while d%2-1:r+=1;d//=2
    x=pow(a,d,n)
    if not 1!=x!=n-1:return 1
    for i in range(r-1):
        if(x:=pow(x,2,n))==n-1:return 1
 
def is_prime(n):
    if n<2:return
    if n<4:return 1
    if n%2-1:return
    for i in[2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==i:return 1
        if not miller_rabin(n,i):return
    return 1
 
def pollardRho(n):
    if is_prime(n):return n
    if n==1:return 1
    if n%2-1:return 2
    x=y=randrange(2, n);c=randrange(1, n);d=1
    f=lambda v:((v*v%n)+c+n)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime(d):return d
    else:return pollardRho(d)
    
def factorize(n):
    d={1:1}
    while n-1:
        p=pollardRho(n)
        d[p]=d.get(p,0)+1
        n//=p
    return d

def factors(d):
    primes = list(d)
    l=[1]
    temp=[]
    for i in primes[1:]:
        for j in range(1,d[i]+1):
            temp+=[k*i**j for k in l]
        l+=temp
        temp=[]
    return sorted(l)

N,R=map(int,input().split())
print(sum(i*(R<i)for i in factors(factorize(N-R))))