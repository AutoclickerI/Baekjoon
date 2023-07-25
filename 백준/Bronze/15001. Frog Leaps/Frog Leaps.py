_,*l=map(int,open(0))
print(sum((j-i)**2for i,j in zip(l,l[1:])))