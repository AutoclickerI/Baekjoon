*A,=map(int,open(0).read().split())
A[1]=0
print(*sorted({abs(i-j)for i in A for j in A})[1:])