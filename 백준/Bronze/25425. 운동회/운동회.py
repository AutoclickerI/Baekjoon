N,M,a,k=map(int,input().split())
r,q=divmod(a-k,M)
if q:r+=1
print(1+min(N-1,a-k),r+1)