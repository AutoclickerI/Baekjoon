s=open(0).read().split()[2:]
print(sum(i!=j for l in s+[*zip(*s)]for i,j in zip(l,l[1:])))