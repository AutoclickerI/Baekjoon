n,*l=map(int,open(0).read().split())
print(sum(j<l[i]for i in range(n)for j in l[i:]))