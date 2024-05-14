N,*A=map(int,open(0).read().split())
print(sum(max(N-a,0)for a in sorted(A[1::2])[1:]))