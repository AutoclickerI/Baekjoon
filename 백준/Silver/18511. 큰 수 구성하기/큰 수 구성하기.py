n,m,*l=map(int,open(0).read().split())
f=lambda m:m<=n and max(m,*[f(m*10+i)for i in l])
print(f(0))