import math

s=set()
for i in range(1001):
    for j in range(1001):
        if i or j:
            g=math.gcd(i,j)
            s.add((i//g,j//g))
r=[0]*1000
for i,j in s:
    r[max(i,j)-1]+=1

a=[0]
for i in r:a+=a[-1]+i,

for C in[*open(0)][1:]:
    print(a[int(C)])