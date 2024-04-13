_,*l=map(int,open(0))
print(sum(max(0,j-i)for i,j in enumerate(sorted(l)[::-1])))