_,*l=map(int,open(0))
l.sort()
print(min(j-i for i,j in zip(l,l[2:]))/2)