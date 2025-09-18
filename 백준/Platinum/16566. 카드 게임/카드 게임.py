from bisect import*
def f(x):
 t=x
 while t-p[t]:t=p[t]
 p[x]=t;return t
(N,*_),a,l=[map(int,i.split())for i in open(0)]
*p,=range(N)
a=sorted(a)
for n in l:print(a[i:=f(bisect_left(a,n+1))]);p[i]=f(i+1)