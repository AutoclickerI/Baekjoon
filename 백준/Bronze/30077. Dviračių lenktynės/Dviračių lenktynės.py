_,M,L,*t=map(int,open(0).read().split())
print(sum(~-M*i<M*min(t)for i in t))