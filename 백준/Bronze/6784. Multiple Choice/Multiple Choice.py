n,*l=open(0)
print(sum(i==j for i,j in zip(l[:int(n)],l[int(n):])))