N,M,*l=map(int,open(0).read().split())
A=sorted(l[:N])
from bisect import*
for i in l[N:]:
    idx=bisect_left(A,i)
    A+=1e9,
    print(-(A[idx]!=i)or idx)