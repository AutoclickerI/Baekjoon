n,m,*a=map(int,open(0).read().split())
b=[0]*n
for i in a[n:]:
 for j in range(n):
  if a[j]<=i:b[j]+=1;break
print(b.index(max(b))+1)