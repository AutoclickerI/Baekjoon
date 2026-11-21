n,m,*l=map(int,open(0).read().split())
for i,j in sorted(zip(l,l[n:])):m+=(j-i)*(m>i<j)
print(m)