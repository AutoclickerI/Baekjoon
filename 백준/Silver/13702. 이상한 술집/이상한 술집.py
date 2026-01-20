N,K,*l=map(int,open(0).read().split())
s=1
e=9**20
while 1<e-s:
    m=s+e>>1
    if K<=sum(i//m for i in l):
        s=m
    else:
        e=m
print(s)