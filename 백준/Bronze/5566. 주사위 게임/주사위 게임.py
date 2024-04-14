n,m,*a=map(int,open(0).read().split())
p=c=0
for j in a[n:]:
 if-~p<n:p+=j+a[p+j];c+=1
print(c)