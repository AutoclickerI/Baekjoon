N,M,*A=map(int,open(0).read().split())
s=0
e=10**18
while 1<e-s:
    m=s+e>>1
    if sum(m//i for i in A)<M:
        s=m
    else:
        e=m
print(e)