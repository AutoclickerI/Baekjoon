N,*A=map(int,open(0))
A.sort()
print(sum(abs(A[i]+~i)for i in range(N)))