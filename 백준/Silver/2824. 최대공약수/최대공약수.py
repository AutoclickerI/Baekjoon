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
    x=y=randrange(2, n);c=randrange(1, n);d=1
    f=lambda v:((v*v%n)+c+n)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime(d):return d
    else:return pollardRho(d)  

d={}
input()
for i in input().split():
    n=int(i)
    while 1<n:
        v=pollardRho(n)
        d[v]=d.get(v,0)+1
        n//=v
d2={}
input()
for i in input().split():
    n=int(i)
    while 1<n:
        v=pollardRho(n)
        d2[v]=d2.get(v,0)+1
        n//=v
n=1
for i in d:
    n*=i**min(d[i],d2.get(i,0))

if 10**9<=n:
    print(f'{n%10**9:09d}')
else:
    print(n)