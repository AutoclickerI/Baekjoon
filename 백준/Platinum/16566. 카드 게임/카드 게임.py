from bisect import*
def f(x):
 t=x
 while t-p[t]:t=p[t]
 p[x]=t;return t
N,a,l=[[*map(int,i.split())]for i in open(0)]
*p,=range(N[0])
a.sort()
for n in l:print(a[i:=f(bisect(a,n))]);p[i]=f(i+1)