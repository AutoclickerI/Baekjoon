n,*l=map(int,open(0))
l.sort()
print(min(i+j for i,j in zip(l,l[::-1])))