n,*l=map(int,open(0))
print(sum(max(0,i-j)for i,j in zip(l,[min(l[:i+1])for i in range(n)])))