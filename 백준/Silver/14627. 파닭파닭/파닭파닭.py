N,K,*l=map(int,open(0).read().split())

s=1
e=10**10
while 1<e-s:
    m=s+e>>1
    if sum(i//m for i in l)<K:
        e=m
    else:
        s=m
print(sum(l)-s*K)