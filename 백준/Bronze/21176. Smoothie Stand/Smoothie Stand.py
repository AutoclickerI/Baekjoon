_,A,*l=[[*map(int,i.split())]for i in open(0)]
print(max(c*min(j//k for j,k in zip(A,i)if k)for *i,c in l))