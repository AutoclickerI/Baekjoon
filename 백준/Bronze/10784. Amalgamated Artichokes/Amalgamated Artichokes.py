from math import*
p,a,b,c,d,n=map(int,input().split())
m=x=0
for k in range(1,n+1):t=sin(a*k+b)+cos(c*k+d)+2;x=max(x,m-t);m=max(m,t)
print(x*p)