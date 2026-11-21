n,*l=map(int,open(0).read().split())
print(sum((i>j)*2+(i>=j)for i,j in zip(l,l[n:])))