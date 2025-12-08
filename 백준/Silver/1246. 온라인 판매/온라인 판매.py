N,M,*l=map(int,open(m:=0).read().split())
p,q=max((i*min(N,sum(map(i.__le__,l))),-i)for i in l)
print(-q,p)