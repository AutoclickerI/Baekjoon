def f(s):
    a,b,c,d=map(int,s.split('.'))
    return a<<24|b<<16|c<<8|d

l=[f(i)for i in[*open(0)][1:]]
fz=2**32-1^l[0]
f=2**32-1

for i in l:
    f&=i^fz

ss=f'{f:b}'

print(32-len(ss.lstrip('1')))