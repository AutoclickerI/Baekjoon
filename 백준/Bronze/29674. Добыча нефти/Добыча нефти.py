n,m,s,*a=map(int,open(0).read().split())
for i in range(n):
 for j in range(i+1,n):
  d={}
  for k in range(m):(t:=a[i*m+k]+a[j*m+k])in d<exit(print(i+1,d[t]+1,j+1,k+1));d[s-t]=k
print(-1)