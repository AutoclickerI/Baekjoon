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

def backtrack(v,i,s,e):
    global f
    if e<v or i==len(l):
        return
    if s<=v:
        v2=n//v
        if sl==sorted(str(v2)+str(v)) and'00'not in str(v2)+str(v):
            raise
    if c[i]:
        c[i]-=1
        backtrack(v*l[i],i,s,e)
        c[i]+=1
    backtrack(v,i+1,s,e)
        

while n:=int(input()):
    f=1
    s=str(n)
    if len(s)%2:
        print(f'{s}:','no')
        continue
    sl=sorted(s)
    d={}
    while 1<n:
        v=pollardRho(n)
        d[v]=d.get(v,0)+1
        n//=v
    n=int(s)
    l=[]
    c=[]
    for i in sorted(d):
        l+=i,
        c+=d[i],
    try:
        backtrack(1,0,10**(len(s)//2-1),10**(len(s)//2)-1)
        print(f'{s}:','no')
    except:
        print(f'{s}:','yes')