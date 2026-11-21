n,m,*l=map(int,open(0).read().split())
*r,=range(n+1)
while l:a,b,*l=l;r[a],r[b]=r[b],r[a]
print(*r[1:])