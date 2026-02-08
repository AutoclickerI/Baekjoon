[N,M],p,*l=[[*map(int,i.split())]for i in open(0)]
p.sort()
from bisect import*
for s,e in l:print(bisect(p,e)-bisect(p,s-1))