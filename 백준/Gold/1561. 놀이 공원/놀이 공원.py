N,M,*l=map(int,open(0).read().split())
if N<=M:
    exit(print(N))
s=0
e=10**18
while 1<e-s:
    m=s+e>>1
    if sum(m//i+1 for i in l)<N:
        s=m
    else:
        e=m

N-=sum((e-1)//i+1 for i in l)
for i in range(M):
    if e%l[i]<1:
        N-=1
        if N<1:print(i+1);break