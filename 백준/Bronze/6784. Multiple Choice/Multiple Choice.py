n,*l=open(0)
print(sum(map(str.__eq__,l,l[int(n):])))