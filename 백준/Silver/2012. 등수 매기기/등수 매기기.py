_,*l=map(int,open(0))
print(sum(abs(j+~i)for i,j in enumerate(sorted(l))))