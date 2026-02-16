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
    f=lambda v:(v*v+c)%n
    while d == 1:
        x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
        if d==n:return pollardRho(n)
    if is_prime(d):return d
    else:return pollardRho(d)

[N,M],A,*l=[[*map(int,i.split())]for i in open(0)]
s=[]
l.sort()
for i in l:
    if s and i[0]<=s[-1][1]:
        s[-1][1]=max(s[-1][1],i[1])
    else:
        s+=i,
r=0
t=1

for p,q in s+[(N+1,N)]:
    for t in range(t,p):
        r+=A[t-1]
    for t in range(p,q+1):
        d={}
        n=A[t-1]
        while 1<n:
            v=pollardRho(n)
            n//=v
            d[v]=1
        r+=sum(d)/len(d)
    t+=1
print(r)