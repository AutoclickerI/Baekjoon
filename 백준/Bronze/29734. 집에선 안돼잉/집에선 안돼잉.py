n,m,t,s=map(int,open(0).read().split())
x,y=n+(n-1)//8*s,m+(m-1)//8*(2*t+s)+t
print('ZDiopk'[y<x::2],min(x,y))