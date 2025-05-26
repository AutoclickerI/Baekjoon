(N,Q),*l=[[*map(int,i.split())]for i in open(0)]

import math

d={}

x=[]

for q,i in l[N:]:
    if q<2:
        x=[i]
    else:
        x+=i,
x={*x}
for i in l[:N]:
    z=tuple(i[j-1]for j in x)
    d[z]=d.get(z,0)+1

a=1

for i in d:
    a*=math.factorial(d[i])

print(a%998244353)