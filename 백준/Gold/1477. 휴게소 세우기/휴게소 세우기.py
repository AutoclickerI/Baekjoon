N,M,*l=map(int,open(0).read().split())
l.sort()
*l,=map(int.__sub__,l,[0]+l)
s=0
e=9**9
while 1<e-s:
    m=s+e>>1
    if sum((i-1)//m for i in l)<=M:
        e=m
    else:
        s=m
print(e)