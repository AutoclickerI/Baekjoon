[N,D],*l=[[*map(int,i.split())]for i in open(0)]

ms=0

d={}

for T,A,B in l:
    ms=max(ms,A+B)
    d[T]=max(d.get(T,0),B)

r=[0]
rt=[]
m=0
for i in sorted(d):
    m=max(m,d[i])
    r+=m,
    rt+=i,

from bisect import*

for T,A,B in l:
    lt=D-T
    ix=bisect_left(rt,lt+1)
    ms=max(ms,A+r[ix])
print(ms)