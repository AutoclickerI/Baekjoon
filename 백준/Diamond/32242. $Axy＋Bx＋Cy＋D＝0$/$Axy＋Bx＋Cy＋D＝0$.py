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

def factorize(n):
    d={}
    while 1<n:
        v=pollardRho(n)
        d[v]=d.get(v,0)+1
        n//=v
    return d

def factors(n):
    d=factorize(n)
    r=[1]
    for j in d:
        r=[i*j**k for i in r for k in range(d[j]+1)]
    return sorted(r)

A,B,C,D=map(int,input().split())
if A==0:
    if B==C==0:
        if D==0:
            exit(print('INFINITY'))
        exit(print(0))
    if D%math.gcd(B,C):
        exit(print(0))
    exit(print('INFINITY'))
K=B*C-A*D
if K==0:
    if C%A==0 or B%A==0:
        exit(print('INFINITY'))
    exit(print(0))
comb=[(1,1),(1,-1),(-1,-1),(-1,1)][K<0::2]
K=abs(K)

fl=factors(K)
r=[]
for i in fl:
    for sp,sq in comb:
        lhs=i*sp
        rhs=K//i*sq
        if(lhs-C)%A==(rhs-B)%A==0:
            r+=((lhs-C)//A,(rhs-B)//A),
r.sort()
print(len(r))
for i in r:
    print(*i)