_,*l=map(int,open(0).read().split())
f=lambda n:max(min(l[n+1::4])-max(l[n::4]),0)
print(f(0)*f(2))