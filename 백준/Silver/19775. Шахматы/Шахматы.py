n,*l=map(int,open(0).read().split())
for i in range(n):
 if l[i]<=i:n=i;break
print(n)
for i in range(1,1+n):print(i,i)