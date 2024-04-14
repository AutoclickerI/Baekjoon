n,*l=map(int,open(0))
print(sum(max(sum(l)//n-i,0)for i in l))