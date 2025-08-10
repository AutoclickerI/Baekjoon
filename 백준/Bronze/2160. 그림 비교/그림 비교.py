f=lambda x:''.join(a[5*x:5*x+5])
n,*a=open(0)
n,*l=int(n),
print(*min((sum(p!=q for p,q in zip(f(i),f(j))),i+1,j+1)for i in range(n)for j in range(i+1,n))[1:])