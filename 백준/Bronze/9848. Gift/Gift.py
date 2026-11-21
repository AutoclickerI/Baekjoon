_,k,*l=map(int,open(0).read().split())
print(sum(i-j>=k for i,j in zip(l,l[1:])))