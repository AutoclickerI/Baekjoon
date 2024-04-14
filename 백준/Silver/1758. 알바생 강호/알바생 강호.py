n,*a=map(int,open(0))
a.sort()
print(sum(max(a[~i]-i,0)for i in range(n)))