n,t,*a=map(int,open(0).read().split())
print(sum(min(abs(x+~i)for i in range(t)if-1<t%~i)for x in a))