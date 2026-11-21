from decimal import*
from math import*
a,b,c=map(D:=Decimal,input().split())
if b<a:sin=lambda x:sum(x*(-x*x)**n/factorial(2*n+1)for n in range(23))
s,e=c/a-b/a,c/a+b/a
while e-s>1e-22:
 if b*D(sin(m:=(s+e)/2))+a*m>c:e=m
 else:s=m
print(f'{s:.6f}')