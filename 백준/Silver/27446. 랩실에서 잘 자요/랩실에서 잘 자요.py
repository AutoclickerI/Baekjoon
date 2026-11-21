N,M,*l=map(int,open(0).read().split())
v=sorted({*range(1,N+1)}-{*l})
print(7*bool(v)+sum(min(2*(j-i),7)for i,j in zip(v,v[1:])))