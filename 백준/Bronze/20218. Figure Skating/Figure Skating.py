n,*l=open(0)
n=int(n)
m=max(d:=[i-l[int(n):].index(l[i])for i in range(n)])
print(m and l[d.index(m)]or'suspicious')