N,K,*A=map(int,open(0).read().split())
def p(i,v):global K;A[i]=v;K-=1;K<1<exit(print(v))
for i in range(N):
 n=A[x:=i]
 while x>0<n<A[x-1]:p(x,A[x:=x-1])
 x<i!=p(x,n)
print(-1)