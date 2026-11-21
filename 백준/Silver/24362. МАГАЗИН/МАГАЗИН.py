n,k,*l=map(int,open(0).read().split())
l.sort()
print(sum(l[~i]for i in range(n)if~i%k))