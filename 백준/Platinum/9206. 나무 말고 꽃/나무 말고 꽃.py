from math import*
from decimal import*
getcontext().prec=99
F=factorial
R=range(999)
V,n=map(D:=Decimal,input().split())
ans=[]
for i in[0]*int(n):a,b,h=map(D,input().split());v=((b*b/2)*h**2+2*a*b*sum([(D(-1)**n/(F(n)*(2*n+D(3)/2)))*h**(2*n+D(3)/2)for n in R])+a*a*sum([(D(-2)**n/(F(n)*(2*n+1)))*h**(2*n+1)for n in R]));ans+=[abs(V-v*D(pi))]
print(ans.index(min(ans)))