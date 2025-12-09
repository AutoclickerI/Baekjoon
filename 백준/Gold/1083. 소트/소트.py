N,*A,S=map(int,open(0).read().split())
l=[]
while A and S:
    v=max(A[:S+1])
    l+=v,
    i=A.index(v)
    del A[i]
    S-=i
print(*l+A)