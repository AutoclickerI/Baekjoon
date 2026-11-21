N,D,*A=map(int,open(0).read().split())
A.sort()
print("YNeos"[any(D<j-i for i,j in zip(A[::2],A[1::2]))::2])