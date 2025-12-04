N,M,*l=map(int,open(0).read().split())

s=0
e=10**18
while 1<e-s:
    m=s+e>>1
    if-sum(i//-m for i in l)<=N:
        e=m
    else:
        s=m
print(e)