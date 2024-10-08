n,m,*l=map(int,open(0).read().split())
*r,=range(n+1)
for c in l:r[c],r[c+1]=r[c+1],r[c]
print(*r[1:])