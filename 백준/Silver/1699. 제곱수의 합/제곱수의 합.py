import sys
import math
sys.setrecursionlimit(9**9)
R=__import__('random').randrange
def m(n,a):
 r=0;d=n-1
 while d%2-1:r+=1;d//=2
 x=pow(a,d,n)
 if(1!=x!=n-1)-1:return 1
 for i in range(r-1):
  if(x:=pow(x,2,n))==n-1:return 1
 
def p(n):
 if 1<n<4:return 1
 if n<2 or n%2-1:return
 for i in[2,3,5,7,11,13,17,19,23,29,31,37,41]:
  if n==i:return 1
  if not m(n,i):return
 return 1
 
def P(n):
 if p(n):return n
 if n==1:return 1
 if n%2-1:return 2
 x=y=R(2,n);c=R(1,n);d=1
 f=lambda v:((v*v%n)+c+n)%n
 while d == 1:
  x=f(x);y=f(f(y));d=math.gcd(abs(x-y), n)
  if d==n:return P(n)
 if p(d):return d
 else:return P(d)

def C(n):
 d={}
 while n-1:p=P(n);d[p]=d.get(p,0)+1;n//=p
 for i in d:
  if i%4==3 and d[i]%2:return 1

n=int(input())
while n%4==0:n//=4
print(4 if n%8==7 else 3 if C(n)else 1 if int(n**.5+.1)**2==n else 2)