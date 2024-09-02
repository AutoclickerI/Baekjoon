n,x,*a=map(int,open(0).read().split())
t=any(a)and(n*x/sum(i*i for i in a))**.5
print(*map(t.__mul__,a))