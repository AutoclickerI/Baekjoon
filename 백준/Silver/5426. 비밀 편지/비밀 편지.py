import math

for i in[*open(0)][1:]:
    i=i.strip()
    n=math.isqrt(len(i))
    for i in[*zip(*zip(*[iter(i)]*n))][::-1]:print(*i,sep='',end='')
    print()