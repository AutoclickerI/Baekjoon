l,*X=[sorted(map(int,s.split()))[::-1]for s in open(0)]
print(l[1],sum(map(int.__mul__,*X)))