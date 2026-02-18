import sys
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
    f=lambda v:((v*v%n)+c+n)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime(d):return d
    else:return pollardRho(d)

from bisect import*

for i in open(T:=0):
    T+=1
    N,t,b=map(int,i.split())
    t%=N
    d={}
    n=b
    while 1<n:
        v=pollardRho(n)
        d[v]=d.get(v,0)+1
        n//=v
    p=[1]
    for i in d:
        p=[k*i**j for k in p for j in range(d[i]+1)]
    p.sort()
    c=t//N*len(p)
    t%=N
    c+=bisect(p,t)
    print(f'Case {T}:','OOfnf'[c%2::2])