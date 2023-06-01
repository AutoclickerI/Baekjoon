import sys
import math
from random import*
from bisect import*
sys.setrecursionlimit(9**9)

def miller_rabin(n,a):
    r=0;d=n-1
    while d%2-1:r+=1;d//=2
    x=pow(a,d,n)
    if not 1!=x!=n-1:return 1
    for i in range(r-1):
      x=pow(x,2,n)
      if x==n-1:return 1
 
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
    d={}
    while n-1:
        p=pollardRho(n)
        d[p]=d.get(p,0)+1
        n//=p
    return d

def factors(d):
    l=[1]
    for i in[i**d[i]for i in d]:
        l+=[j*i for j in l]
    return sorted(l)

p,q=map(int,input().split())
F=factors(factorize(q//p))
M=F[0]+F[-1]
a=F[0]*p,F[-1]*p
for i in range(len(F)//2+1):
    if M>F[i]+F[-1-i]:
        M=F[i]+F[-1-i]
        a=F[i]*p,F[-1-i]*p
print(*a)