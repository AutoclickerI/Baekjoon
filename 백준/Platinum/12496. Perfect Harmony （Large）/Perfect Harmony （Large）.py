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
        n//=v
        d[v]=d.get(v,0)+1
    return d

def divisors(n):
    d=factorize(n)
    r=[1]
    for i in d:
        r=[v*i**j for v in r for j in range(d[i]+1)]
    return sorted(r)

import math
for T in range(int(input())):
    N,L,H=map(int,input().split())
    l=sorted(map(int,input().split()))
    lcm=[l[0]]
    for i in l[1:]:
        lcm+=math.lcm(i,lcm[-1]),
    gcd=[l[-1]]
    for i in l[:-1][::-1]:
        gcd+=math.gcd(gcd[-1],i),
    gcd=gcd[::-1]
    v=float('inf')
    nv=((L-1)//lcm[-1]+1)*lcm[-1]
    if nv<=H:
        v=nv
    for ll,gg in zip(lcm,gcd[1:]):
        vv=[i for i in divisors(gg)if i%ll<1 and L<=i<=H]
        if vv:
            v=min(vv)
            break
    for i in divisors(gcd[0]):
        if L<=i<=H:
            v=i
            break
    if v==float('inf'):
        v='NO'
    print(f'Case #{T+1}:',v)