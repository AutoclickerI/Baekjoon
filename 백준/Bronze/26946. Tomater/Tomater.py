n,d,*l=map(int,open(0).read().split())
print(sum(d>=min(abs(x+~i)for x in l)for i in range(n)))