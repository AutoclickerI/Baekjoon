n,*l=map(int,open(0))
for i in range(n):print(sum(j<l[i]for j in l[:i]))