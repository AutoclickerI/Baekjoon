n,m,*a=map(int,open(0).read().split())
s=[0]*n
for i in range(m):
 b=a[i*n+m:i*n+n+m]
 for j in range(n):s[[a[i]-1,j][a[i]==b[j]]]+=1
print(*s)