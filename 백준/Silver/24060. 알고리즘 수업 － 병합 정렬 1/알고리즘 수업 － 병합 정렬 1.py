N,K,*A=map(int,open(0).read().split())
T=[0,0]*N
C=[0,1]
def M(p,r):
 if p<r:q=(p+r)//2;M(p,q);M(q+1,r);m(p,q,r)
def m(p,q,r):
 i,j,t=p,q+1,1
 while i<=q<j<=r:
  if A[i]<=A[j]:T[t]=A[i];i+=1
  else:T[t]=A[j];j+=1
  t+=1
 while i<=q:T[t]=A[i];t+=1;i+=1
 while j<=r:T[t]=A[j];t+=1;j+=1
 i,t=p,1
 while i<=r:
  A[i]=T[t];t+=1;i+=1;C[0]+=1
  if K==C[0]:print(A[i-1]);C[1]=0
M(0,N-1)
if C[1]:print(-1)