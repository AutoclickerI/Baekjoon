N,M,*A=map(int,open(i:=0).read().split())
while i<M:
 i+=1
 for n in range(1,N):
  if A[m:=n-1]%i>A[n]%i:A[m],A[n]=A[n],A[m]
print(*A)