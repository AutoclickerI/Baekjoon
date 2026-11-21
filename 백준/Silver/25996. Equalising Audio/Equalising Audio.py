n,x,*a=map(int,open(0).read().split())
print(*map((any(a)and(n*x/sum(i*i for i in a))**.5).__mul__,a))