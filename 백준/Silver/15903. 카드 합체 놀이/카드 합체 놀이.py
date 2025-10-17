n,m,*l=map(int,open(0).read().split())
exec('p,q,*l=sorted(l);l+=[p+q]*2;'*m)
print(sum(l))