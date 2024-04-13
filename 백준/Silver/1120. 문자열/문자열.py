p,q=input().split()
print(min(sum(a!=b for a,b in zip(p,q[i:]))for i in range(len(q)-len(p)+1)))