n,*l=map(eval,open(0))
print(sum(10<abs(i-sum(l)/n)for i in l))