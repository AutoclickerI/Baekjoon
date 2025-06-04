n,*l=map(int,open(0).read().split())
print(sum(k*(i+j)for i,j,k in zip(l,l[1:],l[-n:]))/2)