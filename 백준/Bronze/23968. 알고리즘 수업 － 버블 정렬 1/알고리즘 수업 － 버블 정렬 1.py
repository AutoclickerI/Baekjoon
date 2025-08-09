N,K,*A=map(int,open(0).read().split())
for i in range(N*N):
 j=i%N
 if~j>i//N-N<A[j+1]<A[j]:z=A[j:j+2]=A[j+1],A[j];K-=1;K<1<exit(print(*z))
print(-1)