N,M,*A=map(int,open(i:=0).read().split())
while i<M:
 i+=1;n=1
 while n<N:
  if A[m:=n-1]%i>A[n]%i:A[m],A[n]=A[n],A[m]
  n+=1
print(*A)