n,*l=map(int,open(0).read().split())
l.sort()
m=max(j+l[-1-j]for j in range(n))
print(sum(i+n>m for i in l))