[N,M],*l=map(str.split,open(0))
n,v=zip(*l[:int(N)])
*v,=map(int,v)
from bisect import*
for[s]in l[int(N):]:print(n[bisect_left(v,int(s))])