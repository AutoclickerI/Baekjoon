N,K,*A=map(int,open(0).read().split())
for i in range(N):
 v=max(A[:N-i])
 if A[~i]-v:z=A[A.index(v)],A[~i]=A[~i],v;K-=1;K<1<exit(print(*z))
print(-1)