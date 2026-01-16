n,*v=map(int,open(0).read().split())
print(sum((0<min(j,k))+(max(j,k)<i)for i,j,k in zip(v,v[n:],v[2*n:])))