N,K,*l=map(int,open(0).read().split())
print(sum(sorted(j-i for i,j in zip(l,l[1:]))[:N-K]))