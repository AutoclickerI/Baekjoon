M,N,*l=map(int,open(0).read().split())
s=1
e=10**9
get_sum=lambda:sum(i//m for i in l)
while s+1<e:
    m=(s+e+1)//2
    if get_sum()<M:
        e=m
    else:
        s=m
m=s
print((M<=get_sum())*s)