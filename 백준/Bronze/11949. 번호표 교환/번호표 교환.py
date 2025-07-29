N,M,*A=map(int,open(i:=0).read().split())
while i<M:
 i+=1
 for n in range(N-1):
  if A[m:=n+1]%i<A[n]%i:A[n],A[m]=A[m],A[n]
print(*A)