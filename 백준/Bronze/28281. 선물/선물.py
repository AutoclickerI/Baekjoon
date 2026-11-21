_,x,*l=map(int,open(0).read().split())
print(x*min(i+j for i,j in zip(l,l[1:])))