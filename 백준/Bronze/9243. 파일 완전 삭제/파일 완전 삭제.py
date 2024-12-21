n,a,b=open(0)
print('Deletion',['succeeded','failed'][any(int(n)&1^(i!=j)for i,j in zip(a,b[:-1]))])