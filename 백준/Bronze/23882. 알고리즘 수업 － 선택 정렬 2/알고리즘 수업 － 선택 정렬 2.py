N,K,*A=map(int,open(0).read().split())
for i in range(N)[::-1]:
 v=A.index(max(A[:i+1]))
 if i!=v:K-=1;A[i],A[v]=A[v],A[i];K<1<exit(print(*A))
print(-1)