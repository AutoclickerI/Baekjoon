import math
N,*l=map(int,open(0).read().split())
f=[0]
for i in l:f+=math.gcd(i,f[-1]),
f+=0,
b=[0]
for i in l[::-1]:b+=math.gcd(i,b[-1]),
b=[0]+b[::-1]
r=-1
for i in range(1,N+1):
    gcd=math.gcd(f[i-1],b[i+1])
    if l[i-1]%gcd:
        if r<gcd:
            r=gcd
            a=l[i-1]
print(r)
if 0<r:print(a)