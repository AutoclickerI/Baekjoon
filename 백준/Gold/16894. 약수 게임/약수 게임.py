import math
from random import*

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
    for i in[2,3,5,7,11,13,17,19,23,29,31,37,41]:
        if n==i:return 1
        if not miller_rabin(n,i):return
    return 1

def pollardRho(n):
    if is_prime(n):return n
    if n==1:return 1
    if n%2-1:return 2
    x=y=randrange(2,n);c=randrange(1,n);d=1
    f=lambda v:(v*v+c)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime(d):return d
    else:return pollardRho(d)

def factorize(n):
    d={}
    while 1<n:
        v=pollardRho(n)
        n//=v
        d[v]=d.get(v,0)+1
    return d

def factors(n):
    d=factorize(n)
    r=[1]
    for i in d:
        r=[v*i**j for j in range(d[i]+1)for v in r]
    return r[1:-1]

from functools import*

@cache
def recur(n):
    f=factors(n)
    if f==[]:
        return 1
    for v in f:
        if not recur(v):
            return 1
    return 0

print('ckuoboeslaogvae r'[recur(int(input()))::2])