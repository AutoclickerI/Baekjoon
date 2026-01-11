[N],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*N]
for s,e,p,q in l:
    edges[s]+=(e,q,p),
    edges[e]+=(s,p,q),

from fractions import*
v=[0]*N
v[0]=1
l=[(0,Fraction(1))]
for n,c in l:
    for e,p,q in edges[n]:
        if v[e]==0:
            v[e]=c*Fraction(p,q)
            l+=(e,v[e]),
import math
mv=1
for _,n in l:
    mv=math.lcm(mv,n.denominator)

for _,n in sorted(l):
    print(n*mv)