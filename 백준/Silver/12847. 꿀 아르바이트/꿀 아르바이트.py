n,m,*T=map(int,open(0).read().split())
r=v=sum(T[:m])
for i in range(n-m):v+=T[i+m]-T[i];r=max(r,v)
print(r)