n,*l=open(0)
n=int(n)
while n+1:
 if n==sum(int(i)<=n<=int(j)for i,j in map(str.split,l)):break
 n-=1
print(n)