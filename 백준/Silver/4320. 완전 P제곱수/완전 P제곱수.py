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
    for i in[2,7,61]:
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

while(n:=int(input())):
    *F,=factorize(abs(n)).values()
    v=F[0]
    for i in F[1:]:
        v=math.gcd(v,i)
    if n<0:
        while 1-v%2:v//=2
    print(v)