from decimal import*
from math import*
a,b,c=map(D:=Decimal,input().split())
l=1e-9
if(K:=b/a)<1:sin=lambda x:sum([(-1)**n*x**(2*n+1)/factorial(2*n+1)for n in range(23)]);l*=l
P,Q=c/a-K,c/a+K
f=lambda x:a*x+b*D(sin(x))
while f(Q-P)>l:
 if f(p:=(P+Q)/2)>c:Q=p
 else:P=p
print(f'{p:.6f}')